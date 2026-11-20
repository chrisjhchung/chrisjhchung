# Generates Arkytex avatar variants as SVG.
GRID = "".join(f'<line x1="{i}" y1="0" x2="{i}" y2="1024"/><line x1="0" y1="{i}" x2="1024" y2="{i}"/>' for i in range(0, 1025, 32))

def svg(accent, face, name, chest=True):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="42%" r="70%"><stop offset="0" stop-color="#101a2c"/><stop offset="1" stop-color="#04060b"/></radialGradient>
  <radialGradient id="fade" cx="50%" cy="45%" r="55%"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
  <mask id="gridmask"><rect width="1024" height="1024" fill="url(#fade)"/></mask>
  <linearGradient id="hood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c2638"/><stop offset="1" stop-color="#0b0f18"/></linearGradient>
  <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{accent}" stop-opacity=".75"/><stop offset=".55" stop-color="{accent}" stop-opacity=".08"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></linearGradient>
  <radialGradient id="void" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#000"/><stop offset=".8" stop-color="#020306"/><stop offset="1" stop-color="#0c1220"/></radialGradient>
  <radialGradient id="voidglow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{accent}" stop-opacity=".18"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="soft"><feGaussianBlur stdDeviation="18"/></filter>
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<g stroke="{accent}" stroke-opacity=".10" stroke-width="1.5" mask="url(#gridmask)">{GRID}</g>
<g transform="translate(512,540) scale(1.12) translate(-512,-560)">
<path d="M90 1100 L90 1024 C120 870 290 790 400 770 L624 770 C734 790 904 870 934 1024 L934 1100 Z" fill="#111827"/>
<path d="M90 1024 C120 870 290 790 400 770 L624 770 C734 790 904 870 934 1024" fill="none" stroke="url(#rim)" stroke-width="4"/>
<path d="M512 150 C712 150 800 320 800 520 C800 660 745 770 690 840 C630 815 570 800 512 800 C454 800 394 815 334 840 C279 770 224 660 224 520 C224 320 312 150 512 150 Z" fill="url(#hood)"/>
<path d="M512 150 C712 150 800 320 800 520 C800 660 745 770 690 840 M334 840 C279 770 224 660 224 520 C224 320 312 150 512 150" fill="none" stroke="url(#rim)" stroke-width="5"/>
<path d="M512 285 C628 285 690 392 690 515 C690 622 646 705 512 740 C378 705 334 622 334 515 C334 392 396 285 512 285 Z" fill="url(#void)" stroke="#000" stroke-width="10"/>
<ellipse cx="512" cy="520" rx="150" ry="120" fill="url(#voidglow)"/>
{face}
{chest_logo(accent) if chest else ""}
</g>
</svg>'''

def chest_logo(a):
    # drafting compass forming an "A"
    return f'''<g filter="url(#glow)" stroke="{a}" stroke-width="7" stroke-linecap="round" fill="none">
  <circle cx="512" cy="858" r="10" fill="{a}"/>
  <line x1="512" y1="868" x2="468" y2="955"/><line x1="512" y1="868" x2="556" y2="955"/>
  <path d="M482 925 A 70 70 0 0 0 542 925"/>
</g>'''

def eyes(a):
    return f'''<g filter="url(#glow)" fill="{a}">
  <path d="M420 515 L492 500 L494 516 L424 528 Z"/><path d="M604 515 L532 500 L530 516 L600 528 Z"/>
</g>'''

def prompt(a):
    return f'''<g filter="url(#glow)" fill="{a}" font-family="DejaVu Sans Mono, monospace" font-weight="bold">
  <text x="512" y="560" font-size="120" text-anchor="middle">&gt;_</text>
</g>'''

def visor(a):
    return f'''<g filter="url(#glow)">
  <path d="M372 492 Q512 470 652 492 L646 540 Q512 520 378 540 Z" fill="{a}" fill-opacity=".9"/>
</g>
<g stroke="#000" stroke-opacity=".45" stroke-width="3">{"".join(f'<line x1="370" y1="{y}" x2="655" y2="{y}"/>' for y in range(484, 546, 8))}</g>'''

variants = {
  "arkytex-eyes-cyan": svg("#3ce8ff", eyes("#3ce8ff"), "eyes"),
  "arkytex-prompt-green": svg("#3dff8f", prompt("#3dff8f"), "prompt"),
  "arkytex-visor-magenta": svg("#ff3fd2", visor("#ff3fd2"), "visor"),
}
for k, v in variants.items():
    open(f"{k}.svg", "w").write(v)
print("ok")
