"""The Family 9 guide registry, shared by every generator.

Order is publication order. Adding a guide here changes the sibling list on
every earlier guide, so all batches must be regenerated and the live guides
updated, or their sibling lists silently omit the new entries.

Why the sibling list is a window rather than the whole family
------------------------------------------------------------
Until guide 17 every guide listed all the others. That met the 6(g) minimum of
12 inbound comfortably, but it does not scale: the sibling list grows with the
family while 6(g) also caps outbound links at 40. Measured at 17 guides, the
pillar already carried 34 outbound links, and ten more guides would have taken
it to 44 -- over the cap. At the full 30 the design is unbuildable.

So each guide now links the next WINDOW guides in registry order, wrapping
round. That is a circulant digraph: every guide links out to exactly 12 and is
linked to by exactly 12, whatever the family's size. With the hub that is 13
inbound against a minimum of 12, and outbound drops by 14 links on every guide,
leaving headroom to 30 and beyond. assert_regular() below proves the inbound
count rather than trusting the construction.
"""

WINDOW = 12

REGISTRY = [
 ('nil-t2-return-complete-guide', 'The Complete Guide to the Nil T2 Return'),
 ('dormant-and-inactive-corporations',
  'The Complete Guide to Dormant and Inactive Corporations'),
 ('catch-up-unfiled-corporate-tax-returns',
  'The Complete Guide to Catching Up on Unfiled Corporate Tax Returns'),
 ('final-t2-and-dissolution', 'The Complete Guide to the Final T2 and Dissolution'),
 ('t2-short-eligibility', 'The Complete Guide to T2 Short Eligibility'),
 ('provincial-and-federal-annual-returns',
  'The Complete Guide to Provincial and Federal Annual Returns'),
 ('t183corp-signing-and-transmission',
  'The Complete Guide to Form T183CORP Signing and Transmission'),
 ('how-to-file-a-nil-t2-return', 'How to File a Nil T2 Return'),
 ('gifi-schedules-100-125-141',
  'The Complete Guide to GIFI Schedules 100, 125 and 141'),
 ('schedule-8-and-loss-continuity',
  'The Complete Guide to Schedule 8 and Loss Continuity'),
 ('first-year-t2-filing', 'The Complete Guide to First-Year T2 Filing'),
 ('numbered-company-tax-filing',
  'The Complete Guide to Numbered Company Tax Filing'),
 ('t2-late-filing-penalties', 'The Complete Guide to T2 Late Filing Penalties'),
 ('cra-demand-to-file-response',
  'The Complete Guide to Responding to a CRA Demand to File'),
 ('inactive-holding-company-filing',
  'The Complete Guide to Inactive Holding Company Filing'),
 ('t2-schedules-on-a-nil-return',
  'The Complete Guide to T2 Schedules on a Nil Return'),
 ('shelf-corporation-compliance',
  'The Complete Guide to Shelf Corporation Compliance'),
 # Batch 5, guides 18 to 27.
 ('t2-filing-deadlines', 'The Complete Guide to T2 Filing Deadlines'),
 ('zero-activity-corporate-tax-returns',
  'The Complete Guide to Zero-Activity Corporate Tax Returns'),
 ('corporate-tax-arrears-and-interest',
  'The Complete Guide to Corporate Tax Arrears and Interest'),
 ('winding-up-an-inactive-corporation',
  'The Complete Guide to Winding Up an Inactive Corporation'),
 ('small-business-corporate-filing',
  'The Complete Guide to Small Business Corporate Filing'),
 ('corporate-compliance-calendar',
  'The Complete Guide to the Corporate Compliance Calendar'),
 ('numbered-company-maintenance',
  'The Complete Guide to Numbered Company Maintenance'),
 ('mandatory-t2-electronic-filing',
  'The Complete Guide to Mandatory T2 Electronic Filing'),
 ('schedule-50-and-shareholder-reporting',
  'The Complete Guide to Schedule 50 and Shareholder Reporting'),
 ('non-resident-owned-corporation-nil-filing',
  'The Complete Guide to Non-Resident-Owned Corporation Nil Filing'),
 # Batch 6, guides 28 to 30, which complete the family at the plan's 30.
 #
 # Appendix A's F9 list could not supply these: it was exhausted at 27, and
 # what remained in it were naming variants of guides already live. All three
 # topics below are instead backed by approved blog topics in the plan's
 # section at line 2206, so every fact they assert has a source:
 #
 #   28  "Open GST/HST Accounts Still Need Nil Filings", "Closing a GST/HST
 #       Account With Form RC145", "Nil Payroll Accounts and Your Remittance
 #       Obligation"
 #   29  "Your First Tax Year Cannot Exceed 53 Weeks", "Why a Wrong Year-End
 #       Gets Your T2 Transmission Rejected"
 #   30  "Quebec CO-17 Is a Separate Provincial Return", "Alberta AT1 Is a
 #       Separate Provincial Return", and hard rule 8
 #
 # Each also has live Family 2 tools to link down to, which is what the
 # pillar-to-tool-to-form path in 6(g) wants.
 ('cra-accounts-on-a-dormant-corporation',
  'The Complete Guide to CRA Accounts on a Dormant Corporation'),
 ('choosing-and-changing-a-fiscal-year-end',
  'The Complete Guide to Choosing and Changing a Fiscal Year-End'),
 ('quebec-co17-and-alberta-at1',
  'The Complete Guide to Quebec CO-17 and Alberta AT1'),
]

HUB = 'https://corpnilfilingfor300.ca/guides/'

SLUGS = [s for s, _t in REGISTRY]
assert len(set(SLUGS)) == len(SLUGS), 'duplicate slug in the registry'
assert len(REGISTRY) > WINDOW, 'the window must be smaller than the family'
for _s, _t in REGISTRY:
    assert '2026' not in _s and '2027' not in _s, (
        'year token in guide slug %r; 6(k) forbids it outright' % _s)


def siblings(own_slug):
    """The WINDOW guides this one links to: the next ones in order, wrapping."""
    i = SLUGS.index(own_slug)
    n = len(REGISTRY)
    return [REGISTRY[(i + k) % n] for k in range(1, WINDOW + 1)]


def sibling_links(own_slug):
    """The WINDOW <li> rows every guide carries, excluding itself."""
    return '\n'.join('<li><a href="%s%s/">%s</a></li>' % (HUB, s, t)
                     for s, t in siblings(own_slug))


def assert_regular():
    """Prove every guide receives exactly WINDOW sibling links.

    6(g) sets a minimum of 12 inbound for Family 9. The window only satisfies
    it if the digraph really is regular, so count it rather than assume it.
    """
    inbound = {s: 0 for s in SLUGS}
    for s in SLUGS:
        for t, _title in siblings(s):
            assert t != s, 'guide %r links to itself' % s
            inbound[t] += 1
    bad = {s: n for s, n in inbound.items() if n != WINDOW}
    assert not bad, 'uneven inbound: %r' % bad
    return inbound


assert_regular()

if __name__ == '__main__':
    inbound = assert_regular()
    print('%d guides, window %d' % (len(REGISTRY), WINDOW))
    print('every guide: %d sibling inbound + 1 hub = %d, against a 6(g) minimum of 12'
          % (WINDOW, WINDOW + 1))
    print('outbound sibling links per guide: %d (was %d with a full list)'
          % (WINDOW, len(REGISTRY) - 1))
