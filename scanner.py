import re
from crawler import crawl
from payloads import ALL_PAYLOADS

XSS_PATTERNS = [
    r'<script[^>]*>.*?</script>',
    r'javascript:',
    r'on\w+\s*=',
    r'<img[^>]*onerror',
    r'<svg[^>]*onload',
]

SQLI_PATTERNS = [
    r"'?\s*(OR|AND)\s*'?\d+'?='?\d+",
    r"'\s*OR\s+'[^']+'='\s*'",
    r"'\s*--",
    r"';\s*DROP\s+TABLE",
    r"UNION\s+SELECT",
]

def scan_payloads(payloads_list):
    results = []
    for payload in payloads_list:
        vulns = []
        for pattern in XSS_PATTERNS:
            if re.search(pattern, payload, re.IGNORECASE):
                vulns.append("XSS")
                break
        for pattern in SQLI_PATTERNS:
            if re.search(pattern, payload, re.IGNORECASE):
                vulns.append("SQLi")
                break
        if vulns:
            results.append({"payload": payload, "type": ", ".join(vulns)})
    return results

def scan_url(url):
    print(f"\n[SCAN] Crawling: {url}")
    links, forms = crawl(url)
    
    print(f"[+] Found {len(links)} links")
    print(f"[+] Found {len(forms)} forms\n")
    
    for i, form in enumerate(forms, 1):
        print(f"--- Testing Form {i} ---")
        print(f"Action: {form['action']}")
        print(f"Inputs: {form['inputs']}")
        
        findings = scan_payloads(ALL_PAYLOADS)
        
        if findings:
            print(f"[DANGER] {len(findings)} vulnerabilities detected:")
            for f in findings:
                print(f"  - {f['type']}: {f['payload']}")
        else:
            print("[SAFE] No vulnerabilities detected")
        print()

if __name__ == "__main__":
    test_url = "file://C:/Users/march/OneDrive/Desktop/vuln_scanner/test.html"
    scan_url(test_url)