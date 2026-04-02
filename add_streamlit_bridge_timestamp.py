import os
import glob
import re

directories = ["simulations_kannada", "maths_simulations_kannada"]
count = 0

pattern = re.compile(
    r'function\s+report\(\)\s*\{\s*var\s+p\s*=\s*payload\(\);\s*if\s*\(\w*\.AndroidBridge\).*?\}\s*\}',
    re.MULTILINE | re.DOTALL
)

# If the file hasn't been updated to the var p = payload version, use the old pattern
old_pattern = re.compile(
    r'function\s+report\(\)\s*\{\s*if\s*\(!window\.AndroidBridge\)\s*return;\s*try\s*\{\s*window\.AndroidBridge\.onParamChanged\(JSON\.stringify\(payload\(\)\)\);\s*\}\s*catch\(e\)\s*\{\}\s*\}',
    re.MULTILINE | re.DOTALL
)

replacement = """function report() {
        var p = payload();
        if (window.AndroidBridge) {
            try { window.AndroidBridge.onParamChanged(JSON.stringify(p)); } catch(e) {}
        }
        if (window.parent !== window) {
            p.__t = new Date().getTime(); // force streamlit rerun
            try { window.parent.postMessage({type: 'simulation_param_change', params: p}, '*'); } catch(e) {}
        }
    }"""

for directory in directories:
    for filepath in glob.glob(f"{directory}/**/*.html", recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "AndroidBridge" in content:
            new_content = pattern.sub(replacement, content)
            if new_content == content:
                new_content = old_pattern.sub(replacement, content)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Successfully injected forced-timestamp bridge into {count} HTML files.")
