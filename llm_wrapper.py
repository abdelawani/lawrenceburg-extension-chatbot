from langchain.chat_models import ChatOpenAI
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

# temperature=0 for deterministic, model_name can be "gpt-4" if you have access
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

def get_answer(docs, query):
    chain = load_qa_with_sources_chain(llm, chain_type="stuff")
    return chain.run(input_documents=docs, question=query)
