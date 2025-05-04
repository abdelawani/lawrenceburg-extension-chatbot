import streamlit as st
from loader import load_web_content
from rag_engine import build_vector_store, retrieve_documents
from llm_wrapper import get_answer

st.title("Lawrenceburg Extension Office Chatbot 🤖")
st.markdown("Ask me anything about Lawrence County Extension services!")

# Load and index documents (cache this if needed)
with st.spinner("Loading knowledge base..."):
    urls = [
        "https://lawrencecountytn.gov/government/departments/agricultural-extension/",
        "https://utia.tennessee.edu/",
        "https://www.tn.gov/agriculture.html"
    ]
    docs = load_web_content(urls)
    vector_db = build_vector_store(docs)

# User input
query = st.text_input("Ask a question:")

if query:
    with st.spinner("Searching..."):
        docs = retrieve_documents(vector_db, query)
        answer = get_answer(docs, query)
        st.markdown("### Answer:")
        st.write(answer)
