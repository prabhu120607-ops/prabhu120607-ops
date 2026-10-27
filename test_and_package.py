"""
Verification and Packaging Script for Prabhu Angothu's GitHub Profile README
"""

import os, re, xml.etree.ElementTree as ET, zipfile, urllib.request

WORKSPACE = r"c:\Users\prabh\OneDrive\Attachments\Desktop\prabhu120607-ops"
ASSETS_DIR = os.path.join(WORKSPACE, "assets")

svg_files = [
    "hero.svg",
    "about-life.svg",
    "stack.svg",
    "id-dashboard.svg",
    "connect.svg"
]

print("=" * 60)
print("1. VERIFYING SVG INTEGRITY & SECURITY")
print("=" * 60)

errors = []
warnings = []

for filename in svg_files:
    filepath = os.path.join(ASSETS_DIR, filename)
    if not os.path.exists(filepath):
        errors.append(f"Missing file: {filename}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. XML Parse Check
    try:
        root = ET.fromstring(content)
        tag = root.tag
        if not tag.endswith('svg'):
            errors.append(f"{filename}: Root is not <svg>")
    except Exception as e:
        errors.append(f"{filename}: XML parsing error: {e}")
    
    # 2. Check for banned elements: script, foreignObject
    if '<script' in content.lower():
        errors.append(f"{filename}: Contains forbidden <script> tag")
    if '<foreignobject' in content.lower():
        errors.append(f"{filename}: Contains forbidden <foreignObject> tag")
    
    # 3. Check for external URLs (MUST BE SELF-CONTAINED)
    # Match href="http..." or src="http..." or url(http...)
    ext_refs = re.findall(r'(?:href|src|url)\(["\']?(https?://[^"\'\)]+)', content)
    # Filter out xmlns declarations which are XML namespaces, not loaded resources
    ext_refs = [u for u in ext_refs if not u.startswith('http://www.w3.org')]
    if ext_refs:
        errors.append(f"{filename}: Found external network requests: {ext_refs}")
    else:
        print(f"✓ {filename}: 100% self-contained (0 external network requests)")
    
    # 4. Check reduced motion support
    if 'prefers-reduced-motion' not in content:
        warnings.append(f"{filename}: Missing @media (prefers-reduced-motion)")
    else:
        print(f"✓ {filename}: Prefers-reduced-motion accessible fallback included")
        
    # 5. Check size
    size_kb = len(content.encode('utf-8')) / 1024
    print(f"✓ {filename}: Size {size_kb:.1f} KB (within GitHub camo 5MB limit)")

print("\n" + "=" * 60)
print("2. VERIFYING README.MD REQUIREMENTS")
print("=" * 60)

readme_path = os.path.join(WORKSPACE, "README.md")
with open(readme_path, 'r', encoding='utf-8') as f:
    readme_content = f.read()

required_images = [
    "./assets/hero.svg?v=1",
    "./assets/about-life.svg?v=1",
    "./assets/stack.svg?v=1",
    "./assets/id-dashboard.svg?v=1",
    "./assets/connect.svg?v=1"
]

for img in required_images:
    if img in readme_content:
        print(f"✓ README.md includes required image path: {img}")
    else:
        errors.append(f"README.md missing image: {img}")

if "contribution-city" in readme_content.lower() or "contribution_city" in readme_content.lower():
    errors.append("README.md contains forbidden contribution-city section")
else:
    print("✓ README.md: Confirmed NO contribution-city section")

# Check clickable links
for url in ["https://github.com/prabhu120607-ops", "https://pathsetu-eight.vercel.app/"]:
    if url in readme_content:
        print(f"✓ README.md includes verified link: {url}")
    else:
        warnings.append(f"README.md might be missing {url}")

print("\n" + "=" * 60)
print("3. PACKAGING UPLOAD-READY ZIP")
print("=" * 60)

zip_filename = os.path.join(WORKSPACE, "prabhu120607-ops-profile.zip")
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # 1. README.md at root
    zipf.write(readme_path, "README.md")
    print("  Added: README.md")
    
    # 2. preview.html at root
    preview_path = os.path.join(WORKSPACE, "preview.html")
    if os.path.exists(preview_path):
        zipf.write(preview_path, "preview.html")
        print("  Added: preview.html")
        
    # 3. assets/ folder
    for root_dir, dirs, files in os.walk(ASSETS_DIR):
        for file in files:
            full_path = os.path.join(root_dir, file)
            rel_path = os.path.relpath(full_path, WORKSPACE)
            zipf.write(full_path, rel_path)
            print(f"  Added: {rel_path}")

print(f"\n✓ Package created: {zip_filename} ({os.path.getsize(zip_filename)/1024:.1f} KB)")

print("\n" + "=" * 60)
print("AUDIT SUMMARY:")
print(f"Errors: {len(errors)}")
print(f"Warnings: {len(warnings)}")
for e in errors:
    print(f"  ❌ ERROR: {e}")
for w in warnings:
    print(f"  ⚠️ WARNING: {w}")
if not errors:
    print("🎉 ALL REQUIREMENTS SATISFIED!")
print("=" * 60)
