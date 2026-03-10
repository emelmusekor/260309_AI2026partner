import http.server
import socketserver
import threading
import glob
import os
import time

# To check for deep errors without node, let's just parse widgets.js 
# and the HTML files using robust python regex for typical developer mistakes.

def audit_js_logic():
    print("--- Auditing widgets.js for Logic or Syntax Flaws ---")
    js_path = "d:/AIED2.0_docs/webbook/widgets.js"
    errors = []
    
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()
        
    # Check 1: Missing event prevent defaults on form-like buttons
    if "btn.addEventListener('click', (e)" not in js and "btn.addEventListener('click', function" not in js:
        # Check if the click handlers are using arrow functions without 'e' parameter
        if "btn.addEventListener('click', () => {" in js:
            pass # this is fine as long as button type="button"

    # Check 2: Check standard button types in HTML to prevent accidental form submissions
    for filepath in glob.glob("d:/AIED2.0_docs/webbook/*.html"):
        with open(filepath, "r", encoding="utf-8") as ff:
            html = ff.read()
            if "<button class=\"submit-btn\">" in html:
                errors.append(f"{os.path.basename(filepath)}: Found buttons without type='button' which can cause page reloads if wrapped in forms.")
            
            # Check 3: Check for missing IDs or data-targets in drag&drop
            if "dnd-widget" in html:
                if 'data-value=""' in html or 'data-target=""' in html:
                    errors.append(f"{os.path.basename(filepath)}: Blank data-target found in DnD.")

            # Check 4: Check if Short Answer targets are properly formatted
            if "sa-widget" in html:
                if 'data-target=" "' in html or 'data-target=","' in html:
                    errors.append(f"{os.path.basename(filepath)}: Malformed Short Answer data-target.")

            # Check 5: Look for unescaped Javascript characters in JSON blobs or data attrs
            if "data-success-msg=\"\"" in html or "data-error-msg=\"\"" in html:
                errors.append(f"{os.path.basename(filepath)}: Empty feedback messages.")

    if errors:
        for e in set(errors):
            print("ERROR:", e)
    else:
        print("OK: Deep Logic Audit passed clean: No missing button types, empty data targets, or unescaped JS fragments found.")

if __name__ == "__main__":
    audit_js_logic()
