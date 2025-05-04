import os
import streamlit as st
from loader import load_web_content
from rag_engine import build_vector_store, retrieve_documents
from llm_wrapper import get_answer

st.set_page_config(page_title="Lawrenceburg Extension Bot")
st.title("🌱 Lawrenceburg Extension Office Chatbot")
st.markdown("Ask me anything about Lawrence County Extension services!")

# ——————————————————————————————
# Load & index (this runs once per session)
@st.cache_resource(show_spinner=False)
def init_knowledge_base():
    urls = [
        "https://lawrencecountytn.gov/government/departments/agricultural-extension/",
        "https://lawrencecountytn.gov/",
        "https://utia.tennessee.edu/",
        "https://www.tnstate.edu/",
        "https://www.tn.gov/",
        "https://www.tn.gov/agriculture.html"
    ]
    docs = load_web_content(urls)
    return build_vector_store(docs)

vector_db = init_knowledge_base()

# ——————————————————————————————
# Query loop
query = st.text_input("❓ What do you want to know?")
if query:
    with st.spinner("🔎 Searching..."):
        docs = retrieve_documents(vector_db, query)
        answer = get_answer(docs, query)
    st.markdown("### 🤖 Answer")
    st.write(answer)
    # Optionally show sources:
    st.markdown("**Sources:**")
    for d in docs:
        if d.metadata.get("source"):
            st.write(f"- {d.metadata['source']}")
