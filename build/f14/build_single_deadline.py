"""Generates the 'Single - Deadline' Elementor Pro theme template.

Plan refs:
  4.4 line 348 - F14 gets a Single Post template named "Single - Deadline",
                 display condition Singular / nil_deadline / all.
  7.5 byline rule 3 - F14 is bylined to the reviewing CPA directly, with the
                 exact wording reproduced below. Static, not dynamic: the
                 rule fixes one string for every page in the family.
  7.5 last-reviewed rule 1 - the visible line sits under the H1.

The banner reuses the city-hub hero so Family 14 matches the rest of the site:
media 328, dark overlay at 0.79, bottom center, cover, no-repeat.
"""
import json

NAVY = '#314D8A'
BYLINE = ('Written and reviewed by Sharad Gondaliya, CPA (Ontario), '
          'CPA Ontario Membership 61040184.')
HERO_IMG = ('https://corpnilfilingfor300.ca/wp-content/uploads/2026/10/'
            'closeup-blueprint-architecture-layout-plan_53876-147790.jpg')


def banner():
    return {
        "id": "d14ban01", "elType": "container",
        "settings": {
            "flex_direction": "column",
            "background_background": "classic",
            "background_image": {"id": 328, "url": HERO_IMG},
            "background_position": "bottom center",
            "background_size": "cover",
            "background_repeat": "no-repeat",
            "background_overlay_background": "classic",
            "background_overlay_color": "#0A0A0A",
            "background_overlay_opacity": {"unit": "px", "size": 0.79, "sizes": []},
            "padding": {"unit": "px", "top": "100", "right": "20",
                        "bottom": "100", "left": "20", "isLinked": False},
        },
        "elements": [{
            "id": "d14ban02", "elType": "container",
            "settings": {"flex_direction": "column", "content_width": "boxed",
                         "width": {"unit": "%", "size": 100}},
            "elements": [
                # H1 from the post title, so one template serves all 23.
                {"id": "d14h1", "elType": "widget", "widgetType": "theme-post-title",
                 "settings": {
                     "header_size": "h1", "align": "center",
                     "title_color": "#FFFFFF",
                     "typography_typography": "custom",
                     "typography_font_size": {"unit": "px", "size": 40},
                     "typography_font_size_tablet": {"unit": "px", "size": 32},
                     "typography_font_size_mobile": {"unit": "px", "size": 26},
                     "typography_font_weight": "700",
                     "typography_line_height": {"unit": "em", "size": 1.25},
                 }},
                # 7.5 rule 3. Fixed wording for the whole family.
                {"id": "d14byl", "elType": "widget", "widgetType": "text-editor",
                 "settings": {
                     "editor": '<p style="text-align:center">%s</p>' % BYLINE,
                     "text_color": "#E8ECF4",
                     "typography_typography": "custom",
                     "typography_font_size": {"unit": "px", "size": 14},
                     "typography_line_height": {"unit": "em", "size": 1.6},
                     "_margin": {"unit": "px", "top": "14", "right": "0",
                                 "bottom": "0", "left": "0", "isLinked": False},
                 }},
            ],
        }],
    }


def body():
    return {
        "id": "d14bod01", "elType": "container",
        "settings": {
            "flex_direction": "column", "content_width": "boxed",
            "padding": {"unit": "px", "top": "56", "right": "20",
                        "bottom": "72", "left": "20", "isLinked": False},
        },
        "elements": [
            {"id": "d14cont", "elType": "widget", "widgetType": "theme-post-content",
             "settings": {}},
        ],
    }


if __name__ == '__main__':
    tpl = {"version": "0.4", "title": "Single - Deadline",
           "type": "single-post", "content": [banner(), body()],
           "page_settings": []}
    out = 'build/elementor/corpnil-single-deadline.json'
    with open(out, 'w') as fh:
        json.dump(tpl, fh, indent=1)
    blob = json.dumps(tpl['content'])
    print('wrote %s  (%d bytes of _elementor_data)' % (out, len(blob)))
    assert BYLINE in blob, 'byline missing'
    assert 'theme-post-title' in blob and 'theme-post-content' in blob
    print('byline + dynamic title + post content: OK')
