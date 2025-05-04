from langchain.document_loaders import RequestsLoader
from langchain.document_transformers import Html2TextTransformer

def load_web_content(urls):
    loader = RequestsLoader(urls)
    docs = loader.load()

    # Convert raw HTML to readable text
    transformer = Html2TextTransformer()
    return transformer.transform_documents(docs)
