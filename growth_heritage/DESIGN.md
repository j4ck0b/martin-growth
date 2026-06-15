---
name: Growth & Heritage
colors:
  surface: '#f9f9f7'
  surface-dim: '#dadad8'
  surface-bright: '#f9f9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f2'
  surface-container: '#eeeeec'
  surface-container-high: '#e8e8e6'
  surface-container-highest: '#e2e3e1'
  on-surface: '#1a1c1b'
  on-surface-variant: '#474741'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f1ef'
  outline: '#777771'
  outline-variant: '#c8c7bf'
  surface-tint: '#5f5e5c'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1c1a'
  on-primary-container: '#858481'
  inverse-primary: '#c9c6c3'
  secondary: '#466553'
  on-secondary: '#ffffff'
  secondary-container: '#c8ebd3'
  on-secondary-container: '#4c6b59'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#251a00'
  on-tertiary-container: '#a37f15'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2de'
  primary-fixed-dim: '#c9c6c3'
  on-primary-fixed: '#1c1c1a'
  on-primary-fixed-variant: '#474744'
  secondary-fixed: '#c8ebd3'
  secondary-fixed-dim: '#adcfb8'
  on-secondary-fixed: '#022112'
  on-secondary-fixed-variant: '#2f4d3c'
  tertiary-fixed: '#ffdf97'
  tertiary-fixed-dim: '#ecc155'
  on-tertiary-fixed: '#251a00'
  on-tertiary-fixed-variant: '#5a4400'
  background: '#f9f9f7'
  on-background: '#1a1c1b'
  surface-variant: '#e2e3e1'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 72px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
  table-data:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  container-max: 1280px
  margin-desktop: 80px
  margin-mobile: 24px
  gutter: 32px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
  stack-xl: 96px
---

## Brand & Style

This design system is built for an audience that values discretion, structural integrity, and long-term operational excellence. The brand personality is **authoritative, hands-on, and intellectually rigorous.** 

The aesthetic draws heavily from **Minimalism** and **Editorial Design**, specifically echoing the tactile quality of a boutique private equity annual report or a prestige law firm's identity. 

**Key Visual Principles:**
- **Restraint:** Every element must serve a functional or structural purpose. If it doesn't contribute to the hierarchy, remove it.
- **Precision:** Alignment is absolute. Use thin lines to define space rather than shadows or color blocks.
- **Sophistication:** High-contrast typography and a restricted, nature-inspired palette evoke a sense of heritage and permanence.
- **Voice:** Professional and results-oriented. Use Polish as the primary language, ensuring typography handles diacritics with elegance.

## Colors

The palette is anchored in a warm, "paper-like" white to reduce the clinical harshness of pure digital displays, paired with high-contrast charcoal and deep botanical greens.

- **Background (#FAFAF8):** The primary canvas. Use this for all page surfaces to establish a premium, editorial feel.
- **Text (#1A1A18):** Dark charcoal for maximum legibility and a softened alternative to pure black. Use for all body text and primary headlines.
- **Accent (#1C3A2A):** Deep Forest Green. Used sparingly for hover states, primary calls to action, or structural emphasis.
- **Detail (#B8922A):** Warm Gold. Reserved strictly for fine details: 0.5px dividers, small-caps labels, or active pagination markers. Use this to signal "premium" quality without overwhelming the layout.

## Typography

Typography is the primary vehicle for the brand’s authority. The system relies on the tension between a high-contrast serif for narrative elements and a neutral, functional sans-serif for data.

- **Headlines:** Use Playfair Display. Headlines should be large and commanding. Ensure "Display" variants are used for anything above 48px to maintain thin stroke elegance.
- **Body:** Inter provides a modern, utilitarian contrast. It should be set with generous line-height to ensure readability in long-form operational reports.
- **Labels:** Use `label-caps` for section headers, overlines, and table headers. The increased letter spacing is critical for the "prestige" look.
- **Language:** Ensure all fonts support Polish character sets (ą, ć, ę, ł, ń, ó, ś, ź, ż).

## Layout & Spacing

The layout philosophy follows a **fixed-grid** model with expansive margins that prioritize content focus over density.

- **The Grid:** A 12-column grid on desktop. Large amounts of whitespace (negative space) should be used to separate core thematic sections.
- **Horizontal Dividers:** Use 0.5px hair-lines in Gold (#B8922A) or lightened Charcoal to separate content blocks. 
- **Vertical Rhythm:** Use `stack-xl` (96px) between major sections to allow the design to "breathe."
- **Data Display:** Tables should span the full width of their container, using generous cell padding (minimum 16px) to maintain an airy, uncrowded feel.

## Elevation & Depth

This design system is strictly **Flat**. Do not use shadows, blurs, or gradients.

- **Depth through Layering:** Depth is achieved solely through the stacking of colors (e.g., a Dark Forest Green button on a Warm White background).
- **Outlines:** Use 1px or 0.5px borders to define interactive areas.
- **Borders:** All decorative lines must be 0.5px. This thinness communicates precision and high-end craftsmanship.
- **Inactivity:** Use a low-opacity charcoal (#1A1A18 at 10%) for disabled states or secondary structural lines.

## Shapes

The shape language is **Sharp and Architectural.** 

- **Corners:** Buttons, inputs, and cards must have 0px corner radius (Sharp). A maximum of 2px is permitted only if required by a specific platform's technical constraints, but 0px is the preferred standard.
- **Photography:** Images must be strictly rectangular with sharp edges. Never use masks or rounded frames. 
- **Icons:** If used, icons must be thin-line (1px stroke) and geometric. Avoid filled or "playful" icons.

## Components

### Buttons
- **Primary:** Dark Forest Green background (#1C3A2A), white text, sharp corners, no border. Padding: 12px 32px.
- **Secondary:** Transparent background, Dark Charcoal border (1px), sharp corners. 
- **Text Link:** Underlined with a 0.5px Gold line, using `label-caps` typography.

### Data Tables
- Header row uses `label-caps` typography.
- Horizontal dividers only (0.5px). No vertical grid lines.
- Row hover state: Subtle background tint (#1C3A2A at 5% opacity).

### Form Inputs
- Bottom-border only (1px charcoal) to mimic traditional paper forms.
- Labels sit above the input in `label-caps` typography.

### Chips & Tags
- Rectangular, 1px charcoal outline, `label-caps` text. No background fill unless active (then use Forest Green).

### Imagery
- **Style:** Black and white only.
- **Subject:** Structural details, architectural textures, or high-contrast, serious monochrome portraits. 
- **Filter:** High contrast, slight film grain, no soft focus.