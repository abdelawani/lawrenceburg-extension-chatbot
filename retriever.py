from scraper import scrape_pages
from indexer import Indexer
from generator import Generator

URLS = [
    "https://lawrencecountytn.gov/government/departments/agricultural-extension/",
    "https://lawrencecountytn.gov/",
    "https://utia.tennessee.edu/",
    "https://www.tnstate.edu/",
    "https://www.tn.gov/",
    "https://www.tn.gov/agriculture.html"
]

class QA:
    def __init__(self):
        docs = scrape_pages(URLS)
        self.indexer = Indexer()
        self.indexer.build(docs)
        self.generator = Generator()
        # store raw texts by source for context assembly
        self.doc_map = {d["source"]: d["text"] for d in docs}

    def ask(self, question):
        sources, scores = self.indexer.query(question, top_k=3)
        # concatenate top‑3 pages as context
        context = "\n\n".join(self.doc_map[src] for src in sources)
        answer = self.generator.answer(context, question)
        return answer, sources
