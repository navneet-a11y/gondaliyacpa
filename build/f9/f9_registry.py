"""The Family 9 guide registry, shared by all three generators.

Every guide lists all eleven others, so each of the twelve carries eleven
sibling inbound links plus the hub. That is what meets the 6(g) line 1528
minimum of 12 inbound for Family 9. Keeping the list in one module means
adding guide 13 updates the sibling list on all twelve at once, rather than
leaving the earlier ones stale.

Order is publication order.
"""

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
]

HUB = 'https://corpnilfilingfor300.ca/guides/'

def sibling_links(own_slug):
    """The eleven <li> rows every guide carries, excluding itself."""
    return '\n'.join('<li><a href="%s%s/">%s</a></li>' % (HUB, s, t)
                     for s, t in REGISTRY if s != own_slug)
