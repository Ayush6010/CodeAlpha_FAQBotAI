# Project 2: AI FAQ Chatbot

An intelligent NLP-powered FAQ support assistant built with **Python**, **Streamlit** ,and **scikit-learn**. The chatbot leverages TF-IDF Vectorization and Cosine Similarity to understand user queries, identify the most relevant questions from a knowledge base, and provide accurate responses in real time.
---
## Live Application

**Deployment Link**:

https://codealphafaqbotai.streamlit.app/

Experience an intelligent FAQ chatbot that combines Natural Language Processing and Machine Learning techniques to deliver fast, accurate, and user-friendly support responses directly from your browser.
## Features

- **Modern Chat Interface**:
- Built using Streamlit's native `st.chat_message` and `st.chat_input` components.
Provides a clean, responsive, and user-friendly conversational experience.
- **NLP Vectorization Engine**:Converts user queries and knowledge base questions into **TF-IDF vectors**.
Utilizes both word-level and bigram tokenization for improved contextual understanding.
Enhances matching accuracy across diverse user inputs.
- **Cosine Similarity Matching**: Calculates similarity scores between user queries and stored FAQ entries.
Retrieves the most relevant answer based on semantic similarity.
Delivers fast and efficient response generation.
- **Adjustable Threshold Slider**: Interactive sidebar slider allows dynamic adjustment of matching strictness.
Helps control chatbot sensitivity for broader or more precise responses.
Updates behavior instantly without restarting the application.
- **Confidence Metric**: Displays similarity confidence scores alongside chatbot responses.
Provides transparency into how closely a query matches the knowledge base.
Helps users evaluate response reliability.
- **Interactive Knowledge Base Explorer**: Browse available FAQ categories directly from the sidebar.
Explore supported topics and sample questions.
Improves discoverability and user engagement.
- **Smart Fallback Handling**: Gracefully handles unmatched or low-confidence queries.
Suggests alternative topics and available categories.
Ensures a smooth user experience even when no strong match exists.
- **Chat History Management**: Maintains conversation history during the active session.
Includes a dedicated Clear Chat History button for quick resets.
Enhances usability during repeated testing and demonstrations.

---

## Installation & Running

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the application:
   ```bash
   streamlit run app.py
   ```
