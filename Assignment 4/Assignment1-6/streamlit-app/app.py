import streamlit as st
import random

# ---------- Quotes ----------
quotes = [
    "✨ Believe in yourself and all that you are.",
    "🔥 Push yourself, because no one else is going to do it for you.",
    "💡 Success doesn’t just find you. You have to go out and get it.",
    "🚀 The harder you work for something, the greater you’ll feel when you achieve it.",
    "🎯 Dream it. Wish it. Do it.",
    "⚡ Sometimes later becomes never. Do it now.",
    "🌈 Stay positive, work hard, make it happen."
]

# ---------- Page Config ----------
st.set_page_config(page_title="Daily Motivation", layout="centered")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background-image: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding-top: 50px;
    }
    .quote-box {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 30px;
        margin-top: 30px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        transition: 0.4s ease;
    }
    .quote-text {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    .footer {
        margin-top: 50px;
        font-size: 14px;
        color: #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- App Title ----------
st.markdown("<h1 style='text-align: center; color: white;'>🌟 Daily Motivation</h1>", unsafe_allow_html=True)

# ---------- Get Quote Button ----------
if st.button("💫 Get Inspired", use_container_width=True):
    quote = random.choice(quotes)
    st.markdown(f"""
        <div class="main-container">
            <div class="quote-box">
                <div class="quote-text">“{quote}”</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="main-container">
            <div class="quote-box">
                <div class="quote-text">“Click the button to receive your daily inspiration!”</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("<div class='footer'>Made with ❤️ by Farrukh Salim</div>", unsafe_allow_html=True)