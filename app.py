import streamlit as st
import os
from PIL import Image
import glob

st.set_page_config(
    page_title="Happy Birthday! 🎉",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for blue theme
st.markdown("""
<style>
    :root {
        --primary-blue: #1e3a8a;
        --light-blue: #3b82f6;
        --sky-blue: #87ceeb;
        --white: #ffffff;
    }
    
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        color: #ffffff;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e40af 100%);
    }
    
    .main {
        padding: 0;
    }
    
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 60px 20px;
        text-align: center;
        border-bottom: 4px solid #87ceeb;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.4);
        margin: -20px -20px 40px -20px;
    }
    
    .header-title {
        font-size: 4em;
        font-weight: 900;
        background: linear-gradient(135deg, #87ceeb, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 10px;
        text-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    
    .header-subtitle {
        font-size: 1.5em;
        color: #e0f2fe;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    .section-title {
        font-size: 2.5em;
        color: #87ceeb;
        font-weight: 800;
        margin: 40px 0 30px 0;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 15px;
    }
    
    .photo-card {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 2px solid #3b82f6;
        background: #1e40af;
    }
    
    .photo-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 15px 40px rgba(135, 206, 235, 0.6);
        border-color: #87ceeb;
    }
    
    .photo-card img {
        width: 100%;
        height: 300px;
        object-fit: cover;
        display: block;
    }
    
    .memory-card {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        border-left: 5px solid #87ceeb;
        padding: 25px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.3);
        font-size: 1.1em;
        line-height: 1.8;
        color: #e0f2fe;
    }
    
    .memory-author {
        color: #87ceeb;
        font-weight: bold;
        font-size: 1.2em;
        margin-bottom: 10px;
    }
    
    .divider {
        height: 3px;
        background: linear-gradient(to right, #3b82f6, #87ceeb, #3b82f6);
        margin: 50px 0;
        border-radius: 2px;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #87ceeb !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <div class="header-title">🎉 HAPPY BIRTHDAY! 🎂</div>
    <div class="header-subtitle">✨ A celebration of you, from your besties ✨</div>
</div>
""", unsafe_allow_html=True)

# Navigation
tab1, tab2, tab3 = st.tabs(["📸 GALLERY", "💌 MESSAGES", "✨ MEMORIES"])

# Load images - try multiple possible locations
image_paths = []
possible_dirs = ["images", "./images", "images/"]

for directory in possible_dirs:
    if os.path.isdir(directory):
        images = sorted(glob.glob(os.path.join(directory, "*.jpg")) + 
                       glob.glob(os.path.join(directory, "*.jpeg")) + 
                       glob.glob(os.path.join(directory, "*.png")))
        if images:
            image_paths = images
            break

# ==================== TAB 1: GALLERY ====================
with tab1:
    st.markdown('<div class="section-title">Photo Gallery</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center; font-size: 1.2em; color: #e0f2fe; margin-bottom: 30px;'>
    Scroll through these beautiful moments we've shared together 💙
    </p>
    """, unsafe_allow_html=True)
    
    if len(image_paths) > 0:
        # Create columns for responsive grid
        cols = st.columns(3)
        
        for idx, img_path in enumerate(image_paths):
            col = cols[idx % 3]
            with col:
                try:
                    img = Image.open(img_path)
                    st.markdown('<div class="photo-card">', unsafe_allow_html=True)
                    st.image(img, use_column_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Could not load image: {os.path.basename(img_path)}")
    else:
        st.markdown("""
        <div style='text-align: center; padding: 50px; color: #87ceeb;'>
            <p style='font-size: 1.2em;'>📸 Photos will appear here once uploaded!</p>
            <p style='color: #e0f2fe; margin-top: 10px;'>Make sure the images folder contains your photos.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ==================== TAB 2: MESSAGES ====================
with tab2:
    st.markdown('<div class="section-title">Birthday Messages</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center; font-size: 1.2em; color: #e0f2fe; margin-bottom: 30px;'>
    Messages from people who care about you 💙
    </p>
    """, unsafe_allow_html=True)
    
    # Message 1
    st.markdown("""
    <div class="memory-card">
        <div class="memory-author">👑 From Your Bestie</div>
        <p>Add your heartfelt birthday message here! Talk about your favorite memories, inside jokes, what you love about them, and why they're special to you.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Message 2
    st.markdown("""
    <div class="memory-card">
        <div class="memory-author">💫 Friend Message</div>
        <p>Add messages from other friends here! Each message can be unique and personal.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Message 3
    st.markdown("""
    <div class="memory-card">
        <div class="memory-author">⭐ Another Special Message</div>
        <p>Keep adding as many messages as you'd like. Make this a celebration from everyone who loves them!</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: MEMORIES ====================
with tab3:
    st.markdown('<div class="section-title">Shared Memories</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center; font-size: 1.2em; color: #e0f2fe; margin-bottom: 30px;'>
    The moments that make our friendship unforgettable 💙
    </p>
    """, unsafe_allow_html=True)
    
    # Memory 1
    st.markdown("""
    <div class="memory-card">
        <div class="memory-author">📝 Memory #1</div>
        <p>Add a cherished memory here! Maybe the first time you met, a funny moment you shared, a road trip, late-night conversations, or just a random funny thing they did.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Memory 2
    st.markdown("""
    <div class="memory-card">
        <div class="memory-author">📝 Memory #2</div>
        <p>Another special moment! Share what makes your friendship unique and why you're grateful to have them in your life.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Memory 3
    st.markdown("""
    <div class="memory-card">
        <div class="memory-author">📝 Memory #3</div>
        <p>Keep the memories coming! This is her gift — a scrapbook of all the good times and why she matters so much.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 40px; color: #87ceeb; font-size: 1.1em;'>
    <p>💙 Made with love for someone special 💙</p>
    <p style='color: #e0f2fe; font-size: 0.9em; margin-top: 20px;'>This app is your gift — a celebration of your friendship!</p>
</div>
""", unsafe_allow_html=True)
