# Splits the generated hub into the two pieces that survive an Elementor
# rebuild, with the Posts widget taking the place of the hand-written cards.
import io, os

src = open('blog-hub.html').read().split('\n')

# Elementor's Posts widget (classic skin) dressed to match .ei-card exactly,
# so the dynamic grid is indistinguishable from the cards it replaces.
POSTS_CSS = """
.elementor-posts .elementor-post{border:1px solid #e2e8f0;border-radius:10px;background:#fff;padding:0;overflow:hidden;transition:box-shadow .15s ease,border-color .15s ease}
.elementor-posts .elementor-post:hover{border-color:#cfe4f6;box-shadow:0 2px 10px rgba(26,35,64,.07)}
.elementor-posts .elementor-post__thumbnail{padding:0;border-bottom:1px solid #e2e8f0}
.elementor-posts .elementor-post__thumbnail img{width:100%;height:auto;display:block}
.elementor-posts .elementor-post__text{padding:18px 20px;margin:0}
.elementor-posts .elementor-post__title{margin:0 0 6px;font-size:1.08em;font-weight:700;line-height:1.35}
.elementor-posts .elementor-post__title a{color:#1a2340;text-decoration:none}
.elementor-posts .elementor-post:hover .elementor-post__title a{color:rgba(32,135,201,1)}
.elementor-posts .elementor-post__excerpt p{margin:0;color:#4a5568;font-size:.94em;line-height:1.65}
.elementor-posts .elementor-post__meta-data{margin:0 0 6px;padding:0;border:0;color:#6b7280;font-size:.85em}
.elementor-posts .elementor-post__read-more{color:rgba(32,135,201,1);font-weight:700;font-size:.9em;text-decoration:none}
.elementor-pagination{margin-top:18px;text-align:center}
.elementor-pagination .page-numbers{color:#4a5568;padding:6px 12px;border:1px solid #e2e8f0;border-radius:6px;margin:0 3px;text-decoration:none;display:inline-block}
.elementor-pagination .page-numbers.current{background:rgba(32,135,201,1);border-color:rgba(32,135,201,1);color:#fff}
"""

close = src.index('</style>')                      # line 38, zero-based 37
head = '\n'.join(src[:close]) + POSTS_CSS + '</style>\n'

# Part 1: everything down to the "Every Post on This Site" heading, wrappers
# closed. Sliced to wherever the card grid starts rather than to a fixed
# three-line offset, which silently dropped any line added to the section --
# as it did when the live child count was put back in.
cards_open = src.index('<div class="ei-cards">')
hero = '\n'.join(src[close + 1:cards_open])
part1 = head + hero + '\n</div></div>\n'

# Part 2: the "Also on This Site" links and the bottom CTA, untouched.
alt = src.index('<div class="ei-section-alt"><div class="ei-wrap ei-art">')
part2 = '\n'.join(src[alt:]).rstrip() + '\n'

open('blog-part1-hero.html', 'w').write(part1)
open('blog-part2-links.html', 'w').write(part2)

# The two parts plus the Posts widget must account for the whole hub: what is
# dropped should be exactly the hand-written card grid and nothing else.
dropped = '\n'.join(src[cards_open:alt])
print('part1  %5d bytes' % len(part1))
print('part2  %5d bytes' % len(part2))
print('dropped %4d bytes:' % len(dropped))
print(dropped[:200])
