"""WordPress REST publisher for a generated manifest.

This is the October 7 deliverable: the pipeline that publishes with meta, terms
and Rank Math fields, with the banned-phrase sweep refusing a bad publish.

It runs on Navneet's machine against the live REST API with an application
password, so a 23-page batch and a 336-page batch cost the same effort.

  Setup once:
    WordPress, Users, Profile, Application Passwords. Create one named
    "cnf-pipeline". Copy the generated password.

    export CNF_USER='navneet'
    export CNF_APP_PASSWORD='xxxx xxxx xxxx xxxx xxxx xxxx'

  Dry run first, which publishes nothing:
    python3 publish.py f14-manifest.json nil_deadline --dry-run

  Then for real:
    python3 publish.py f14-manifest.json nil_deadline

  Ten records only, matching the plan's done-when:
    python3 publish.py f14-manifest.json nil_deadline --limit 10

Behaviour worth knowing:
  - The gate runs first. If any record fails, nothing publishes at all.
  - Existing slugs are updated, not duplicated, so re-running is safe.
  - Items are created as draft unless --publish is passed. Family 14 is
    reviewed by Sharad Gondaliya before it goes live, so draft is the default.
"""
import json, os, sys, time, base64, urllib.request, urllib.error, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate import check

SITE = os.environ.get('CNF_SITE', 'https://corpnilfilingfor300.ca')
USER = os.environ.get('CNF_USER')
PW   = os.environ.get('CNF_APP_PASSWORD')

def call(method, path, payload=None):
    url = f'{SITE}/wp-json{path}'
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header('Content-Type', 'application/json')
    tok = base64.b64encode(f'{USER}:{PW}'.encode()).decode()
    req.add_header('Authorization', f'Basic {tok}')
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())

def find_by_slug(base, slug):
    q = urllib.parse.urlencode({'slug': slug, 'status': 'publish,draft,pending'})
    try:
        hits = call('GET', f'/wp/v2/{base}?{q}')
        return hits[0]['id'] if hits else None
    except urllib.error.HTTPError:
        return None

def main():
    manifest, base = sys.argv[1], sys.argv[2]
    dry     = '--dry-run' in sys.argv
    go_live = '--publish' in sys.argv
    limit   = None
    if '--limit' in sys.argv:
        limit = int(sys.argv[sys.argv.index('--limit') + 1])

    recs = json.load(open(manifest))
    if limit: recs = recs[:limit]

    # Gate first. One failure stops the whole batch.
    failed = [(r['slug'], check(r)) for r in recs]
    failed = [(s, f) for s, f in failed if f]
    if failed:
        for s, f in failed:
            print(f'  REFUSED  {s}: {", ".join(f)}')
        print(f'\nPUBLISH REFUSED. {len(failed)} of {len(recs)} records carry banned content.')
        sys.exit(1)
    print(f'gate clear: {len(recs)} records')

    if dry:
        for r in recs:
            print(f'  would publish  {base}/{r["slug"]:46s} {len(r["content"]):>6,} b  '
                  f'{len(r.get("meta",{}))} meta  {sum(len(v) for v in r.get("terms",{}).values())} terms')
        print('\ndry run, nothing written')
        return
    if not (USER and PW):
        print('CNF_USER and CNF_APP_PASSWORD must be set'); sys.exit(2)

    status = 'publish' if go_live else 'draft'
    done = 0
    for r in recs:
        body = {'title': r['title'], 'slug': r['slug'], 'content': r['content'], 'status': status}
        if r.get('meta'): body['meta'] = r['meta']
        for tax, terms in (r.get('terms') or {}).items():
            if terms: body[tax] = terms
        existing = find_by_slug(base, r['slug'])
        try:
            if existing:
                res = call('POST', f'/wp/v2/{base}/{existing}', body); verb = 'updated'
            else:
                res = call('POST', f'/wp/v2/{base}', body); verb = 'created'
            print(f'  {verb:8s} {res["id"]:>5}  {res["link"]}')
            done += 1
        except urllib.error.HTTPError as e:
            print(f'  FAILED   {r["slug"]}: HTTP {e.code} {e.read().decode()[:160]}')
        time.sleep(0.4)          # stay under the WAF rate limit
    print(f'\n{done} of {len(recs)} written as {status}')

if __name__ == '__main__':
    main()
