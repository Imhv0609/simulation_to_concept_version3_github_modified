import os
import glob

def inject_bridge():
    # We want to inject inside `function report() { ... }`
    # Just after `if (window.AndroidBridge) { ... }`
    
    html_files = glob.glob("simulations_kannada/*.html")
    count = 0
    
    injection = """
        if (window.parent) {
            p['__t'] = Date.now();
            window.parent.postMessage({
                type: 'simulation_update',
                params: p
            }, '*');
        }
"""
    
    for fp in html_files:
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "type: 'simulation_update'" in content:
            continue
            
        # Find the function report
        # We know it looks exactly like:
        #     function report() {
        #         var p = payload();
        #         if (window.AndroidBridge) {
        #             try { window.AndroidBridge.onParamChanged(JSON.stringify(p)); } catch(e) {}
        #         }
        
        target = "try { window.AndroidBridge.onParamChanged(JSON.stringify(p)); } catch(e) {}\n        }"
        
        if target in content:
            new_content = content.replace(target, target + injection)
            with open(fp, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            
    print(f"Injected into {count} files.")

if __name__ == "__main__":
    inject_bridge()
