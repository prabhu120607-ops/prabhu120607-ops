"""
Profile SVG Generator for Prabhu Angothu (prabhu120607-ops)
Generates:
  - assets/hero.svg
  - assets/about-life.svg
  - assets/stack.svg
  - assets/id-dashboard.svg
  - assets/connect.svg
All SVGs are fully self-contained with base64 embedded WOFF2 fonts and high-DPI transparent PNGs.
"""

import json, base64, io, os
from PIL import Image

# 1. Load assets
with open('assets/fonts.json', 'r') as f:
    fonts = json.load(f)

with open('assets/simple_icons.json', 'r') as f:
    icons = json.load(f)

# Helper to optimize & base64 encode PNG
def get_image_b64(path, max_w=900):
    im = Image.open(path)
    if im.width > max_w:
        ratio = max_w / im.width
        im = im.resize((max_w, int(im.height * ratio)), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

id_b64 = get_image_b64('assets/id.png', max_w=900)
conn_b64 = get_image_b64('assets/right_pointing.png', max_w=900)

font_outfit_800 = fonts['Outfit_800']['b64']
font_outfit_600 = fonts['Outfit_600']['b64']
font_mono_500 = fonts['JetBrains Mono_500']['b64']
font_mono_700 = fonts['JetBrains Mono_700']['b64']

def get_font_faces():
    return f"""
    @font-face {{
      font-family: 'Outfit';
      font-style: normal;
      font-weight: 800;
      font-display: swap;
      src: url(data:font/woff2;charset=utf-8;base64,{font_outfit_800}) format('woff2');
    }}
    @font-face {{
      font-family: 'Outfit';
      font-style: normal;
      font-weight: 600;
      font-display: swap;
      src: url(data:font/woff2;charset=utf-8;base64,{font_outfit_600}) format('woff2');
    }}
    @font-face {{
      font-family: 'JetBrains Mono';
      font-style: normal;
      font-weight: 500;
      font-display: swap;
      src: url(data:font/woff2;charset=utf-8;base64,{font_mono_500}) format('woff2');
    }}
    @font-face {{
      font-family: 'JetBrains Mono';
      font-style: normal;
      font-weight: 700;
      font-display: swap;
      src: url(data:font/woff2;charset=utf-8;base64,{font_mono_700}) format('woff2');
    }}
    """

# ==============================================================================
# 1. HERO.SVG
# ==============================================================================
def build_hero():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 880 340" fill="none">
  <!--
    PRABHU ANGOTHU - HERO BANNER
    Fonts: Outfit (OFL 1.1), JetBrains Mono (OFL 1.1)
    Color Palette: Deep Navy #070b16, Electric Blue #247bff, Crimson #ff354f, Off-White #f0f4fc
  -->
  <defs>
    <style>
      {get_font_faces()}
      
      .p-hero-root {{
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
      .p-hero-mono {{
        font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
      }}
      
      /* Blinking cursor */
      @keyframes p-hero-blink {{
        0%, 49% {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}
      .p-hero-cursor {{
        animation: p-hero-blink 1.0s infinite;
      }}
      
      /* Rising Name Reveal with Fallback */
      @keyframes p-hero-name-rise {{
        0% {{ transform: translateY(65px); opacity: 0; }}
        100% {{ transform: translateY(0); opacity: 1; }}
      }}
      .p-hero-name-group {{
        animation: p-hero-name-rise 0.9s cubic-bezier(0.16, 1, 0.3, 1) both;
      }}
      
      /* 4 Cycling Roles (12s infinite loop: 3s per role) */
      @keyframes p-hero-role1 {{
        0% {{ opacity: 0; transform: translateY(14px); }}
        4%, 22% {{ opacity: 1; transform: translateY(0); }}
        25%, 100% {{ opacity: 0; transform: translateY(-14px); }}
      }}
      @keyframes p-hero-role2 {{
        0%, 25% {{ opacity: 0; transform: translateY(14px); }}
        29%, 47% {{ opacity: 1; transform: translateY(0); }}
        50%, 100% {{ opacity: 0; transform: translateY(-14px); }}
      }}
      @keyframes p-hero-role3 {{
        0%, 50% {{ opacity: 0; transform: translateY(14px); }}
        54%, 72% {{ opacity: 1; transform: translateY(0); }}
        75%, 100% {{ opacity: 0; transform: translateY(-14px); }}
      }}
      @keyframes p-hero-role4 {{
        0%, 75% {{ opacity: 0; transform: translateY(14px); }}
        79%, 97% {{ opacity: 1; transform: translateY(0); }}
        100% {{ opacity: 0; transform: translateY(-14px); }}
      }}
      
      .p-hero-r1 {{ animation: p-hero-role1 12s infinite ease-in-out; }}
      .p-hero-r2 {{ animation: p-hero-role2 12s infinite ease-in-out; }}
      .p-hero-r3 {{ animation: p-hero-role3 12s infinite ease-in-out; }}
      .p-hero-r4 {{ animation: p-hero-role4 12s infinite ease-in-out; }}
      
      /* Ambient Glow Pulse */
      @keyframes p-hero-pulse {{
        0%, 100% {{ opacity: 0.55; transform: scale(1); }}
        50% {{ opacity: 0.85; transform: scale(1.05); }}
      }}
      .p-hero-glow {{
        animation: p-hero-pulse 6s ease-in-out infinite;
        transform-origin: 720px 170px;
      }}
      
      /* Reduced Motion Accessibility */
      @media (prefers-reduced-motion: reduce) {{
        .p-hero-name-group {{ animation: none; transform: translateY(0); opacity: 1; }}
        .p-hero-cursor {{ animation: none; opacity: 1; }}
        .p-hero-glow {{ animation: none; opacity: 0.6; }}
        .p-hero-r1 {{ animation: none; opacity: 1; transform: none; }}
        .p-hero-r2, .p-hero-r3, .p-hero-r4 {{ display: none; }}
      }}
    </style>
    
    <!-- Background Gradients & Dot Grid -->
    <linearGradient id="p-hero-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b16"/>
      <stop offset="60%" stop-color="#0a1022"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>
    
    <linearGradient id="p-hero-border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="30%" stop-color="#247bff" stop-opacity="0.2"/>
      <stop offset="70%" stop-color="#ff354f" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="p-hero-text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#f0f4fc"/>
      <stop offset="100%" stop-color="#247bff"/>
    </linearGradient>
    
    <radialGradient id="p-hero-blue-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.32"/>
      <stop offset="50%" stop-color="#247bff" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="p-hero-crimson-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.24"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </radialGradient>
    
    <pattern id="p-hero-dotgrid" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#247bff" fill-opacity="0.13"/>
    </pattern>
    
    <!-- Rising Mask for Name Reveal -->
    <clipPath id="p-hero-name-mask">
      <rect x="0" y="0" width="560" height="65"/>
    </clipPath>

    <clipPath id="p-hero-portrait-clip">
      <rect x="585" y="25" width="265" height="290" rx="18"/>
    </clipPath>
  </defs>

  <!-- Canvas Base -->
  <rect width="880" height="340" rx="20" fill="url(#p-hero-bg-grad)"/>
  <rect width="880" height="340" rx="20" fill="url(#p-hero-dotgrid)"/>
  
  <!-- Ambient Atmospheric Glows -->
  <circle cx="720" cy="170" r="190" fill="url(#p-hero-blue-glow)" class="p-hero-glow"/>
  <circle cx="600" cy="90" r="150" fill="url(#p-hero-crimson-glow)" class="p-hero-glow"/>
  <circle cx="120" cy="80" r="130" fill="url(#p-hero-blue-glow)" opacity="0.4"/>
  
  <!-- Outer Hairline Border -->
  <rect x="0.75" y="0.75" width="878.5" height="338.5" rx="19.25" fill="none" stroke="url(#p-hero-border-grad)" stroke-width="1.5"/>

  <!-- ================= LEFT CONTENT AREA ================= -->
  <g class="p-hero-root">
    
    <!-- 1. Typed Greeting Line -->
    <g transform="translate(48, 52)">
      <rect x="0" y="-12" width="12" height="12" rx="3" fill="#247bff" fill-opacity="0.2"/>
      <path d="M3 -6 L7 -6 M5 -8 L5 -4" stroke="#247bff" stroke-width="1.5" stroke-linecap="round"/>
      <text x="22" y="-1" fill="#247bff" class="p-hero-mono" font-size="12" font-weight="700" letter-spacing="1.5">INIT &gt; HELLO, WORLD! I AM</text>
      <!-- Blinking Terminal Cursor -->
      <rect x="238" y="-12" width="7" height="14" fill="#247bff" class="p-hero-cursor" rx="1.5"/>
    </g>

    <!-- 2. Large Rising-Mask Name Reveal -->
    <g transform="translate(48, 68)">
      <g clip-path="url(#p-hero-name-mask)">
        <g class="p-hero-name-group">
          <text x="0" y="50" font-size="44" font-weight="800" letter-spacing="-0.5" fill="url(#p-hero-text-grad)">PRABHU ANGOTHU</text>
        </g>
      </g>
    </g>

    <!-- 3. Four Cycling Roles -->
    <g transform="translate(48, 142)">
      <!-- Role Badge Container -->
      <rect x="0" y="0" width="375" height="34" rx="10" fill="#0d172e" stroke="#247bff" stroke-width="1" stroke-opacity="0.4"/>
      <circle cx="16" cy="17" r="4" fill="#ff354f"/>
      <text x="28" y="21" class="p-hero-mono" font-size="10.5" font-weight="700" fill="#7d92b5" letter-spacing="1">SPECIALTY // </text>
      
      <!-- Role 1: Web Developer -->
      <g class="p-hero-r1">
        <text x="122" y="21" class="p-hero-mono" font-size="11.5" font-weight="700" fill="#f0f4fc">Web Developer</text>
      </g>
      <!-- Role 2: Frontend Developer -->
      <g class="p-hero-r2">
        <text x="122" y="21" class="p-hero-mono" font-size="11.5" font-weight="700" fill="#247bff">Frontend Developer</text>
      </g>
      <!-- Role 3: AI Project Builder -->
      <g class="p-hero-r3">
        <text x="122" y="21" class="p-hero-mono" font-size="11.5" font-weight="700" fill="#ff354f">AI Project Builder</text>
      </g>
      <!-- Role 4: Software Development Learner -->
      <g class="p-hero-r4">
        <text x="122" y="21" class="p-hero-mono" font-size="11.5" font-weight="700" fill="#38ef7d">Software Dev Learner</text>
      </g>
    </g>

    <!-- 4. One-Line Pitch -->
    <g transform="translate(48, 202)">
      <text x="0" y="0" font-size="14.2" font-weight="600" fill="#c3cfe4" letter-spacing="0.1">
        <tspan x="0" dy="0">Aspiring web developer passionate about building practical web</tspan>
        <tspan x="0" dy="21">applications and AI-powered solutions that solve real-world problems.</tspan>
      </text>
    </g>

    <!-- 5. Location / Company / GitHub Metadata Row -->
    <g transform="translate(48, 268)">
      <!-- Location Pill -->
      <rect x="0" y="0" width="85" height="28" rx="8" fill="#0d172e" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.3"/>
      <text x="12" y="18" font-size="12">📍</text>
      <text x="32" y="18" class="p-hero-mono" font-size="11" font-weight="500" fill="#e2e8f0">India</text>

      <!-- Role / Company Pill -->
      <rect x="95" y="0" width="220" height="28" rx="8" fill="#0d172e" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.3"/>
      <text x="107" y="18" font-size="12">💼</text>
      <text x="127" y="18" class="p-hero-mono" font-size="11" font-weight="500" fill="#e2e8f0">Student • Independent Dev</text>

      <!-- GitHub Pill -->
      <rect x="325" y="0" width="168" height="28" rx="8" fill="#0d172e" stroke="#ff354f" stroke-width="0.8" stroke-opacity="0.4"/>
      <g transform="translate(337, 7) scale(0.6)">
        <path d="{icons['github']}" fill="#f0f4fc"/>
      </g>
      <text x="357" y="18" class="p-hero-mono" font-size="11" font-weight="500" fill="#f0f4fc">prabhu120607-ops</text>
    </g>
  </g>

  <!-- ================= RIGHT PORTRAIT AREA ================= -->
  <g>
    <!-- Card Frame Backdrop -->
    <rect x="585" y="25" width="265" height="290" rx="18" fill="#090f1f" stroke="url(#p-hero-border-grad)" stroke-width="1.4"/>
    
    <!-- Corner Tech HUD Accents -->
    <path d="M593 40 L593 33 L600 33" stroke="#247bff" stroke-width="2" fill="none"/>
    <path d="M842 40 L842 33 L835 33" stroke="#247bff" stroke-width="2" fill="none"/>
    <path d="M593 295 L593 302 L600 302" stroke="#ff354f" stroke-width="2" fill="none"/>
    <path d="M842 295 L842 302 L835 302" stroke="#ff354f" stroke-width="2" fill="none"/>

    <!-- Subtle Diagonal Pattern Behind Portrait -->
    <g clip-path="url(#p-hero-portrait-clip)">
      <circle cx="717" cy="160" r="110" fill="url(#p-hero-blue-glow)" opacity="0.6"/>
      
      <!-- Inlined High-DPI Portrait (Preserving Exact Alpha & Head/Chest Framing) -->
      <!-- BBox in 1584x993 image: x=[190, 1451], y=[16, 992]. Centered nicely -->
      <image href="data:image/png;base64,{id_b64}" x="532" y="25" width="370" height="290" preserveAspectRatio="xMidYMid meet"/>
      
      <!-- Subtle Bottom Dark Vignette so status pill sits cleanly -->
      <rect x="585" y="250" width="265" height="65" fill="url(#p-hero-vignette)"/>
    </g>
    
    <!-- Gradient for vignette -->
    <linearGradient id="p-hero-vignette" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#070b16" stop-opacity="0"/>
      <stop offset="100%" stop-color="#070b16" stop-opacity="0.9"/>
    </linearGradient>

    <!-- Verified Live Status Tag -->
    <g transform="translate(642, 282)">
      <rect x="0" y="0" width="152" height="24" rx="12" fill="#070c18" stroke="#247bff" stroke-width="1" stroke-opacity="0.6"/>
      <circle cx="12" cy="12" r="3.5" fill="#38ef7d"/>
      <circle cx="12" cy="12" r="6" fill="#38ef7d" fill-opacity="0.3"/>
      <text x="24" y="16" class="p-hero-mono" font-size="9.5" font-weight="700" fill="#f0f4fc" letter-spacing="0.8">ACTIVE DEVELOPER</text>
    </g>
  </g>
</svg>"""

# ==============================================================================
# 2. ABOUT-LIFE.SVG
# ==============================================================================
def build_about_life():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 880 340" fill="none">
  <!--
    PRABHU ANGOTHU - CAPABILITIES & INTERESTS CAROUSEL
    Three-slide interests carousel changing every 4 seconds with segment progress bars.
    Fonts: Outfit, JetBrains Mono
  -->
  <defs>
    <style>
      {get_font_faces()}
      
      .p-abt-root {{
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
      .p-abt-mono {{
        font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
      }}
      
      /* Carousel Slides: 12s total cycle (Slide 1: 0-4s, Slide 2: 4-8s, Slide 3: 8-12s) */
      @keyframes p-abt-slide1 {{
        0% {{ opacity: 0; transform: translateX(20px); }}
        3%, 30% {{ opacity: 1; transform: translateX(0); }}
        33.3%, 100% {{ opacity: 0; transform: translateX(-20px); }}
      }}
      @keyframes p-abt-slide2 {{
        0%, 33.3% {{ opacity: 0; transform: translateX(20px); }}
        36.3%, 63.3% {{ opacity: 1; transform: translateX(0); }}
        66.6%, 100% {{ opacity: 0; transform: translateX(-20px); }}
      }}
      @keyframes p-abt-slide3 {{
        0%, 66.6% {{ opacity: 0; transform: translateX(20px); }}
        69.6%, 96.6% {{ opacity: 1; transform: translateX(0); }}
        100% {{ opacity: 0; transform: translateX(-20px); }}
      }}
      
      .p-abt-s1 {{ animation: p-abt-slide1 12s infinite ease-in-out; }}
      .p-abt-s2 {{ animation: p-abt-slide2 12s infinite ease-in-out; }}
      .p-abt-s3 {{ animation: p-abt-slide3 12s infinite ease-in-out; }}
      
      /* Progress Bar Animations (Segment 1, 2, 3) */
      @keyframes p-abt-prog1 {{
        0% {{ width: 0px; }}
        33.3% {{ width: 112px; }}
        99.9% {{ width: 112px; }}
        100% {{ width: 0px; }}
      }}
      @keyframes p-abt-prog2 {{
        0%, 33.3% {{ width: 0px; }}
        66.6% {{ width: 112px; }}
        99.9% {{ width: 112px; }}
        100% {{ width: 0px; }}
      }}
      @keyframes p-abt-prog3 {{
        0%, 66.6% {{ width: 0px; }}
        100% {{ width: 112px; }}
      }}
      
      .p-abt-bar1 {{ animation: p-abt-prog1 12s infinite linear; }}
      .p-abt-bar2 {{ animation: p-abt-prog2 12s infinite linear; }}
      .p-abt-bar3 {{ animation: p-abt-prog3 12s infinite linear; }}
      
      /* Card Hover / Micro Glows */
      .p-abt-cap-card {{
        transition: transform 0.2s ease;
      }}
      
      @media (prefers-reduced-motion: reduce) {{
        .p-abt-s1 {{ animation: none; opacity: 1; transform: none; }}
        .p-abt-s2, .p-abt-s3 {{ display: none; }}
        .p-abt-bar1 {{ animation: none; width: 112px; }}
        .p-abt-bar2, .p-abt-bar3 {{ animation: none; width: 0px; }}
      }}
    </style>
    
    <linearGradient id="p-abt-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b16"/>
      <stop offset="50%" stop-color="#091022"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>

    <linearGradient id="p-abt-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.7"/>
      <stop offset="50%" stop-color="#247bff" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.7"/>
    </linearGradient>

    <linearGradient id="p-abt-card-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0d172e"/>
      <stop offset="100%" stop-color="#0a1224"/>
    </linearGradient>
    
    <pattern id="p-abt-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#247bff" fill-opacity="0.12"/>
    </pattern>

    <clipPath id="p-abt-carousel-clip">
      <rect x="455" y="70" width="395" height="235" rx="14"/>
    </clipPath>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="340" rx="20" fill="url(#p-abt-bg)"/>
  <rect width="880" height="340" rx="20" fill="url(#p-abt-dots)"/>
  <rect x="0.75" y="0.75" width="878.5" height="338.5" rx="19.25" fill="none" stroke="url(#p-abt-border)" stroke-width="1.5"/>

  <!-- ================= LEFT COLUMN: CAPABILITIES ================= -->
  <g class="p-abt-root" transform="translate(30, 25)">
    <!-- Header -->
    <text x="0" y="16" class="p-abt-mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.5">// CORE ENGINEERING</text>
    <text x="0" y="42" font-size="22" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Technical Capabilities</text>

    <!-- Capability 1: Full-Stack Web -->
    <g transform="translate(0, 58)" class="p-abt-cap-card">
      <rect width="390" height="52" rx="10" fill="url(#p-abt-card-grad)" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.3"/>
      <circle cx="26" cy="26" r="14" fill="#247bff" fill-opacity="0.15"/>
      <text x="20" y="30" font-size="13">🌐</text>
      <text x="48" y="22" font-size="13.5" font-weight="700" fill="#f0f4fc">Full-Stack Web Development</text>
      <text x="48" y="39" class="p-abt-mono" font-size="10.5" fill="#8ea2c2">HTML5 • CSS3 • JavaScript (ES6+) • PHP • MySQL</text>
    </g>

    <!-- Capability 2: AI & Intelligent Systems -->
    <g transform="translate(0, 118)" class="p-abt-cap-card">
      <rect width="390" height="52" rx="10" fill="url(#p-abt-card-grad)" stroke="#ff354f" stroke-width="0.8" stroke-opacity="0.3"/>
      <circle cx="26" cy="26" r="14" fill="#ff354f" fill-opacity="0.15"/>
      <text x="20" y="30" font-size="13">🤖</text>
      <text x="48" y="22" font-size="13.5" font-weight="700" fill="#f0f4fc">AI &amp; Intelligent Applications</text>
      <text x="48" y="39" class="p-abt-mono" font-size="10.5" fill="#8ea2c2">Python • Streamlit • LLM Integration • Automation</text>
    </g>

    <!-- Capability 3: Modern UI/UX -->
    <g transform="translate(0, 178)" class="p-abt-cap-card">
      <rect width="390" height="52" rx="10" fill="url(#p-abt-card-grad)" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.3"/>
      <circle cx="26" cy="26" r="14" fill="#247bff" fill-opacity="0.15"/>
      <text x="20" y="30" font-size="13">🎨</text>
      <text x="48" y="22" font-size="13.5" font-weight="700" fill="#f0f4fc">Modern Responsive UI/UX</text>
      <text x="48" y="39" class="p-abt-mono" font-size="10.5" fill="#8ea2c2">Component Architecture • Micro-Interactions • SVG</text>
    </g>

    <!-- Capability 4: Core CS & Algorithms -->
    <g transform="translate(0, 238)" class="p-abt-cap-card">
      <rect width="390" height="52" rx="10" fill="url(#p-abt-card-grad)" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.3"/>
      <circle cx="26" cy="26" r="14" fill="#247bff" fill-opacity="0.15"/>
      <text x="20" y="30" font-size="13">⚡</text>
      <text x="48" y="22" font-size="13.5" font-weight="700" fill="#f0f4fc">Data Structures &amp; Algorithms</text>
      <text x="48" y="39" class="p-abt-mono" font-size="10.5" fill="#8ea2c2">Java • Analytical Problem Solving • Optimization</text>
    </g>
  </g>

  <!-- Divider Line -->
  <line x1="440" y1="35" x2="440" y2="305" stroke="#247bff" stroke-opacity="0.15" stroke-dasharray="4 4"/>

  <!-- ================= RIGHT COLUMN: INTERESTS CAROUSEL ================= -->
  <g class="p-abt-root" transform="translate(460, 25)">
    <!-- Header with 4s Carousel Indicator -->
    <text x="0" y="16" class="p-abt-mono" font-size="11" font-weight="700" fill="#ff354f" letter-spacing="1.5">// INTERESTS CAROUSEL</text>
    
    <!-- 3 Segment Progress Bars (Changing every 4 seconds) -->
    <g transform="translate(0, 30)">
      <!-- Segment 1 Track & Fill -->
      <rect x="0" y="0" width="112" height="4" rx="2" fill="#15213b"/>
      <rect x="0" y="0" width="0" height="4" rx="2" fill="#247bff" class="p-abt-bar1"/>
      
      <!-- Segment 2 Track & Fill -->
      <rect x="122" y="0" width="112" height="4" rx="2" fill="#15213b"/>
      <rect x="122" y="0" width="0" height="4" rx="2" fill="#ff354f" class="p-abt-bar2"/>

      <!-- Segment 3 Track & Fill -->
      <rect x="244" y="0" width="112" height="4" rx="2" fill="#15213b"/>
      <rect x="244" y="0" width="0" height="4" rx="2" fill="#247bff" class="p-abt-bar3"/>
      
      <!-- 4s Timer Badge -->
      <text x="365" y="6" class="p-abt-mono" font-size="9" fill="#7588a8">4s</text>
    </g>

    <!-- Carousel Content Box -->
    <g transform="translate(0, 48)">
      <rect width="390" height="235" rx="14" fill="#0b1326" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.35"/>
      
      <!-- SLIDE 1: Learning New Technologies -->
      <g class="p-abt-s1">
        <g transform="translate(24, 28)">
          <rect x="0" y="0" width="150" height="22" rx="6" fill="#247bff" fill-opacity="0.15"/>
          <text x="10" y="15" class="p-abt-mono" font-size="10" font-weight="700" fill="#247bff">01 / EXPANDING HORIZONS</text>
          
          <text x="0" y="48" font-size="20" font-weight="800" fill="#ffffff">Learning New Technologies</text>
          
          <text x="0" y="76" font-size="13.5" fill="#a4b6d4" font-weight="500">
            <tspan x="0" dy="0">Constantly driven by curiosity to explore modern web</tspan>
            <tspan x="0" dy="21">standards, developer tools, and practical AI frameworks.</tspan>
            <tspan x="0" dy="21">Turning new technical discoveries into working solutions.</tspan>
          </text>
          
          <!-- Tags -->
          <g transform="translate(0, 138)">
            <rect x="0" y="0" width="92" height="24" rx="6" fill="#13203c" stroke="#247bff" stroke-width="0.7" stroke-opacity="0.4"/>
            <text x="10" y="16" class="p-abt-mono" font-size="10" fill="#f0f4fc">Continuous</text>

            <rect x="100" y="0" width="110" height="24" rx="6" fill="#13203c" stroke="#247bff" stroke-width="0.7" stroke-opacity="0.4"/>
            <text x="110" y="16" class="p-abt-mono" font-size="10" fill="#f0f4fc">Modern Tools</text>

            <rect x="218" y="0" width="85" height="24" rx="6" fill="#13203c" stroke="#247bff" stroke-width="0.7" stroke-opacity="0.4"/>
            <text x="228" y="16" class="p-abt-mono" font-size="10" fill="#f0f4fc">Innovation</text>
          </g>
        </g>
      </g>

      <!-- SLIDE 2: Building Practical Projects -->
      <g class="p-abt-s2">
        <g transform="translate(24, 28)">
          <rect x="0" y="0" width="145" height="22" rx="6" fill="#ff354f" fill-opacity="0.15"/>
          <text x="10" y="15" class="p-abt-mono" font-size="10" font-weight="700" fill="#ff354f">02 / ACTIVE CREATION</text>
          
          <text x="0" y="48" font-size="20" font-weight="800" fill="#ffffff">Building Practical Projects</text>
          
          <text x="0" y="76" font-size="13.5" fill="#a4b6d4" font-weight="500">
            <tspan x="0" dy="0">Engineering real-world applications with high utility.</tspan>
            <tspan x="0" dy="21">From PathSetu (AI career roadmaps) to EventPulse</tspan>
            <tspan x="0" dy="21">(feedback automation) and interactive portfolios.</tspan>
          </text>
          
          <!-- Tags -->
          <g transform="translate(0, 138)">
            <rect x="0" y="0" width="82" height="24" rx="6" fill="#13203c" stroke="#ff354f" stroke-width="0.7" stroke-opacity="0.4"/>
            <text x="10" y="16" class="p-abt-mono" font-size="10" fill="#ff7588">PathSetu</text>

            <rect x="90" y="0" width="94" height="24" rx="6" fill="#13203c" stroke="#ff354f" stroke-width="0.7" stroke-opacity="0.4"/>
            <text x="100" y="16" class="p-abt-mono" font-size="10" fill="#ff7588">EventPulse</text>

            <rect x="192" y="0" width="92" height="24" rx="6" fill="#13203c" stroke="#ff354f" stroke-width="0.7" stroke-opacity="0.4"/>
            <text x="202" y="16" class="p-abt-mono" font-size="10" fill="#ff7588">Production</text>
          </g>
        </g>
      </g>

      <!-- SLIDE 3: Solving DSA Problems -->
      <g class="p-abt-s3">
        <g transform="translate(24, 28)">
          <rect x="0" y="0" width="158" height="22" rx="6" fill="#38ef7d" fill-opacity="0.15"/>
          <text x="10" y="15" class="p-abt-mono" font-size="10" font-weight="700" fill="#38ef7d">03 / ANALYTICAL FOUNDATIONS</text>
          
          <text x="0" y="48" font-size="20" font-weight="800" fill="#ffffff">Solving DSA Problems</text>
          
          <text x="0" y="76" font-size="13.5" fill="#a4b6d4" font-weight="500">
            <tspan x="0" dy="0">Strengthening problem-solving depth and analytical logic</tspan>
            <tspan x="0" dy="21">using Java. Mastering algorithmic complexity, data structures,</tspan>
            <tspan x="0" dy="21">and clean, efficient software implementation.</tspan>
          </text>
          
          <!-- Tags -->
          <g transform="translate(0, 138)">
            <rect x="0" y="0" width="60" height="24" rx="6" fill="#13203c" stroke="#38ef7d" stroke-width="0.7" stroke-opacity="0.4"/>
            <text x="10" y="16" class="p-abt-mono" font-size="10" fill="#88f5b2">Java</text>

            <rect x="68" y="0" width="90" height="24" rx="6" fill="#13203c" stroke="#38ef7d" stroke-width="0.7" stroke-opacity="0.4"/>
            <text x="78" y="16" class="p-abt-mono" font-size="10" fill="#88f5b2">Algorithms</text>

            <rect x="166" y="0" width="125" height="24" rx="6" fill="#13203c" stroke="#38ef7d" stroke-width="0.7" stroke-opacity="0.4"/>
            <text x="176" y="16" class="p-abt-mono" font-size="10" fill="#88f5b2">Data Structures</text>
          </g>
        </g>
      </g>
    </g>
  </g>
</svg>"""

# ==============================================================================
# 3. STACK.SVG
# ==============================================================================
def build_stack():
    # Orbit nodes coordinates: 3 tilted ellipses centered at (440, 140)
    # Tilted angle: -14 deg
    # Center hub: 440, 140
    # Orbit 1 (Inner): rx=160, ry=55 (HTML5, CSS3, JavaScript)
    # Orbit 2 (Middle): rx=245, ry=82 (PHP, MySQL, Java, Git)
    # Orbit 3 (Outer): rx=335, ry=110 (Python, Streamlit, GitHub, Vercel)
    
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 880 430" fill="none">
  <!--
    PRABHU ANGOTHU - TECH STACK ON 3 TILTED ELLIPTICAL ORBITS & GROUPED CHIPS
    Fonts: Outfit, JetBrains Mono
    Simple Icons Official Vectors
  -->
  <defs>
    <style>
      {get_font_faces()}
      
      .p-stk-root {{
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
      .p-stk-mono {{
        font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
      }}
      
      /* Harmonic orbit floating breathing animations */
      @keyframes p-stk-float1 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(0, -6px); }}
      }}
      @keyframes p-stk-float2 {{
        0%, 100% {{ transform: translate(0, 0); }}
        50% {{ transform: translate(0, 6px); }}
      }}
      @keyframes p-stk-pulse-hub {{
        0%, 100% {{ r: 32px; opacity: 0.8; }}
        50% {{ r: 36px; opacity: 1; }}
      }}
      
      .p-stk-n1 {{ animation: p-stk-float1 4.5s ease-in-out infinite; }}
      .p-stk-n2 {{ animation: p-stk-float2 5.0s ease-in-out infinite; }}
      .p-stk-n3 {{ animation: p-stk-float1 5.5s ease-in-out infinite; }}
      
      /* Chip hover transitions */
      .p-stk-chip {{
        transition: transform 0.2s ease;
      }}
      
      @media (prefers-reduced-motion: reduce) {{
        .p-stk-n1, .p-stk-n2, .p-stk-n3 {{ animation: none; }}
      }}
    </style>
    
    <linearGradient id="p-stk-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b16"/>
      <stop offset="50%" stop-color="#091024"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>

    <linearGradient id="p-stk-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#247bff" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="p-stk-hub-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff"/>
      <stop offset="100%" stop-color="#ff354f"/>
    </linearGradient>
    
    <radialGradient id="p-stk-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.35"/>
      <stop offset="60%" stop-color="#247bff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>
    
    <pattern id="p-stk-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#247bff" fill-opacity="0.12"/>
    </pattern>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="430" rx="20" fill="url(#p-stk-bg)"/>
  <rect width="880" height="430" rx="20" fill="url(#p-stk-dots)"/>
  <rect x="0.75" y="0.75" width="878.5" height="428.5" rx="19.25" fill="none" stroke="url(#p-stk-border)" stroke-width="1.5"/>

  <!-- Atmospheric Glow at Center -->
  <circle cx="440" cy="140" r="180" fill="url(#p-stk-glow)"/>

  <!-- Header Title -->
  <g class="p-stk-root" transform="translate(48, 38)">
    <text x="0" y="0" class="p-stk-mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.5">// TECHNICAL ARSENAL</text>
    <text x="0" y="24" font-size="22" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Interactive Planetary Orbits &amp; Stack</text>
  </g>

  <!-- ================= 3 TILTED ELLIPTICAL ORBITS ================= -->
  <!-- Center: (440, 140), Tilt: -14 degrees -->
  <g transform="translate(440, 140)">
    
    <!-- Tilted Orbit Lines -->
    <g transform="rotate(-14)">
      <!-- Orbit 1: Inner (rx=160, ry=55) -->
      <ellipse cx="0" cy="0" rx="160" ry="55" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.35" stroke-dasharray="4 6"/>
      <!-- Orbit 2: Middle (rx=245, ry=82) -->
      <ellipse cx="0" cy="0" rx="245" ry="82" fill="none" stroke="#247bff" stroke-width="1.2" stroke-opacity="0.25" stroke-dasharray="6 8"/>
      <!-- Orbit 3: Outer (rx=335, ry=110) -->
      <ellipse cx="0" cy="0" rx="335" ry="110" fill="none" stroke="#ff354f" stroke-width="1.2" stroke-opacity="0.25" stroke-dasharray="8 10"/>
    </g>

    <!-- Center Hub -->
    <circle cx="0" cy="0" r="32" fill="#0c1429" stroke="url(#p-stk-hub-grad)" stroke-width="2"/>
    <circle cx="0" cy="0" r="24" fill="#247bff" fill-opacity="0.15"/>
    <text x="0" y="-4" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#247bff" text-anchor="middle" letter-spacing="1">PRABHU</text>
    <text x="0" y="8" class="p-stk-mono" font-size="9" font-weight="700" fill="#ffffff" text-anchor="middle" letter-spacing="1">STACK</text>
    <text x="0" y="19" class="p-stk-mono" font-size="7" fill="#ff354f" text-anchor="middle">CORE</text>

    <!-- ===== ORBIT 1 NODES: HTML5, CSS3, JavaScript ===== -->
    <!-- Node 1: HTML5 (tilted ellipse: angle ~ 150 deg -> x=-135, y=-22) -->
    <g transform="translate(-142, -26)" class="p-stk-n1">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#E34F26" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['html5']}" fill="#E34F26"/>
      </g>
      <rect x="-24" y="20" width="48" height="16" rx="4" fill="#070c18" stroke="#E34F26" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">HTML5</text>
    </g>

    <!-- Node 2: JavaScript (angle ~ -30 deg -> x=138, y=-26) -->
    <g transform="translate(138, -26)" class="p-stk-n2">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#F7DF1E" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['javascript']}" fill="#F7DF1E"/>
      </g>
      <rect x="-30" y="20" width="60" height="16" rx="4" fill="#070c18" stroke="#F7DF1E" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">JavaScript</text>
    </g>

    <!-- Node 3: CSS3 (angle ~ 80 deg -> x=10, y=52) -->
    <g transform="translate(15, 52)" class="p-stk-n3">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#1572B6" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['css3']}" fill="#1572B6"/>
      </g>
      <rect x="-22" y="20" width="44" height="16" rx="4" fill="#070c18" stroke="#1572B6" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">CSS3</text>
    </g>

    <!-- ===== ORBIT 2 NODES: PHP, MySQL, Java, Git ===== -->
    <!-- Node 4: PHP (x=-230, y=-38) -->
    <g transform="translate(-230, -38)" class="p-stk-n2">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#777BB4" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['php']}" fill="#777BB4"/>
      </g>
      <rect x="-20" y="20" width="40" height="16" rx="4" fill="#070c18" stroke="#777BB4" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">PHP</text>
    </g>

    <!-- Node 5: MySQL (x=230, y=-42) -->
    <g transform="translate(230, -42)" class="p-stk-n1">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#4479A1" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['mysql']}" fill="#4479A1"/>
      </g>
      <rect x="-24" y="20" width="48" height="16" rx="4" fill="#070c18" stroke="#4479A1" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">MySQL</text>
    </g>

    <!-- Node 6: Java (x=-110, y=75) -->
    <g transform="translate(-115, 75)" class="p-stk-n3">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#ED8B00" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['openjdk']}" fill="#ED8B00"/>
      </g>
      <rect x="-20" y="20" width="40" height="16" rx="4" fill="#070c18" stroke="#ED8B00" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">Java</text>
    </g>

    <!-- Node 7: Git (x=120, y=72) -->
    <g transform="translate(125, 72)" class="p-stk-n2">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#F05032" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['git']}" fill="#F05032"/>
      </g>
      <rect x="-18" y="20" width="36" height="16" rx="4" fill="#070c18" stroke="#F05032" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">Git</text>
    </g>

    <!-- ===== ORBIT 3 NODES: Python, Streamlit, GitHub, Vercel ===== -->
    <!-- Node 8: Python (x=-315, y=-52) -->
    <g transform="translate(-320, -52)" class="p-stk-n3">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#3776AB" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['python']}" fill="#3776AB"/>
      </g>
      <rect x="-24" y="20" width="48" height="16" rx="4" fill="#070c18" stroke="#3776AB" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">Python</text>
    </g>

    <!-- Node 9: Streamlit (x=315, y=-55) -->
    <g transform="translate(320, -55)" class="p-stk-n1">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#FF4B4B" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['streamlit']}" fill="#FF4B4B"/>
      </g>
      <rect x="-28" y="20" width="56" height="16" rx="4" fill="#070c18" stroke="#FF4B4B" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">Streamlit</text>
    </g>

    <!-- Node 10: GitHub (x=-235, y=92) -->
    <g transform="translate(-240, 92)" class="p-stk-n2">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#ffffff" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['github']}" fill="#ffffff"/>
      </g>
      <rect x="-24" y="20" width="48" height="16" rx="4" fill="#070c18" stroke="#ffffff" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">GitHub</text>
    </g>

    <!-- Node 11: Vercel (x=245, y=88) -->
    <g transform="translate(245, 88)" class="p-stk-n3">
      <circle cx="0" cy="0" r="17" fill="#0d172e" stroke="#00d8ff" stroke-width="1.5"/>
      <g transform="translate(-8, -8) scale(0.68)">
        <path d="{icons['vercel']}" fill="#ffffff"/>
      </g>
      <rect x="-22" y="20" width="44" height="16" rx="4" fill="#070c18" stroke="#00d8ff" stroke-width="0.6"/>
      <text x="0" y="31" class="p-stk-mono" font-size="8.5" font-weight="700" fill="#f0f4fc" text-anchor="middle">Vercel</text>
    </g>
  </g>

  <!-- ================= GROUPED STACK CHIPS (BOTTOM) ================= -->
  <g class="p-stk-root" transform="translate(48, 298)">
    <text x="0" y="0" class="p-stk-mono" font-size="10.5" font-weight="700" fill="#7a8ea8" letter-spacing="1.2">// GROUPED TECH DOMAINS</text>
    
    <!-- 4 Domain Groups -->
    <g transform="translate(0, 14)">
      
      <!-- Group 1: Frontend Core -->
      <g transform="translate(0, 0)">
        <rect width="186" height="85" rx="10" fill="#0b1326" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.35"/>
        <text x="14" y="20" class="p-stk-mono" font-size="9.5" font-weight="700" fill="#247bff">FRONTEND CORE</text>
        <!-- Chips -->
        <g transform="translate(12, 32)">
          <rect x="0" y="0" width="48" height="22" rx="5" fill="#131e36"/>
          <text x="24" y="14" class="p-stk-mono" font-size="9" fill="#f0f4fc" text-anchor="middle">HTML5</text>

          <rect x="54" y="0" width="44" height="22" rx="5" fill="#131e36"/>
          <text x="76" y="14" class="p-stk-mono" font-size="9" fill="#f0f4fc" text-anchor="middle">CSS3</text>

          <rect x="104" y="0" width="58" height="22" rx="5" fill="#131e36"/>
          <text x="133" y="14" class="p-stk-mono" font-size="9" fill="#f0f4fc" text-anchor="middle">JavaScript</text>
        </g>
        <text x="14" y="72" class="p-abt-mono" font-size="8.5" fill="#6c809e">Semantic &amp; Interactive Web</text>
      </g>

      <!-- Group 2: Backend & DB -->
      <g transform="translate(198, 0)">
        <rect width="186" height="85" rx="10" fill="#0b1326" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.35"/>
        <text x="14" y="20" class="p-stk-mono" font-size="9.5" font-weight="700" fill="#247bff">BACKEND &amp; DATA</text>
        <g transform="translate(12, 32)">
          <rect x="0" y="0" width="42" height="22" rx="5" fill="#131e36"/>
          <text x="21" y="14" class="p-stk-mono" font-size="9" fill="#f0f4fc" text-anchor="middle">PHP</text>

          <rect x="48" y="0" width="54" height="22" rx="5" fill="#131e36"/>
          <text x="75" y="14" class="p-stk-mono" font-size="9" fill="#f0f4fc" text-anchor="middle">MySQL</text>

          <rect x="108" y="0" width="44" height="22" rx="5" fill="#131e36"/>
          <text x="130" y="14" class="p-stk-mono" font-size="9" fill="#f0f4fc" text-anchor="middle">Java</text>
        </g>
        <text x="14" y="72" class="p-abt-mono" font-size="8.5" fill="#6c809e">Relational Data &amp; Server Logic</text>
      </g>

      <!-- Group 3: AI & Scripting -->
      <g transform="translate(396, 0)">
        <rect width="186" height="85" rx="10" fill="#0b1326" stroke="#ff354f" stroke-width="0.8" stroke-opacity="0.35"/>
        <text x="14" y="20" class="p-stk-mono" font-size="9.5" font-weight="700" fill="#ff354f">AI &amp; SCRIPTING</text>
        <g transform="translate(12, 32)">
          <rect x="0" y="0" width="56" height="22" rx="5" fill="#131e36"/>
          <text x="28" y="14" class="p-stk-mono" font-size="9" fill="#ff8c9b" text-anchor="middle">Python</text>

          <rect x="62" y="0" width="70" height="22" rx="5" fill="#131e36"/>
          <text x="97" y="14" class="p-stk-mono" font-size="9" fill="#ff8c9b" text-anchor="middle">Streamlit</text>
        </g>
        <text x="14" y="72" class="p-abt-mono" font-size="8.5" fill="#6c809e">Intelligent Pipelines &amp; Apps</text>
      </g>

      <!-- Group 4: DevOps & Cloud -->
      <g transform="translate(594, 0)">
        <rect width="190" height="85" rx="10" fill="#0b1326" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.35"/>
        <text x="14" y="20" class="p-stk-mono" font-size="9.5" font-weight="700" fill="#247bff">WORKFLOW &amp; CLOUD</text>
        <g transform="translate(12, 32)">
          <rect x="0" y="0" width="40" height="22" rx="5" fill="#131e36"/>
          <text x="20" y="14" class="p-stk-mono" font-size="9" fill="#f0f4fc" text-anchor="middle">Git</text>

          <rect x="46" y="0" width="54" height="22" rx="5" fill="#131e36"/>
          <text x="73" y="14" class="p-stk-mono" font-size="9" fill="#f0f4fc" text-anchor="middle">GitHub</text>

          <rect x="106" y="0" width="54" height="22" rx="5" fill="#131e36"/>
          <text x="133" y="14" class="p-stk-mono" font-size="9" fill="#f0f4fc" text-anchor="middle">Vercel</text>
        </g>
        <text x="14" y="72" class="p-abt-mono" font-size="8.5" fill="#6c809e">Version Control &amp; Edge CI/CD</text>
      </g>
    </g>
  </g>
</svg>"""

# ==============================================================================
# 4. ID-DASHBOARD.SVG
# ==============================================================================
def build_id_dashboard():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 880 490" fill="none">
  <!--
    PRABHU ANGOTHU - LANYARD ID BADGE & VERIFIED REPOSITORIES
    Damped pendulum entrance settling to +/-1.7 degree perpetual gentle swing.
    Foil sweep animation across ID card.
    Dated & verified project metrics only.
    Fonts: Outfit, JetBrains Mono
  -->
  <defs>
    <style>
      {get_font_faces()}
      
      .p-id-root {{
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
      .p-id-mono {{
        font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
      }}
      
      /* Damped Pendulum Drop settling to perpetual +/- 1.7-degree gentle swing */
      @keyframes p-id-pendulum {{
        0% {{
          transform: translateY(-220px) rotate(16deg);
          opacity: 0;
        }}
        12% {{
          transform: translateY(0px) rotate(-13deg);
          opacity: 1;
        }}
        24% {{ transform: rotate(9deg); }}
        36% {{ transform: rotate(-5.5deg); }}
        48% {{ transform: rotate(3.2deg); }}
        60% {{ transform: rotate(-2.2deg); }}
        72% {{ transform: rotate(1.7deg); }}
        86% {{ transform: rotate(-1.7deg); }}
        100% {{ transform: rotate(1.7deg); }}
      }}
      
      /* Perpetual gentle swing (+/-1.7 deg) after initial drop */
      @keyframes p-id-perpetual-swing {{
        0% {{ transform: rotate(-1.7deg); }}
        50% {{ transform: rotate(1.7deg); }}
        100% {{ transform: rotate(-1.7deg); }}
      }}
      
      .p-id-lanyard-pendulum {{
        transform-origin: 195px 15px;
        animation: p-id-pendulum 3.2s cubic-bezier(0.25, 1, 0.5, 1) 0s 1 normal forwards,
                   p-id-perpetual-swing 4.2s ease-in-out 3.2s infinite;
      }}
      
      /* Foil / Light Sheen Sweep Across Badge */
      @keyframes p-id-foil-sweep {{
        0% {{ transform: translateX(-280px) rotate(25deg); opacity: 0; }}
        20% {{ opacity: 0.6; }}
        40% {{ transform: translateX(280px) rotate(25deg); opacity: 0; }}
        100% {{ transform: translateX(280px) rotate(25deg); opacity: 0; }}
      }}
      .p-id-sheen {{
        animation: p-id-foil-sweep 5.5s infinite ease-in-out;
      }}
      
      @media (prefers-reduced-motion: reduce) {{
        .p-id-lanyard-pendulum {{ animation: none; transform: rotate(0deg); opacity: 1; }}
        .p-id-sheen {{ animation: none; display: none; }}
      }}
    </style>
    
    <linearGradient id="p-id-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b16"/>
      <stop offset="60%" stop-color="#0a1024"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>

    <linearGradient id="p-id-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#247bff" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <!-- Metallic Clasp Chrome Gradient -->
    <linearGradient id="p-id-chrome" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#6a788e"/>
      <stop offset="25%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#8c9cb3"/>
      <stop offset="75%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#4a5568"/>
    </linearGradient>

    <!-- ID Card Acrylic Dark Gradient -->
    <linearGradient id="p-id-card-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0e172e"/>
      <stop offset="100%" stop-color="#070c18"/>
    </linearGradient>
    
    <!-- Holographic Foil Sheen Gradient -->
    <linearGradient id="p-id-sheen-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0"/>
      <stop offset="30%" stop-color="#ffffff" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#ff354f" stop-opacity="0.35"/>
      <stop offset="70%" stop-color="#247bff" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </linearGradient>

    <pattern id="p-id-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#247bff" fill-opacity="0.12"/>
    </pattern>

    <clipPath id="p-id-badge-clip">
      <rect x="70" y="60" width="250" height="395" rx="18"/>
    </clipPath>

    <clipPath id="p-id-port-clip">
      <rect x="88" y="130" width="214" height="155" rx="12"/>
    </clipPath>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="490" rx="20" fill="url(#p-id-bg)"/>
  <rect width="880" height="490" rx="20" fill="url(#p-id-dots)"/>
  <rect x="0.75" y="0.75" width="878.5" height="488.5" rx="19.25" fill="none" stroke="url(#p-id-border)" stroke-width="1.5"/>

  <!-- ================= LEFT: HANGING LANYARD ID WITH PENDULUM SWING ================= -->
  <!-- Top Anchor Cord (Static above pivot) -->
  <g transform="translate(195, 0)">
    <!-- Woven Lanyard Strap from Top edge to Clasp -->
    <path d="M-12 0 L-6 20 L6 20 L12 0" fill="#0d1b38" stroke="#247bff" stroke-width="1"/>
    <line x1="-3" y1="0" x2="-3" y2="20" stroke="#ff354f" stroke-width="1.5" stroke-dasharray="3 2"/>
    <line x1="3" y1="0" x2="3" y2="20" stroke="#247bff" stroke-width="1.5" stroke-dasharray="3 2"/>
  </g>

  <!-- PENDULUM SWING GROUP (Rotates around Pivot: 195, 20) -->
  <g class="p-id-lanyard-pendulum">
    
    <!-- Metal Clasp & Carabiner Ring -->
    <g transform="translate(195, 20)">
      <!-- Swivel Ring -->
      <ellipse cx="0" cy="8" rx="8" ry="6" fill="none" stroke="url(#p-id-chrome)" stroke-width="3"/>
      <!-- Metal Trigger Clip -->
      <path d="M-5 13 L5 13 L6 32 L-6 32 Z" fill="url(#p-id-chrome)"/>
      <rect x="-7" y="30" width="14" height="6" rx="2" fill="url(#p-id-chrome)"/>
      <circle cx="0" cy="22" r="2.5" fill="#334155"/>
      <!-- ID Badge Slot Hook -->
      <path d="M-3 36 L3 36 L2 45 L-2 45 Z" fill="url(#p-id-chrome)"/>
    </g>

    <!-- THE ID CARD -->
    <!-- Card Frame (x=70, y=60, w=250, h=395) -->
    <g class="p-id-root">
      <!-- Shadow -->
      <rect x="74" y="66" width="250" height="395" rx="18" fill="#000000" fill-opacity="0.45"/>
      
      <!-- Card Body -->
      <rect x="70" y="60" width="250" height="395" rx="18" fill="url(#p-id-card-bg)" stroke="#247bff" stroke-width="1.2"/>
      
      <!-- Inner Holographic Foil Sweep (Clipped to Card) -->
      <g clip-path="url(#p-id-badge-clip)">
        <!-- Sweeping Light Beam -->
        <rect x="0" y="0" width="90" height="500" fill="url(#p-id-sheen-grad)" class="p-id-sheen"/>
      </g>

      <!-- Slot Punch Hole at Top -->
      <rect x="180" y="68" width="30" height="7" rx="3.5" fill="#070c18" stroke="#334155" stroke-width="1"/>

      <!-- Badge Header Row -->
      <g transform="translate(86, 92)">
        <text x="0" y="0" class="p-id-mono" font-size="8.5" font-weight="700" fill="#247bff" letter-spacing="1">DEV PASS // 2026</text>
        <rect x="164" y="-10" width="54" height="15" rx="4" fill="#13203c"/>
        <text x="170" y="1" class="p-id-mono" font-size="8.5" fill="#f0f4fc">INDIA 🇮🇳</text>
      </g>

      <!-- Security Microchip Graphic -->
      <g transform="translate(88, 102)">
        <rect x="0" y="0" width="26" height="19" rx="3" fill="#cf9d38" stroke="#8c6819" stroke-width="0.8"/>
        <line x1="0" y1="9" x2="26" y2="9" stroke="#8c6819" stroke-width="0.8"/>
        <line x1="13" y1="0" x2="13" y2="19" stroke="#8c6819" stroke-width="0.8"/>
        <line x1="7" y1="4" x2="7" y2="15" stroke="#8c6819" stroke-width="0.6"/>
        <line x1="19" y1="4" x2="19" y2="15" stroke="#8c6819" stroke-width="0.6"/>
      </g>

      <!-- Contactless NFC Wave Graphic -->
      <g transform="translate(122, 111)" stroke="#247bff" stroke-width="1.2" fill="none">
        <path d="M0 0 A6 6 0 0 1 0 8"/>
        <path d="M4 -2 A10 10 0 0 1 4 10"/>
      </g>

      <!-- Portrait Box -->
      <rect x="87" y="129" width="216" height="157" rx="13" fill="#070c18" stroke="url(#p-id-border)" stroke-width="1.2"/>
      
      <!-- Inlined Portrait with Alpha Preserved -->
      <g clip-path="url(#p-id-port-clip)">
        <rect x="88" y="130" width="214" height="155" fill="#090f20"/>
        <!-- Centered Prabhu Portrait -->
        <image href="data:image/png;base64,{id_b64}" x="70" y="125" width="250" height="165" preserveAspectRatio="xMidYMid meet"/>
      </g>

      <!-- Identity Details -->
      <g transform="translate(88, 308)">
        <text x="0" y="0" font-size="16" font-weight="800" fill="#ffffff" letter-spacing="-0.2">PRABHU ANGOTHU</text>
        <text x="0" y="16" class="p-id-mono" font-size="10" font-weight="700" fill="#247bff">Student &amp; Web/AI Developer</text>
        
        <!-- Metadata Row -->
        <g transform="translate(0, 32)">
          <text x="0" y="0" class="p-id-mono" font-size="8.5" fill="#7588a8">ID: DEV-PA-120607</text>
          <text x="135" y="0" class="p-id-mono" font-size="8.5" fill="#38ef7d">● VERIFIED</text>
        </g>
      </g>

      <!-- Barcode Graphic (Authentic variable line widths) -->
      <g transform="translate(88, 362)">
        <rect x="0" y="0" width="214" height="42" rx="6" fill="#070c18" stroke="#172440" stroke-width="0.8"/>
        <!-- Barcode lines -->
        <g transform="translate(18, 6)" fill="#ffffff">
          <rect x="0" y="0" width="2" height="20"/>
          <rect x="4" y="0" width="3" height="20"/>
          <rect x="9" y="0" width="1" height="20"/>
          <rect x="12" y="0" width="4" height="20"/>
          <rect x="18" y="0" width="2" height="20"/>
          <rect x="22" y="0" width="1" height="20"/>
          <rect x="25" y="0" width="3" height="20"/>
          <rect x="31" y="0" width="2" height="20"/>
          <rect x="35" y="0" width="4" height="20"/>
          <rect x="42" y="0" width="1" height="20"/>
          <rect x="45" y="0" width="2" height="20"/>
          <rect x="50" y="0" width="3" height="20"/>
          <rect x="55" y="0" width="1" height="20"/>
          <rect x="58" y="0" width="2" height="20"/>
          <rect x="63" y="0" width="4" height="20"/>
          <rect x="70" y="0" width="1" height="20"/>
          <rect x="74" y="0" width="3" height="20"/>
          <rect x="80" y="0" width="2" height="20"/>
          <rect x="84" y="0" width="1" height="20"/>
          <rect x="88" y="0" width="4" height="20"/>
          <rect x="95" y="0" width="2" height="20"/>
          <rect x="100" y="0" width="1" height="20"/>
          <rect x="103" y="0" width="3" height="20"/>
          <rect x="108" y="0" width="2" height="20"/>
          <rect x="113" y="0" width="4" height="20"/>
          <rect x="120" y="0" width="1" height="20"/>
          <rect x="123" y="0" width="2" height="20"/>
          <rect x="128" y="0" width="3" height="20"/>
          <rect x="134" y="0" width="1" height="20"/>
          <rect x="137" y="0" width="4" height="20"/>
          <rect x="144" y="0" width="2" height="20"/>
          <rect x="148" y="0" width="3" height="20"/>
          <rect x="154" y="0" width="1" height="20"/>
          <rect x="158" y="0" width="2" height="20"/>
          <rect x="162" y="0" width="4" height="20"/>
          <rect x="169" y="0" width="2" height="20"/>
          <rect x="174" y="0" width="2" height="20"/>
        </g>
        <text x="107" y="35" class="p-id-mono" font-size="8" fill="#7588a8" text-anchor="middle" letter-spacing="3">8 901206 072026</text>
      </g>
    </g>
  </g>

  <!-- ================= RIGHT: VERIFIED REPOSITORIES & METRICS ================= -->
  <g class="p-id-root" transform="translate(355, 30)">
    <!-- Header -->
    <text x="0" y="16" class="p-id-mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.5">// VERIFIED REPOSITORIES &amp; DATA</text>
    <text x="0" y="42" font-size="22" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Authentic Projects &amp; Milestones</text>
    
    <!-- Verified Live Status Badge -->
    <rect x="375" y="24" width="105" height="22" rx="6" fill="#13203c" stroke="#38ef7d" stroke-width="0.8"/>
    <circle cx="387" cy="35" r="3" fill="#38ef7d"/>
    <text x="395" y="39" class="p-id-mono" font-size="9" font-weight="700" fill="#f0f4fc">DATED 2026</text>

    <!-- 3 Verified Project Cards -->
    <g transform="translate(0, 60)">
      
      <!-- Project 1: PathSetu -->
      <g transform="translate(0, 0)">
        <rect width="485" height="88" rx="12" fill="#0b1326" stroke="#247bff" stroke-width="1" stroke-opacity="0.4"/>
        <g transform="translate(18, 20)">
          <!-- Title & Badges -->
          <text x="0" y="0" font-size="16" font-weight="800" fill="#ffffff">PathSetu</text>
          <rect x="80" y="-12" width="138" height="18" rx="4" fill="#247bff" fill-opacity="0.18"/>
          <text x="86" y="0" class="p-id-mono" font-size="9" font-weight="700" fill="#247bff">AI CAREER PLATFORM</text>
          
          <rect x="224" y="-12" width="100" height="18" rx="4" fill="#38ef7d" fill-opacity="0.15"/>
          <text x="230" y="0" class="p-id-mono" font-size="9" font-weight="700" fill="#38ef7d">LIVE PRODUCTION</text>

          <!-- Description -->
          <text x="0" y="22" font-size="12" fill="#a4b5cf">
            <tspan x="0" dy="0">AI career guidance platform for students to explore pathways, discover</tspan>
            <tspan x="0" dy="16">in-demand skills, and construct comprehensive educational roadmaps.</tspan>
          </text>
          
          <!-- Stack & URL -->
          <text x="0" y="56" class="p-id-mono" font-size="9.5" fill="#788ba8">
            <tspan fill="#ff354f">Stack: </tspan>Python, Streamlit, AI, Vercel | <tspan fill="#247bff">pathsetu-eight.vercel.app</tspan>
          </text>
        </g>
      </g>

      <!-- Project 2: Personal Portfolio Website -->
      <g transform="translate(0, 100)">
        <rect width="485" height="88" rx="12" fill="#0b1326" stroke="#247bff" stroke-width="1" stroke-opacity="0.4"/>
        <g transform="translate(18, 20)">
          <text x="0" y="0" font-size="16" font-weight="800" fill="#ffffff">Personal Portfolio Website</text>
          <rect x="200" y="-12" width="98" height="18" rx="4" fill="#247bff" fill-opacity="0.18"/>
          <text x="206" y="0" class="p-id-mono" font-size="9" font-weight="700" fill="#247bff">PORTFOLIO V2</text>
          
          <rect x="304" y="-12" width="100" height="18" rx="4" fill="#38ef7d" fill-opacity="0.15"/>
          <text x="310" y="0" class="p-id-mono" font-size="9" font-weight="700" fill="#38ef7d">LIVE PRODUCTION</text>

          <text x="0" y="22" font-size="12" fill="#a4b5cf">
            <tspan x="0" dy="0">High-performance responsive personal engineering portfolio showcasing</tspan>
            <tspan x="0" dy="16">web apps, development projects, technical skills, and interactive contact.</tspan>
          </text>
          
          <text x="0" y="56" class="p-id-mono" font-size="9.5" fill="#788ba8">
            <tspan fill="#ff354f">Stack: </tspan>HTML5, CSS3, JavaScript, Vercel | <tspan fill="#247bff">portfolio-v2-nine-blue.vercel.app</tspan>
          </text>
        </g>
      </g>

      <!-- Project 3: AI University Event Feedback System -->
      <g transform="translate(0, 200)">
        <rect width="485" height="88" rx="12" fill="#0b1326" stroke="#ff354f" stroke-width="1" stroke-opacity="0.4"/>
        <g transform="translate(18, 20)">
          <text x="0" y="0" font-size="16" font-weight="800" fill="#ffffff">AI EventPulse Feedback System</text>
          <rect x="250" y="-12" width="102" height="18" rx="4" fill="#ff354f" fill-opacity="0.18"/>
          <text x="256" y="0" class="p-id-mono" font-size="9" font-weight="700" fill="#ff354f">EVENTPULSE ARCH</text>

          <rect x="358" y="-12" width="90" height="18" rx="4" fill="#1e293b"/>
          <text x="364" y="0" class="p-id-mono" font-size="9" font-weight="700" fill="#cbd5e1">OPEN SOURCE</text>

          <text x="0" y="22" font-size="12" fill="#a4b5cf">
            <tspan x="0" dy="0">System architecture automating university post-event student feedback</tspan>
            <tspan x="0" dy="16">collection, intelligent sentiment aggregation, and report structuring.</tspan>
          </text>
          
          <text x="0" y="56" class="p-id-mono" font-size="9.5" fill="#788ba8">
            <tspan fill="#ff354f">Stack: </tspan>PHP, MySQL, AI Concepts | <tspan fill="#247bff">github.com/prabhu120607-ops/eventpulse</tspan>
          </text>
        </g>
      </g>
    </g>

    <!-- Verified Metrics Summary Bar (Dated & Genuine) -->
    <g transform="translate(0, 365)">
      <rect width="485" height="48" rx="10" fill="#091024" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.3"/>
      
      <g transform="translate(16, 29)">
        <text x="0" y="0" class="p-id-mono" font-size="10" fill="#8ca0c0">
          <tspan font-weight="700" fill="#f0f4fc">Status: </tspan>Student &amp; Independent Dev  |  
          <tspan font-weight="700" fill="#f0f4fc">Core: </tspan>Full-Stack &amp; AI  |  
          <tspan font-weight="700" fill="#38ef7d">Verified 2026</tspan>
        </text>
      </g>
    </g>
  </g>
</svg>"""

# ==============================================================================
# 5. CONNECT.SVG
# ==============================================================================
def build_connect():
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="auto" viewBox="0 0 880 340" fill="none">
  <!--
    PRABHU ANGOTHU - CONNECT & COLLABORATE
    Pointing character on left, generously spaced social cards on right with platform icons and nudging arrows.
    Preserves exact character image and alpha without redrawing or silhouette masks.
    Fonts: Outfit, JetBrains Mono
  -->
  <defs>
    <style>
      {get_font_faces()}
      
      .p-con-root {{
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
      .p-con-mono {{
        font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
      }}
      
      /* Nudging Arrow Animation */
      @keyframes p-con-nudge {{
        0%, 100% {{ transform: translateX(0); }}
        50% {{ transform: translateX(7px); }}
      }}
      .p-con-arrow {{
        animation: p-con-nudge 1.6s ease-in-out infinite;
      }}
      
      /* Gentle Atmospheric Pulse Behind Character */
      @keyframes p-con-glow-pulse {{
        0%, 100% {{ opacity: 0.35; transform: scale(1); }}
        50% {{ opacity: 0.6; transform: scale(1.08); }}
      }}
      .p-con-glow {{
        animation: p-con-glow-pulse 5.0s ease-in-out infinite;
        transform-origin: 180px 170px;
      }}
      
      @media (prefers-reduced-motion: reduce) {{
        .p-con-arrow {{ animation: none; transform: translateX(3px); }}
        .p-con-glow {{ animation: none; opacity: 0.4; }}
      }}
    </style>
    
    <linearGradient id="p-con-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b16"/>
      <stop offset="60%" stop-color="#0a1024"/>
      <stop offset="100%" stop-color="#070b16"/>
    </linearGradient>

    <linearGradient id="p-con-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#247bff" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
    </linearGradient>

    <radialGradient id="p-con-glow-blue" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#247bff" stop-opacity="0.3"/>
      <stop offset="60%" stop-color="#247bff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="p-con-glow-crimson" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff354f" stop-opacity="0.25"/>
      <stop offset="60%" stop-color="#ff354f" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
    </radialGradient>

    <pattern id="p-con-dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="#247bff" fill-opacity="0.12"/>
    </pattern>

    <clipPath id="p-con-char-clip">
      <rect x="15" y="15" width="345" height="310" rx="16"/>
    </clipPath>
  </defs>

  <!-- Background Base -->
  <rect width="880" height="340" rx="20" fill="url(#p-con-bg)"/>
  <rect width="880" height="340" rx="20" fill="url(#p-con-dots)"/>
  <rect x="0.75" y="0.75" width="878.5" height="338.5" rx="19.25" fill="none" stroke="url(#p-con-border)" stroke-width="1.5"/>

  <!-- Atmospheric Glow Behind Pointing Hand & Character -->
  <circle cx="180" cy="170" r="150" fill="url(#p-con-glow-blue)" class="p-con-glow"/>
  <circle cx="330" cy="150" r="100" fill="url(#p-con-glow-crimson)" class="p-con-glow"/>

  <!-- ================= LEFT: POINTING CHARACTER ================= -->
  <!-- Bounding box: x=[30, 1388], y=[18, 992]. Hand points to the viewer's RIGHT -->
  <g clip-path="url(#p-con-char-clip)">
    <!-- Base card container on left -->
    <rect x="15" y="15" width="345" height="310" rx="16" fill="#080e1c" stroke="#247bff" stroke-width="1" stroke-opacity="0.3"/>
    
    <!-- Subtle Radar / Concentric Rings behind pointing arm -->
    <circle cx="320" cy="140" r="40" fill="none" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.3" stroke-dasharray="3 4"/>
    <circle cx="320" cy="140" r="70" fill="none" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.2" stroke-dasharray="4 6"/>
    <circle cx="320" cy="140" r="105" fill="none" stroke="#ff354f" stroke-width="0.8" stroke-opacity="0.15" stroke-dasharray="5 7"/>
    
    <!-- Inlined High-DPI Pointing Character (Preserving Exact Alpha) -->
    <image href="data:image/png;base64,{conn_b64}" x="-10" y="15" width="375" height="310" preserveAspectRatio="xMidYMid meet"/>
    
    <!-- Corner HUD markers -->
    <path d="M25 35 L25 25 L35 25" stroke="#247bff" stroke-width="1.8" fill="none"/>
    <path d="M345 35 L345 25 L335 25" stroke="#247bff" stroke-width="1.8" fill="none"/>
    <path d="M25 305 L25 315 L35 315" stroke="#ff354f" stroke-width="1.8" fill="none"/>
    <path d="M345 305 L345 315 L335 315" stroke="#ff354f" stroke-width="1.8" fill="none"/>
  </g>

  <!-- ================= RIGHT: GENEROUSLY SPACED SOCIAL CARDS ================= -->
  <g class="p-con-root" transform="translate(385, 25)">
    <!-- Header -->
    <text x="0" y="16" class="p-con-mono" font-size="11" font-weight="700" fill="#247bff" letter-spacing="1.5">// LET'S CONNECT &amp; BUILD</text>
    <text x="0" y="40" font-size="20" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Connect Across The Web</text>

    <!-- Social Cards Group (4 cards, height: 50, spacing: 12) -->
    <g transform="translate(0, 56)">
      
      <!-- CARD 1: GitHub -->
      <g transform="translate(0, 0)">
        <rect width="460" height="50" rx="10" fill="#0c1429" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.35"/>
        <g transform="translate(14, 13)">
          <circle cx="12" cy="12" r="12" fill="#ffffff" fill-opacity="0.12"/>
          <g transform="translate(4, 4) scale(0.66)">
            <path d="{icons['github']}" fill="#ffffff"/>
          </g>
          <text x="34" y="10" font-size="13" font-weight="700" fill="#ffffff">GitHub</text>
          <text x="34" y="21" class="p-con-mono" font-size="9.5" fill="#7d92b5">@prabhu120607-ops • Code repositories &amp; open-source projects</text>
          
          <!-- Nudging Arrow -->
          <g transform="translate(415, 6)" class="p-con-arrow">
            <circle cx="8" cy="8" r="10" fill="#15223d"/>
            <path d="M5 8 L11 8 M9 5 L12 8 L9 11" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          </g>
        </g>
      </g>

      <!-- CARD 2: LinkedIn -->
      <g transform="translate(0, 62)">
        <rect width="460" height="50" rx="10" fill="#0c1429" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.35"/>
        <g transform="translate(14, 13)">
          <circle cx="12" cy="12" r="12" fill="#0a66c2" fill-opacity="0.18"/>
          <g transform="translate(4, 4) scale(0.66)">
            <path d="{icons['linkedin']}" fill="#0a66c2"/>
          </g>
          <text x="34" y="10" font-size="13" font-weight="700" fill="#ffffff">LinkedIn</text>
          <text x="34" y="21" class="p-con-mono" font-size="9.5" fill="#7d92b5">Prabhu Kumar Amgothu • Professional network &amp; updates</text>
          
          <!-- Nudging Arrow -->
          <g transform="translate(415, 6)" class="p-con-arrow">
            <circle cx="8" cy="8" r="10" fill="#15223d"/>
            <path d="M5 8 L11 8 M9 5 L12 8 L9 11" stroke="#247bff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          </g>
        </g>
      </g>

      <!-- CARD 3: Instagram -->
      <g transform="translate(0, 124)">
        <rect width="460" height="50" rx="10" fill="#0c1429" stroke="#ff354f" stroke-width="0.8" stroke-opacity="0.35"/>
        <g transform="translate(14, 13)">
          <circle cx="12" cy="12" r="12" fill="#e4405f" fill-opacity="0.18"/>
          <g transform="translate(4, 4) scale(0.66)">
            <path d="{icons['instagram']}" fill="#e4405f"/>
          </g>
          <text x="34" y="10" font-size="13" font-weight="700" fill="#ffffff">Instagram</text>
          <text x="34" y="21" class="p-con-mono" font-size="9.5" fill="#7d92b5">@_prabhu_120607_ • Tech journey, highlights &amp; creativity</text>
          
          <!-- Nudging Arrow -->
          <g transform="translate(415, 6)" class="p-con-arrow">
            <circle cx="8" cy="8" r="10" fill="#15223d"/>
            <path d="M5 8 L11 8 M9 5 L12 8 L9 11" stroke="#ff354f" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          </g>
        </g>
      </g>

      <!-- CARD 4: Portfolio Website -->
      <g transform="translate(0, 186)">
        <rect width="460" height="50" rx="10" fill="#0c1429" stroke="#247bff" stroke-width="0.8" stroke-opacity="0.35"/>
        <g transform="translate(14, 13)">
          <circle cx="12" cy="12" r="12" fill="#247bff" fill-opacity="0.18"/>
          <g transform="translate(4, 4)">
            <!-- Globe / Web SVG Icon -->
            <circle cx="8" cy="8" r="7" fill="none" stroke="#247bff" stroke-width="1.4"/>
            <ellipse cx="8" cy="8" rx="3.5" ry="7" fill="none" stroke="#247bff" stroke-width="1.2"/>
            <line x1="1" y1="8" x2="15" y2="8" stroke="#247bff" stroke-width="1.2"/>
          </g>
          <text x="34" y="10" font-size="13" font-weight="700" fill="#ffffff">Portfolio Website</text>
          <text x="34" y="21" class="p-con-mono" font-size="9.5" fill="#7d92b5">portfolio-v2-nine-blue.vercel.app • Live projects &amp; contact</text>
          
          <!-- Nudging Arrow -->
          <g transform="translate(415, 6)" class="p-con-arrow">
            <circle cx="8" cy="8" r="10" fill="#15223d"/>
            <path d="M5 8 L11 8 M9 5 L12 8 L9 11" stroke="#247bff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          </g>
        </g>
      </g>

    </g>
  </g>
</svg>"""

# ==============================================================================
# MAIN WRITE LOOP
# ==============================================================================
if __name__ == '__main__':
    files = {
        'assets/hero.svg': build_hero(),
        'assets/about-life.svg': build_about_life(),
        'assets/stack.svg': build_stack(),
        'assets/id-dashboard.svg': build_id_dashboard(),
        'assets/connect.svg': build_connect()
    }
    
    for filename, content in files.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        size_kb = os.path.getsize(filename) / 1024
        print(f"Generated {filename} ({size_kb:.1f} KB)")
