import json
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    # Lowercase, clean punctuation, normalize whitespace
    text = text.lower()
    text = re.sub(r'[^\w\s\?]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

class FAQChatbot:
    def __init__(self, data_path):
        # Load FAQ data
        with open(data_path, 'r', encoding='utf-8') as f:
            self.faq_data = json.load(f)
            
        # Store questions and answers
        self.questions = [item['question'] for item in self.faq_data]
        
        # Initialize and train vectorizer on dataset questions
        self.vectorizer = TfidfVectorizer(
            preprocessor=preprocess_text,
            stop_words='english',
            ngram_range=(1, 2)  # Use word and bigram tokens for better matching
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(self.questions)

    def get_response(self, query, threshold=0.3):
        # Handle empty queries
        if not query.strip():
            return {
                "matched_question": None,
                "answer": "Please ask a question!",
                "category": "None",
                "confidence": 0.0,
                "is_fallback": True
            }

        # Vectorize query
        query_vec = self.vectorizer.transform([query])
        
        # Compute cosine similarity
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        # Get best match
        best_match_idx = np.argmax(similarities)
        best_score = similarities[best_match_idx]
        
        if best_score >= threshold:
            match_data = self.faq_data[best_match_idx]
            return {
                "matched_question": match_data["question"],
                "answer": match_data["answer"],
                "category": match_data["category"],
                "confidence": float(best_score),
                "is_fallback": False
            }
        else:
            return {
                "matched_question": None,
                "answer": "🤖 I'm sorry, I couldn't find a confident match for your question in my knowledge base. "
                          "Could you try rephrasing or asking something else? (e.g. 'What is Streamlit?' or 'Explain YOLO')",
                "category": "Fallback",
                "confidence": float(best_score),
                "is_fallback": True
            }
