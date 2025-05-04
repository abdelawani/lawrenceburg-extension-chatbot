import requests
from bs4 import BeautifulSoup
from langchain.schema import Document

def load_web_content(urls):
    docs = []
    headers = {"User-Agent": "LawrenceburgBot/1.0"}
    for url in urls:
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            # remove scripts/styles
            for tag in soup(["script", "style", "header", "footer", "nav"]):
                tag.decompose()
            text = soup.get_text(separator="\n")
            docs.append(Document(page_content=text, metadata={"source": url}))
        except Exception as e:
            print(f"⚠️ Error loading {url}: {e}")
    return docs
