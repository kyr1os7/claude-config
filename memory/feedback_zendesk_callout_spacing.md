---
name: feedback-zendesk-callout-spacing
description: "Zendesk Help Center article callout boxes need a spacer <p> before the next heading, not inline div margin, or spacing looks broken"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 782ee77e-cb23-4529-8d86-dbb82e8378d6
  modified: 2026-09-09T14:42:52.215Z
---

When a callout box (`<div style="background:#e7f3fe...">` info, or `<div style="background:#fff3cd...">` warning) is immediately followed by an `<h2>`/`<h3>` heading in a Zendesk Help Center article body, insert a spacer paragraph between them:

```html
</div>
<p>&nbsp;</p>
<h2>Next heading</h2>
```

One `<p>&nbsp;</p>` is the right amount — do not use two (tested and confirmed too wide/loose by the user).

**Why:** Increasing the callout `<div>`'s inline `margin`/`padding` (tried 15px → 28/32px → 40/48px) produced **zero visible change** in the rendered page — the site's Zendesk theme CSS overrides or strips inline margin on these divs. A spacer paragraph works because it rides on the theme's own paragraph margin, which is reliably applied everywhere else in the article body.

**Note:** Zendesk's API silently converts `&nbsp;` to the literal Unicode non-breaking-space character (`\xa0`) when it stores the body — so if scripting a search/replace against the body fetched back from the API, match on `\xa0`, not the literal string `&nbsp;`.

**How to apply:** Whenever writing or editing a Help Center article body with a callout div directly followed by a heading, always add the `<p>&nbsp;</p>` spacer line between them. This applies to the [[reference_zendesk_helpcenter_api]] project — the 生活・就労ガイドブック migration and any other Funtoco Help Center article work.
