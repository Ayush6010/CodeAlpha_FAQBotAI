import streamlit as st
import os
from chatbot_engine import FAQChatbot

# Page configuration
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for styling chat window and visual accents
def inject_custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Header Styling */
    .chat-header {
        text-align: center;
        padding: 2rem 1.5rem;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(168, 85, 247, 0.08) 100%);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
    }
    .chat-title {
        font-size: 2.6rem;
        font-weight: 700;
        background: linear-gradient(90deg, #A855F7 0%, #6366F1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .chat-subtitle {
        color: #94A3B8;
        font-size: 1.1rem;
        font-weight: 400;
    }
    
    /* Confidence Badge styling */
    .confidence-badge {
        display: inline-flex;
        align-items: center;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        background-color: rgba(99, 102, 241, 0.15);
        color: #818CF8;
        border: 1px solid rgba(99, 102, 241, 0.3);
        margin-top: 5px;
    }
    .confidence-badge-low {
        background-color: rgba(239, 68, 68, 0.15);
        color: #F87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# Cache chatbot engine loader
@st.cache_resource
def load_chatbot():
    data_path = os.path.join(os.path.dirname(__file__), "faq_data.json")
    return FAQChatbot(data_path)

def main():
    inject_custom_css()
    
    # Render header
    st.markdown("""
    <div class="chat-header">
        <h1 class="chat-title">🤖 AI FAQ Chatbot</h1>
        <p class="chat-subtitle">NLP-powered support agent using TF-IDF matching and Cosine Similarity</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load NLP Chatbot
    try:
        chatbot = load_chatbot()
    except Exception as e:
        st.error(f"Failed to initialize Chatbot Engine: {e}")
        return

    # Sidebar controls
    with st.sidebar:
        st.markdown("### ⚙️ Engine Parameters")
        threshold = st.slider(
            "Matching Confidence Threshold",
            min_value=0.1,
            max_value=1.0,
            value=0.3,
            step=0.05,
            help="Set the minimum cosine similarity required to match a question. Lower values are more lenient; higher values are more strict."
        )
        
        st.markdown("---")
        st.markdown("### 📚 FAQ Knowledge Base")
        
        # Group questions by category for sidebar explorer
        faq_by_category = {}
        for item in chatbot.faq_data:
            cat = item['category']
            faq_by_category.setdefault(cat, []).append(item['question'])
            
        for cat, qs in faq_by_category.items():
            with st.expander(f"📁 {cat} ({len(qs)})"):
                for q in qs:
                    st.caption(f"• {q}")
                    
        st.markdown("---")
        if st.button("🧹 Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

    # Chat history session state initialization
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I am your AI Support Assistant. Ask me anything about Artificial Intelligence, Machine Learning, Streamlit, or your internship submission!", "confidence": 1.0, "is_fallback": False}
        ]

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            # If assistant message and has metadata, show confidence score
            if msg["role"] == "assistant" and msg.get("confidence") is not None and not msg.get("is_init", False):
                score = msg["confidence"]
                if msg.get("is_fallback", False):
                    st.markdown(f'<span class="confidence-badge confidence-badge-low">Match Score: {score:.1%} (Below Threshold)</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<span class="confidence-badge">Confidence Match: {score:.1%}</span>', unsafe_allow_html=True)

    # Chat input
    if user_query := st.chat_input("Ask a question..."):
        # Display user question
        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        # Get AI response
        with st.spinner("Analyzing question query..."):
            response = chatbot.get_response(user_query, threshold=threshold)
            
        # Display assistant answer
        with st.chat_message("assistant"):
            st.markdown(response["answer"])
            if response["is_fallback"]:
                st.markdown(f'<span class="confidence-badge confidence-badge-low">Match Score: {response["confidence"]:.1%} (Below Threshold)</span>', unsafe_allow_html=True)
            else:
                st.markdown(f'<span class="confidence-badge">Confidence Match: {response["confidence"]:.1%}</span>', unsafe_allow_html=True)
                
        # Store response in session state
        st.session_state.messages.append({
            "role": "assistant",
            "content": response["answer"],
            "confidence": response["confidence"],
            "is_fallback": response["is_fallback"]
        })
        st.rerun()

# Set initial message properties
if len(st.session_state.get('messages', [])) > 0:
    st.session_state.messages[0]['is_init'] = True

if __name__ == "__main__":
    main()
