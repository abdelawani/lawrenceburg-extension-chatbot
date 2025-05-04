import requests
from bs4 import BeautifulSoup

def scrape_pages(urls):
    docs = []
    headers = {"User-Agent": "LawrenceburgBot/1.0"}
    for url in urls:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script","style","nav","footer","header"]):
            tag.decompose()
        text = soup.get_text(separator="\n")
        docs.append({"text": text, "source": url})
    return docs
