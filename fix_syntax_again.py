import glob

def fix_syntax():
    html_files = glob.glob("simulations_kannada/*.html")
    count = 0
    
    for fp in html_files:
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check if the syntax is broken (missing bracket before document.addEventListener)
        target = "        }\n\n    \n    document.addEventListener('click', function(e) {"
        
        if target in content:
            new_content = content.replace(target, "        }\n    }\n\n    document.addEventListener('click', function(e) {")
            with open(fp, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            continue
            
        # Try various whitespace variations
        import re
        if re.search(r'\}\s*document\.addEventListener\(\'click\', function\(e\) \{', content):
            new_content = re.sub(
                r'(\})\s*document\.addEventListener\(\'click\', function\(e\) \{', 
                r'\1\n    }\n\n    document.addEventListener(\'click\', function(e) {', 
                content
            )
            with open(fp, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            
    print(f"Fixed {count} files.")

if __name__ == "__main__":
    fix_syntax()
