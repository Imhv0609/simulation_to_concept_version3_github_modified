import glob

directories = ["simulations_kannada", "maths_simulations_kannada"]
count = 0

malformed_block = """    function report() {
        var p = payload();
        if (window.AndroidBridge) {
            try { window.AndroidBridge.onParamChanged(JSON.stringify(p)); } catch(e) {}
        }
        if (window.parent !== window) {
            p.__t = new Date().getTime(); // force streamlit rerun
            try { window.parent.postMessage({type: 'simulation_param_change', params: p}, '*'); } catch(e) {}
        }
    }
        if (window.parent !== window) {
            try { window.parent.postMessage({type: 'simulation_param_change', params: p}, '*'); } catch(e) {}
        }
    }"""

clean_block = """    function report() {
        var p = payload();
        if (window.AndroidBridge) {
            try { window.AndroidBridge.onParamChanged(JSON.stringify(p)); } catch(e) {}
        }
        if (window.parent !== window) {
            p.__t = new Date().getTime(); // force streamlit rerun
            try { window.parent.postMessage({type: 'simulation_param_change', params: p}, '*'); } catch(e) {}
        }
    }"""

malformed_block_2 = """function report() {
        var p = payload();
        if (window.AndroidBridge) {
            try { window.AndroidBridge.onParamChanged(JSON.stringify(p)); } catch(e) {}
        }
        if (window.parent !== window) {
            p.__t = new Date().getTime(); // force streamlit rerun
            try { window.parent.postMessage({type: 'simulation_param_change', params: p}, '*'); } catch(e) {}
        }
    }
        if (window.parent !== window) {
            try { window.parent.postMessage({type: 'simulation_param_change', params: p}, '*'); } catch(e) {}
        }
    }"""

malformed_block_3 = """    function report() {
        var p = payload();
        if (window.AndroidBridge) {
            try { window.AndroidBridge.onParamChanged(JSON.stringify(p)); } catch(e) {}
        }
        if (window.parent !== window) {
            p.__t = new Date().getTime(); // force streamlit rerun
            try { window.parent.postMessage({type: 'simulation_param_change', params: p}, '*'); } catch(e) {}
        }
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
            
        modified = content.replace(malformed_block, clean_block).replace(malformed_block_2, clean_block).replace(malformed_block_3, clean_block)
        
        # Also fix any other similar dangling blocks
        import re
        dangling_pattern = re.compile(
            r'function\s+report\(\)\s*\{.*?\}\s*if\s*\(\w*\.parent\s*!==\s*\w*\)\s*\{.*?\}\s*\}',
            re.MULTILINE | re.DOTALL
        )
        if "if (window.parent !== window)" in modified and modified != content:
            pass # The replace worked
        else:
            # Let's use a very safe regex to find the report block and replace it completely
            report_body_pattern = re.compile(
                r'function\s+report\(\)\s*\{[^{}]*?(?:\{[^{}]*\}[^{}]*)*\}\s*(?:if\s*\([^\{]+\)\s*\{[^\}]+\}\s*\})?',
                re.MULTILINE | re.DOTALL
            )
            # Actually, I'll just rely on a slightly looser replace
            pass
            
        # simpler, highly targeted regex cleanup
        bad_tail = re.compile(r'\}\s*if\s*\(window\.parent\s*!==\s*window\)\s*\{\s*(?:p\.__t[^\n]+)?\s*try\s*\{\s*window\.parent\.postMessage[^\n]+\}\s*catch\(e\)\s*\{\}\s*\}\s*\}', re.MULTILINE | re.DOTALL)
        modified = bad_tail.sub('}', modified)

        if modified != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified)
            count += 1

print(f"Fixed syntax errors in {count} HTML files.")
