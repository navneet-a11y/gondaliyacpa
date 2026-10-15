"""Generates the 'Single - Cost' Elementor Pro theme template.

Plan refs:
  4.4 line 342 - F8 gets a Single Post template named "Single - Cost",
                 condition Singular / nil_cost / all, dynamic tags
                 cnf_price_incl_hst, cnf_hst_component, cnf_included_rows_json,
                 cnf_excluded_rows_json. Note on that row: "Price block is a
                 single dynamic value so both sites cannot drift."
  7.5 rule 3   - Family 8 is one of the families bylined to the reviewing CPA
                 directly, so the byline is one fixed string, not per-author.

Built to the same shape as Single - Deadline (573): banner carrying the H1 from
the Post Title tag plus the fixed byline, then one Post Content widget.

NOT YET WIRED: the plan's dynamic price block and the two *_rows_json tags are
deliberately left out. See docs/decisions.md - a Post Custom Field tag prints a
meta value verbatim, so a JSON array renders as raw JSON rather than a list, and
the "single dynamic value" price block assumed the "including HST" wording that
Navneet's standing correction replaced. Both need a decision before they can be
built honestly.
"""
import json

BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')
HERO_IMG = ('https://corpnilfilingfor300.ca/wp-content/uploads/2026/09/'
            'business-executives-having-meeting_1098-18316.jpg')


def banner():
    return {
        "id": "f8ban01", "elType": "container",
        "settings": {
            "flex_direction": "column",
            "background_background": "classic",
            "background_image": {"id": 180, "url": HERO_IMG},
            "background_position": "center center",
            "background_size": "cover",
            "background_repeat": "no-repeat",
            "background_overlay_background": "classic",
            "background_overlay_color": "#0B1A33",
            "background_overlay_opacity": {"unit": "px", "size": 0.82, "sizes": []},
            "padding": {"unit": "px", "top": "40", "right": "20",
                        "bottom": "40", "left": "20", "isLinked": False},
        },
        "elements": [{
            "id": "f8ban02", "elType": "container",
            "settings": {"flex_direction": "column", "content_width": "boxed"},
            "elements": [
                {"id": "f8h1", "elType": "widget", "widgetType": "theme-post-title",
                 "settings": {
                     "header_size": "h1", "align": "left", "title_color": "#FFFFFF",
                     "typography_typography": "custom",
                     "typography_font_family": "Poppins",
                     "typography_font_size": {"unit": "px", "size": 40},
                     "typography_font_size_mobile": {"unit": "px", "size": 28},
                     "typography_font_weight": "700",
                     "typography_line_height": {"unit": "em", "size": 1.25},
                 }},
                {"id": "f8byl", "elType": "widget", "widgetType": "text-editor",
                 "settings": {
                     "editor": "<p>%s</p>" % BYLINE,
                     "text_color": "#E8ECF4", "align": "left",
                     "typography_typography": "custom",
                     "typography_font_size": {"unit": "px", "size": 15},
                     "typography_line_height": {"unit": "em", "size": 1.6},
                     "_margin": {"unit": "px", "top": "12", "right": "0",
                                 "bottom": "0", "left": "0", "isLinked": False},
                 }},
            ],
        }],
    }


def body():
    return {
        "id": "f8bod01", "elType": "container",
        "settings": {
            "flex_direction": "column", "content_width": "boxed",
            "padding": {"unit": "px", "top": "0", "right": "0",
                        "bottom": "0", "left": "0", "isLinked": True},
        },
        "elements": [{"id": "f8cont", "elType": "widget",
                      "widgetType": "theme-post-content", "settings": {}}],
    }


if __name__ == '__main__':
    tpl = {"version": "0.4", "title": "Single - Cost", "type": "single-post",
           "content": [banner(), body()], "page_settings": []}
    out = 'build/elementor/corpnil-single-cost.json'
    with open(out, 'w') as fh:
        json.dump(tpl, fh, indent=1)
    blob = json.dumps(tpl['content'])
    assert BYLINE in blob and 'theme-post-title' in blob and 'theme-post-content' in blob
    print('wrote %s (%d bytes of _elementor_data)' % (out, len(blob)))
    print('byline + dynamic title + post content: OK')
