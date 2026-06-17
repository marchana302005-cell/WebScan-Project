from flask import Flask, render_template, request, send_file
from scanner import scan_url, scan_payloads
from crawler import crawl
from payloads import ALL_PAYLOADS
import datetime
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        url = request.form['url']
        links, forms = crawl(url)
        
        for form in forms:
            vulns = scan_payloads(ALL_PAYLOADS)
            
            # Add severity levels
            for v in vulns:
                if 'SQLi' in v['type']:
                    v['severity'] = 'CRITICAL'
                elif 'XSS' in v['type']:
                    v['severity'] = 'HIGH'
                else:
                    v['severity'] = 'MEDIUM'
            
            results.append({
                'action': form['action'],
                'inputs': form['inputs'],
                'vulns': vulns
            })
        
        # Save report to file
        with open('report.html', 'w', encoding='utf-8') as f:
            f.write(f"<h1>Vuln Scanner Report - {datetime.datetime.now()}</h1>")
            f.write(f"<h2>Target: {url}</h2>")
            for r in results:
                f.write(f"<h3>Form: {r['action']}</h3>")
                f.write(f"<p>Inputs: {r['inputs']}</p>")
                for v in r['vulns']:
                    f.write(f"<p style='color:red'>[{v['severity']}] {v['type']}: {v['payload']}</p>")
    
    return render_template('index.html', results=results)

@app.route('/download')
def download_report():
    return send_file('report.html', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)