import sys
import os

def verify():
    print("Verifying Project 2: AI FAQ Chatbot...")
    try:
        import streamlit as st
        from chatbot_engine import FAQChatbot
        
        # Initialize
        data_path = os.path.join(os.path.dirname(__file__), "faq_data.json")
        chatbot = FAQChatbot(data_path)
        
        # Test exact match
        resp = chatbot.get_response("What is Artificial Intelligence (AI)?")
        assert not resp["is_fallback"]
        assert resp["confidence"] > 0.9
        
        # Test fuzzy match
        resp = chatbot.get_response("tell me about machine learning")
        assert not resp["is_fallback"]
        assert resp["confidence"] > 0.4
        
        # Test fallback
        resp = chatbot.get_response("what is the weather in Paris today?")
        assert resp["is_fallback"]
        
        print("[SUCCESS] Project 2 verification successful!")
    except Exception as e:
        print(f"[FAILED] Project 2 verification failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify()
