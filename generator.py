from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL = "google/flan-t5-base"

class Generator:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)

    def answer(self, context, question, max_length=256):
        prompt = "Context:\n" + context + "\n\nQuestion: " + question + "\nAnswer:"
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
