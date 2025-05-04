import gradio as gr
from retriever import QA

qa = QA()

def chat(query):
    answer, sources = qa.ask(query)
    src_list = "\n".join(f"- {s}" for s in sources)
    return answer + "\n\n**Sources:**\n" + src_list

with gr.Blocks() as demo:
    gr.Markdown("# 🌱 Lawrenceburg Extension Chatbot")
    inp = gr.Textbox(placeholder="Ask about Extension services...", label="Your question")
    out = gr.Markdown()
    btn = gr.Button("Send")
    btn.click(fn=chat, inputs=inp, outputs=out)

if __name__ == "__main__":
    demo.launch()
