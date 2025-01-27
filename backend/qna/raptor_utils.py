# raptor_utils.py
from transformers import pipeline
from typing import List

class RAPTORSummarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        
    def chunk_code(self, code: str, chunk_size: int = 512) -> List[str]:
        """Split code into chunks for hierarchical summarization."""
        tokens = code.split()
        return [' '.join(tokens[i:i+chunk_size]) for i in range(0, len(tokens), chunk_size)]
    
    def summarize(self, code: str) -> str:
        """Generate hierarchical summaries using RAPTOR-like approach."""
        chunks = self.chunk_code(code)
        
        # Level 1: Summarize each chunk
        chunk_summaries = [self.summarizer(chunk, max_length=50, min_length=25)[0]["summary_text"] 
                          for chunk in chunks]
        
        # Level 2: Summarize combined chunk summaries
        combined = " ".join(chunk_summaries)
        final_summary = self.summarizer(combined, max_length=100, min_length=50)[0]["summary_text"]
        
        return final_summary