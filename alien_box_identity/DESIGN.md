---
name: Alien Box Identity
colors:
  surface: '#10141a'
  surface-dim: '#10141a'
  surface-bright: '#353940'
  surface-container-lowest: '#0a0e14'
  surface-container-low: '#181c22'
  surface-container: '#1c2026'
  surface-container-high: '#262a31'
  surface-container-highest: '#31353c'
  on-surface: '#dfe2eb'
  on-surface-variant: '#bacbb9'
  inverse-surface: '#dfe2eb'
  inverse-on-surface: '#2d3137'
  outline: '#859585'
  outline-variant: '#3b4a3d'
  surface-tint: '#00e475'
  primary: '#75ff9e'
  on-primary: '#003918'
  primary-container: '#00e676'
  on-primary-container: '#00612e'
  inverse-primary: '#006d35'
  secondary: '#e7b4ff'
  on-secondary: '#500075'
  secondary-container: '#b204ff'
  on-secondary-container: '#fff6fd'
  tertiary: '#a3f1ff'
  on-tertiary: '#00363d'
  tertiary-container: '#00dcf5'
  on-tertiary-container: '#005d68'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#62ff96'
  primary-fixed-dim: '#00e475'
  on-primary-fixed: '#00210b'
  on-primary-fixed-variant: '#005226'
  secondary-fixed: '#f6d9ff'
  secondary-fixed-dim: '#e7b4ff'
  on-secondary-fixed: '#300049'
  on-secondary-fixed-variant: '#7100a4'
  tertiary-fixed: '#9cf0ff'
  tertiary-fixed-dim: '#00daf3'
  on-tertiary-fixed: '#001f24'
  on-tertiary-fixed-variant: '#004f58'
  background: '#10141a'
  on-background: '#dfe2eb'
  surface-variant: '#31353c'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
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
  label-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  container-max-width: 1440px
---

## Brand & Style
The design system embodies the "Alien Box" identity—a high-octane fusion of **Neo-Brutalism** and **Futuristic Sci-Fi**. It is designed to feel like an advanced extraterrestrial interface: raw, powerful, and uncompromising. 

The aesthetic prioritizes high-contrast dark surfaces punctuated by radioactive neons. Visual weight is anchored by heavy, sharp-edged containers that mimic the structural integrity of a "box." The atmosphere is immersive and cinematic, utilizing "glowing" light leaks and sharp technical borders to evoke a sense of advanced technology found in deep space.

## Colors
The palette is centered on **Deep Black (#080C12)** to provide a void-like backdrop, allowing the radioactive accent colors to vibrate. 

- **Verde CHUS (#00E676):** The primary action color, used for success states and critical interactive elements.
- **Púrpura Alien (#B200FF):** The secondary brand color, used for secondary actions and mystical/premium highlights.
- **Azul Neón (#00E5FF):** The technical accent, primarily used for borders, data visualizations, and glowing effects.
- **Functional Grays:** Mid-tones are avoided to maintain high contrast; use low-opacity versions of Azul Neón for subtle dividers.

## Typography
The typographic hierarchy relies on the tension between the technical, geometric nature of **Space Grotesk** and the hyper-legible utility of **Inter**.

- **Headlines:** Use Space Grotesk for all headings. Tighten letter spacing for larger display sizes to create a "blocked" Neo-Brutalist look.
- **Body:** Inter is reserved for long-form content to ensure maximum readability against dark backgrounds.
- **Labels:** Use uppercase Space Grotesk with increased tracking for a "system readout" aesthetic.

## Layout & Spacing
The layout follows a **Fixed Grid** model to reinforce the "Alien Box" concept. Content is housed within rigid, structural modules.

- **Grid:** A 12-column system for desktop with 24px gutters.
- **Modular Blocks:** Use hard-edged containers. Spacing between major sections should be aggressive (80px+) to allow the brand colors to breathe.
- **Padding:** Internal container padding should be generous (min 32px) to maintain a premium, editorial feel within the technical constraints.
- **Mobile:** Reflow to a 4-column grid. Margins shrink to 16px, but container borders remain 1px solid to maintain the sharp aesthetic.

## Elevation & Depth
In this design system, depth is not conveyed through soft shadows, but through **Tonal Layering** and **Luminescence**.

- **Surfaces:** Use `#111821` for elevated cards against the `#080C12` background.
- **Glows:** Instead of drop shadows, use `box-shadow` with 0px blur and a spread of Azul Neón for "hard" elevation, or a diffused `drop-shadow` in Púrpura Alien for "active" glowing states.
- **Outlines:** Elevation levels are primarily defined by 1px solid borders. Higher priority elements use the Azul Neón border, while secondary elements use a muted 20% opacity white.

## Shapes
The shape language is strictly **Sharp (0px roundedness)**. 

To honor the "Box" identity and the reference logo, every interactive element—from buttons to input fields—must feature 90-degree angles. This reinforces the Neo-Brutalist influence and ensures the UI feels like a constructed technical object. The only exception is the use of circular "indicator" lights or specific brand iconography.

## Components
- **Buttons:** Rectangular with 1px solid borders. Primary buttons use a solid Verde CHUS background with black text. Secondary buttons use a black background with Azul Neón borders and text.
- **Glowing States:** On hover, buttons and cards should trigger an outer glow (`box-shadow: 0 0 15px`) using the component's accent color.
- **Inputs:** Dark background (#080C12) with a 1px Azul Neón border. Labels should appear above the input in uppercase Space Grotesk.
- **Chips:** Small, sharp-edged tags with a subtle Púrpura Alien border and 10% opacity fill.
- **Cards:** Use a 1px solid #00E5FF border. For a "header" effect, place a solid bar of color (Verde CHUS) at the top of the card, mimicking the bars in the CHUS BZN logo.
- **Progress Bars:** Use a stepped, "pixelated" look rather than a smooth fill to enhance the Sci-Fi computer interface feel.