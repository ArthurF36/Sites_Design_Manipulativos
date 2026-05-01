import requests
from bs4 import BeautifulSoup

def obter_html(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(["script", "style", "meta", "noscript", "link"]):
            script_or_style.decompose()
            
        return str(soup.body)[:20000]
        
    except Exception as e:
        print(f"[ERRO] Falha ao acessar {url}: {e}")
        return None