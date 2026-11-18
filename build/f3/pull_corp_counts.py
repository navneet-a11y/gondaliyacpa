#!/usr/bin/env python3
"""Pull the F3 city-hub local data value from Corporations Canada open data.

Named repeatable source for plan line 1211. Run monthly, paste the printed
figures into CITY_DATA in build_cityhub.py, then rebuild the affected hubs.

Dataset: open.canada.ca 0032ce54-c5dd-4b66-99a0-320a7b5e99f2 ("Federal
Corporations"), refreshed daily at source. Resource URLs are resolved from the
CKAN package_show API rather than hardcoded, because the files moved to a CDN
host once already.

Counts active federal BUSINESS corporations (the CBCA file; every row in it
carries Status "Active") by registered-office City/town, restricted to the
city's own province and Country "CA".

Where a city has amalgamated, the former municipality names are counted with
it -- a registered office in Scarborough is a registered office in Toronto.
Both the literal and the amalgamated figure are printed so the choice stays
visible.

  python3 build/f3/pull_corp_counts.py              # all configured cities
  python3 build/f3/pull_corp_counts.py toronto      # one city
"""
import csv, json, os, sys, urllib.request

PKG = '0032ce54-c5dd-4b66-99a0-320a7b5e99f2'
API = f'https://open.canada.ca/data/en/api/3/action/package_show?id={PKG}'
RESOURCE = 'corporations-active-cbca-en.csv'
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_corpdata')

# slug -> (province code, [city/town values that count as this city])
CITIES = {
    'toronto':       ('ON', ['Toronto', 'Scarborough', 'North York',
                             'Etobicoke', 'York', 'East York']),
    'mississauga':   ('ON', ['Mississauga']),
    'brampton':      ('ON', ['Brampton']),
    'markham':       ('ON', ['Markham']),
    'vaughan':       ('ON', ['Vaughan', 'Woodbridge', 'Thornhill',
                             'Maple', 'Concord', 'Kleinburg']),
    'richmond-hill': ('ON', ['Richmond Hill']),
    'oakville':      ('ON', ['Oakville']),
    'ottawa':        ('ON', ['Ottawa', 'Nepean', 'Kanata', 'Gloucester',
                             'Orleans', 'Stittsville']),
    'oshawa':        ('ON', ['Oshawa']),
    'guelph':        ('ON', ['Guelph']),
    'hamilton':      ('ON', ['Hamilton', 'Ancaster', 'Dundas',
                             'Stoney Creek', 'Waterdown', 'Flamborough']),
    'windsor':       ('ON', ['Windsor']),
}


def resource_url():
    with urllib.request.urlopen(API, timeout=90) as r:
        meta = json.load(r)
    for res in meta['result']['resources']:
        url = res.get('url') or ''
        if url.rsplit('/', 1)[-1] == RESOURCE:
            return url
    raise SystemExit(f'{RESOURCE} not found in dataset {PKG}')


def fetch(url):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, RESOURCE)
    if os.path.exists(path):
        print(f'using cached {path}')
        return path
    print(f'downloading {url}')
    urllib.request.urlretrieve(url, path)
    return path


def main(argv):
    want = [a.lower() for a in argv[1:]] or list(CITIES)
    unknown = [w for w in want if w not in CITIES]
    if unknown:
        raise SystemExit(f'unknown city slug(s): {", ".join(unknown)}')

    # alias (province, casefolded city) -> slug
    lookup = {}
    for slug in want:
        prov, names = CITIES[slug]
        for n in names:
            lookup[(prov, n.casefold())] = slug

    tally = {s: {} for s in want}
    rows = skipped_status = 0
    path = fetch(resource_url())
    with open(path, encoding='utf-8-sig', newline='') as f:
        for row in csv.DictReader(f):
            rows += 1
            if (row.get('Status') or '').strip() != 'Active':
                skipped_status += 1
                continue
            if (row.get('Country') or '').strip().upper() != 'CA':
                continue
            key = ((row.get('Province/territory') or '').strip().upper(),
                   (row.get('City/town') or '').strip().casefold())
            slug = lookup.get(key)
            if slug:
                city = (row.get('City/town') or '').strip()
                tally[slug][city] = tally[slug].get(city, 0) + 1

    print(f'\n{rows:,} rows read ({skipped_status:,} not Active)\n')
    for slug in want:
        prov, names = CITIES[slug]
        got = tally[slug]
        literal = sum(v for k, v in got.items() if k.casefold() == names[0].casefold())
        total = sum(got.values())
        print(f'{slug}  ({prov})')
        print(f"  literal {names[0]!r:20s} {literal:>8,}")
        if len(names) > 1:
            for k in sorted(got, key=lambda x: -got[x]):
                if k.casefold() != names[0].casefold():
                    print(f'    + {k:<22s} {got[k]:>8,}')
            print(f'  {"amalgamated total":<30s} {total:>8,}')
        print()


if __name__ == '__main__':
    main(sys.argv)
