from transformers import pipeline
from typing import List
import re

class RAPTORProcessor:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.chunk_size = 512
        
    def _chunk_code(self, code: str) -> List[str]:
        chunks = re.split(r'(?:\n{2,}|;|})', code)
        final_chunks = []
        for chunk in chunks:
            if len(chunk) > self.chunk_size:
                tokens = chunk.split()
                for i in range(0, len(tokens), self.chunk_size):
                    final_chunks.append(' '.join(tokens[i:i+self.chunk_size]))
            else:
                final_chunks.append(chunk)
        return final_chunks
    
    def process(self, code: str) -> dict:
        chunks = self._chunk_code(code)
        level1 = [self.summarizer(c, max_length=150)[0]['summary_text'] for c in chunks]
        level2 = self.summarizer(' '.join(level1), max_length=300)[0]['summary_text']
        return {"summary": level2, "chunks": chunks}