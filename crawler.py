import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl(url):
    links = set()
    forms = []

    try:
        # Handle local files vs web URLs
        if url.startswith("file://"):
            with open(url.replace("file://", ""), 'r', encoding='utf-8') as f:
                html = f.read()
        else:
            r = requests.get(url, timeout=10)
            html = r.text

        soup = BeautifulSoup(html, 'html.parser')

        # Find all links
        for a in soup.find_all('a', href=True):
            href = a['href']
            if url.startswith("file://"):
                # For local files, just join path
                full_url = url.rsplit('/', 1)[0] + '/' + href
            else:
                full_url = urljoin(url, href)

            # Only keep links from same domain/site
            if url.startswith("file://") or urlparse(full_url).netloc == urlparse(url).netloc:
                links.add(full_url)

        # Find all forms
        for form in soup.find_all('form'):
            action = form.get('action', '')
            if url.startswith("file://") and action:
                action_url = url.rsplit('/', 1)[0] + '/' + action
            else:
                action_url = urljoin(url, action)

            forms.append({
                'action': action_url,
                'method': form.get('method', 'get').lower(),
                'inputs': [i.get('name') for i in form.find_all('input') if i.get('name')]
            })

    except Exception as e:
        print(f"Error: {e}")

    return list(links), forms

# TEST CODE - runs only when you do: python crawler.py
if __name__ == "__main__":
    test_url = "file://C:/Users/march/OneDrive/Desktop/vuln_scanner/test.html"
    print(f"Testing crawler on: local test.html")

    links, forms = crawl(test_url)

    print(f"\nFound {len(links)} links:")
    for l in links:
        print(f" - {l}")

    print(f"\nFound {len(forms)} forms:")
    for f in forms:
        print(f" - Action: {f['action']} | Method: {f['method']} | Inputs: {f['inputs']}")