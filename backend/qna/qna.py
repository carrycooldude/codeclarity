from transformers import pipeline
from raptor_utils import summarize_code

def answer_question(code, question):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(code, max_length=50, min_length=25, do_sample=False)
    return summary[0]["summary_text"]