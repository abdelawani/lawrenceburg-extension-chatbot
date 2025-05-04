from langchain.document_loaders import WebBaseLoader

def load_web_content(urls):
    loader = WebBaseLoader(urls)
    return loader.load()
