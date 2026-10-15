# Author archive for Sharad Gondaliya — setup steps

Satisfies plan section 7.5, byline rule 5:

> Every bylined person has a live author archive at `/author/<first-last>/` with a
> real biography, credentials and a photo. No author archive is noindexed.

## The username is not the problem

WordPress builds the author archive URL from `user_nicename` — the user's **slug** —
not from `user_login`. The login stays `sharad7433` and nothing about signing in
changes. Only the slug has to move, and wp-admin simply has no field for it, which
is why it looks fixed.

Current state of user 1:

| Field | Now | Needs to be |
|---|---|---|
| `user_login` | `sharad7433` | unchanged — this is the login |
| `user_nicename` (slug) | `sharad7433` | `sharad-gondaliya` |
| `display_name` | Sharad Gondaliya, CPA | unchanged, already correct |
| `description` (Biographical Info) | *empty* | the bio below |
| `first_name` / `last_name` | *empty* | Sharad / Gondaliya |

The corpnil connector is read-only for users (`wp_get_user` and `wp_get_user_meta`
only), so this cannot be done from the Claude session. Step 1 below does it in one
pass.

## Step 1 — run this once in WPCode

WPCode → Add Snippet → Add Your Custom Code → **PHP Snippet**. Paste, set it to
*Run Everywhere*, Activate, then load any page on the site once. It writes itself
off with an option flag, so a second run does nothing. Deactivate and delete it
afterwards.

```php
add_action( 'init', function () {

	// Runs once, then disables itself.
	if ( get_option( 'cnf_author_profile_v1' ) ) {
		return;
	}

	$user = get_user_by( 'login', 'sharad7433' );
	if ( ! $user ) {
		return;
	}

	$bio = 'Sharad Gondaliya, CPA (Canada and USA). CPA Ontario Membership 61040184. '
		. 'Washington 57629. Montana PAC-CPAP-LIC-033176. '
		. 'Sharad is a Chartered Professional Accountant and the practising member of '
		. 'Gondaliya CPA Professional Corporation, the CPA Ontario registered firm behind '
		. 'corpnilfilingfor300.ca, CPA Ontario Firm Registration 61330051. He reviews the '
		. 'nil T2 returns filed through this service before they are transmitted to the '
		. 'Canada Revenue Agency.';

	wp_update_user( array(
		'ID'            => $user->ID,
		'user_nicename' => 'sharad-gondaliya',
		'display_name'  => 'Sharad Gondaliya, CPA',
		'first_name'    => 'Sharad',
		'last_name'     => 'Gondaliya',
		'description'   => $bio,
	) );

	update_option( 'cnf_author_profile_v1', 1 );
} );
```

The archive is then at `https://corpnilfilingfor300.ca/author/sharad-gondaliya/`.

The bio wording is drawn from plan line 381 (the Reviewing CPA block) and from the
bio page already live at `/sharad-gondaliya-cpa/`. It carries no EFILE number and no
CRA GroupID (hard rule 5), and says only that returns are *transmitted to* the CRA,
never *authorized* or *approved by* it (hard rule 1).

## Step 2 — the photo

Rule 5 wants a photo. WordPress shows a Gravatar by default, keyed to the profile
email, currently `sharad7433@gmail.com`. Either:

- set a Gravatar on that address at gravatar.com, or
- install a local-avatar plugin, which needs Sharad's approval first since it is a
  tool not already in the stack, or
- have the Astra author box pull the image — simplest if the theme's author box is
  already enabled.

Worth settling with Sharad, since the same photo belongs on `/about/` and in the
Person schema.

## Step 3 — do not let Rank Math suppress it

Rank Math → Titles & Meta → **Authors**:

- Author archives must be **enabled**. If they are switched off, Rank Math redirects
  `/author/...` to the home page and rule 5 cannot be met at all.
- The archive must not be set to noindex.

This is a launch-gate item, not a today item: hard rule 10 keeps the whole site
noindexed until Sharad confirms launch. The point is that when that site-wide
noindex comes off, the author archive must not stay behind with its own.

## What is already done

- `/sharad-gondaliya-cpa/` (page 473) and `/vandana-goel-cpa/` (page 475) are live,
  with the credentials table, the registry numbers and the firm registration.
- Display name already reads "Sharad Gondaliya, CPA".
- All 23 Family 14 pages carry the 7.5 rule 3 byline in the hero.

## Note on the bio page URLs

These stay at the root. Section 6(a) line 1153 lists `/our-cpas/`,
`/sharad-gondaliya-cpa/` and `/vandana-goel-cpa/` at the root, and line 322 registers
Family 15 with a `root` rewrite base. Appendix A instead gives `/team/`,
`/team/sharad-gondaliya-cpa/`, `/team/vandana-goel-cpa/`, `/team/navneet/`,
`/team/deepak/` and `/team/second-reviewing-cpa/`.

That is the seventh Appendix A conflict found so far, and it is resolved the same way
as the previous six: follow 6(a), because the CPT rewrite table agrees with it. No
page moves, and the four internal links to `/sharad-gondaliya-cpa/` stay valid.

`/our-cpas/`, the third Family 15 page naming both CPAs, is still unbuilt.
