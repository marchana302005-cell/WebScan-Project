### **Project Name**
Web Application Vulnerability Scanner



### **Objective**
Build a scanner to detect common web application vulnerabilities like **XSS,SQL Injection and CSRF** using Python. 



### **Tools & Technologies**
- **Python** - Core programming language
- **Requests** - Send HTTP requests for crawling + form submission
- **BeautifulSoup** - Parse HTML to find links, forms, and input fields
- **Regex `re`** - Pattern matching to detect XSS/SQLi attack success
- **Flask** - Web framework for browser-based UI at `127.0.0.1:5000`
- **OWASP Top 10** - Reference for vulnerability types and payloads



### *📁 Project Structure*
vuln_scanner/
├── app.py          # Flask web server
├── crawler.py      # Finds links + forms
├── scanner.py      # Regex detection logic
├── payloads.py     # XSS + SQLi test payloads
├── templates/
│   └── index.html  # Web UI
└── test.html       # Vulnerable test page



### *What I built:*
Component | Status | What it does
**crawler.py** | Crawls HTML files, finds all links + forms
**payloads.py**  | Stores XSS + SQLi test payloads
**scanner.py**  | Regex engine detects XSS/SQLi patterns
**app.py + http://index.html** | Flask web UI for browser scanning



### **📋 Features**
1. **Auto Crawling**: Finds all links and input forms on target URL
2. **Payload Injection**: Tests XSS + SQLi payloads on every form
3. **Regex Detection**: Identifies attack success patterns in responses
4. **Severity Levels**: Classifies SQLi as `CRITICAL`, XSS as `HIGH`, CSRF as 'Medium'
5. **Web UI**: No command line needed - scan from browser
6. **Report Export**: Download `report.html`. I give as jpeg format( vulnerabilities tested - XSS+SQLI+CSFR) and Report.html.



### **Implementation + Results**
| Step| Implementation | Result |
 **a. Crawl** | Use requests and BeautifulSoup to crawl input fields and URLs 
| `crawler.py` parses all `<a>` links and `<form>` tags with inputs
| `Found 3 links` + `Inputs: ['q'] ['username','password']` ✅ 

 **b. Inject** | Inject payloads for XSS, SQLi, etc., and analyze responses
| `payloads.py` stores 8 test payloads: `<script>alert()>`, `' OR 1=1--` 
| Payloads injected into `search.php` + `login.php` ✅ 

**c. Detect** | Use regex or pattern matching for vulnerability detection
| `scanner.py` uses regex to check response for `<script>`, `alert()`, `SQL syntax` 
| `[DANGER] XSS detected` + `[DANGER] SQLi detected + CSRF`  ✅ 

 **d. Flask UI** | Create a Flask UI to manage scans and view results
| `app.py + index.html` provides web form to enter URL + Scan button 
| Browser UI working at `127.0.0.1:5000` ✅ 
 
**e. Log** | Log each vulnerability with evidence and severity 
| `report.html` export with timestamp, target URL, severity `CRITICAL/HIGH/Medium` + payload  



### *📸 Sample Output*
Form: search.php
Inputs: ['q']
[CRITICAL] SQLi: ' OR '1'='1
[HIGH] XSS: <script>alert('XSS')</script>
[MEDIUM] CSRF: No CSRF token found



### **Deliverables**
1. **Python-based Scanner**: 4 modules → `crawler.py`, `payloads.py`, `scanner.py`, `app.py`
2. **Web Interface**: Flask app with URL input, Scan button, and results display
3. **Detailed Reports**: Auto-generated `report.html` with timestamp, target URL, form details, vulnerability type, severity level, and exact payload used
4. **Demo Proof**: Screenshot showing `[DANGER] 8 vulnerabilities found` on test page.





