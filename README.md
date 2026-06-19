# Project 2: AI FAQ Chatbot

An NLP-based FAQ support agent built with **Python**, **Streamlit**, and **scikit-learn** that uses TF-IDF Vectorization and Cosine Similarity to find matches for user questions.

---

## Features

- **Modern Chat Interface**: Smooth experience using Streamlit's native `st.chat_message` and `st.chat_input` widgets.
- **NLP Vectorization Engine**: Converts sentences to TF-IDF vectors using word and bigram tokens.
- **Cosine Similarity Matching**: Computes similarity scores to retrieve the best answer.
- **Adjustable Threshold Slider**: Adjust the match strictness in real time.
- **Confidence Metric**: Displays matching confidence scores (similarities) alongside the responses.
- **Interactive Knowledge Base Explorer**: Explore available questions grouped by category in the sidebar.
- **Smart Fallback Handling**: Elegant replies and topics list when queries fall below the threshold.
- **History Control**: Easily wipe out session logs with the "Clear Chat History" button.

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
