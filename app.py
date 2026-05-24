import streamlit as st
import os
from PIL import Image
import glob
import base64

st.set_page_config(
    page_title="Happy 21st Birthday! 🎉",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - clean blue theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e40af 100%);
    }
    
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 50px 20px;
        text-align: center;
        border-bottom: 4px solid #87ceeb;
        margin: -20px -20px 30px -20px;
        border-radius: 0 0 20px 20px;
    }
    
    .header-title {
        font-size: 3.5em;
        font-weight: 900;
        color: #87ceeb;
        margin: 10px 0;
    }
    
    .header-subtitle {
        font-size: 1.3em;
        color: #e0f2fe;
    }
    
    .section-title {
        font-size: 2.2em;
        color: #87ceeb;
        font-weight: 800;
        margin: 30px 0 20px 0;
        text-align: center;
    }
    
    .message-box {
        background: linear-gradient(135deg, rgba(30, 64, 175, 0.8) 0%, rgba(59, 130, 246, 0.6) 100%);
        border-left: 6px solid #87ceeb;
        padding: 30px;
        border-radius: 12px;
        margin: 20px 0;
        color: #e0f2fe;
        font-size: 1.05em;
        line-height: 1.9;
    }
    
    .author {
        color: #87ceeb;
        font-weight: bold;
        font-size: 1.25em;
        margin-bottom: 15px;
    }
    
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    
    .gallery-item {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
        transition: all 0.4s ease;
        border: 3px solid #3b82f6;
        cursor: pointer;
    }
    
    .gallery-item:hover {
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 15px 40px rgba(135, 206, 235, 0.7);
        border-color: #87ceeb;
    }
    
    .gallery-item img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# Add calm background music (royalty-free)
st.markdown("""
<audio autoplay loop volume="0.3" style="display:none;">
    <source src="https://assets.mixkit.co/active_storage/musics/577-3dfe6ae8-5b39-4f9e-bae9-5bfeae5df1c4.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <div class="header-title">🎉 LOOK WHO'S 21! 🎂</div>
    <div class="header-subtitle">✨ A celebration of you, from your bestie ✨</div>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["💌 MESSAGE", "📸 GALLERY", "✨ MEMORIES"])

# Load images from images folder
image_paths = []
if os.path.isdir("images"):
    images = glob.glob("images/*")
    image_paths = [img for img in images if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    image_paths.sort()

# ==================== TAB 1: MESSAGE ====================
with tab1:
    st.markdown('<h2 class="section-title">A Message For You</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="message-box">', unsafe_allow_html=True)
    st.markdown('<div class="author">💙 From Your Bestie</div>', unsafe_allow_html=True)
    
    st.write("Look who's no longer a teen anymore… YES that is my bestieeee!!")
    st.write("")
    st.markdown("**HAPPY 21ST BIRTHDAY!**")
    st.write("")
    st.write("Gosh, where do I even start? From the very first day we spoke in 2018 to now, we have definitely come such a long way together.")
    st.write("")
    st.write("From that sweet 12-year-old girl I knew back then, to the amazing woman and friend you are today — you have truly outshined yourself. You've grown into someone I deeply admire and respect. I am immensely grateful and thankful for our friendship over these years and how we've managed to stay really close despite the distance.")
    st.write("")
    st.write("All the amazing memories we've shared, and missing each other after every call, have brought us closer with time. You are nothing but the best friend I could ever ask for. I miss you the most, Nesi. 💙")
    st.write("")
    st.write("We only meet a few times every year when you come to Sri Lanka, but I truly value those little moments we spend together. It's only then that I feel like I'm actually with someone I genuinely love as a friend — someone I truly care for. Those moments are everything to me.")
    st.write("")
    st.write("I hope we always remain as close friends and be there for each other no matter what life throws our way. You ALWAYS know that I'm just one call away. For any problem, any issue, any time you need my opinion or just someone to listen — I'm always there for you. And I know you're there for me too. That means the world to me.")
    st.write("")
    st.write("I'm so happy that you're living the life you always wanted, surrounded by people who love and care for you. But don't ever forget the girl back home! 😂 I'll always be counting down the days until we meet again — hopefully in December or January. I'm eagerly waiting to see my best friend again.")
    st.write("")
    st.write("I hope this year is definitely one for the books, and welcome to adulthood! I wish that everything you hope and pray for comes true, because you deserve absolutely everything and so much more. You're going to do amazing things, and I can't wait to see you shine even brighter.")
    st.write("")
    st.markdown("**I LOVE YOU SO MUCH, AND I REALLY REALLY WISH I WAS THERE FOR YOUR 21ST! 💙💙💙**")
    st.write("")
    st.markdown('<p style="color: #87ceeb; margin-top: 20px; font-size: 0.95em;">Here\'s to new adventures, unforgettable memories, and a friendship that will last forever.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 2: GALLERY ====================
with tab2:
    st.markdown('<h2 class="section-title">Photo Gallery</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #e0f2fe; font-size: 1.1em;">Hover over photos to see them shine ✨</p>', unsafe_allow_html=True)
    
    if len(image_paths) > 0:
        cols = st.columns(3)
        for idx, img_path in enumerate(image_paths):
            col = cols[idx % 3]
            with col:
                try:
                    img = Image.open(img_path)
                    st.image(img, use_column_width=True, caption=f"Memory {idx+1}")
                except:
                    st.warning(f"Could not load image")
    else:
        st.markdown("""
        <div style='text-align: center; padding: 60px 20px; color: #87ceeb;'>
            <h3>📸 Photos Coming Soon!</h3>
            <p style='font-size: 1.1em;'>Make sure images are uploaded to the images/ folder</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 3: MEMORIES ====================
with tab3:
    st.markdown('<h2 class="section-title">Our Memories Together</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="message-box">', unsafe_allow_html=True)
    st.markdown('<div class="author">📝 2018 - When It All Began</div>', unsafe_allow_html=True)
    st.write("That very first conversation in 2018 changed everything. We didn't know then that we'd become as close as we are now. From that first moment, there was just something special — a connection that felt natural and real.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="message-box">', unsafe_allow_html=True)
    st.markdown('<div class="author">💙 The Distance & The Bond</div>', unsafe_allow_html=True)
    st.write("Distance has never been able to break what we have. Every call, every message, every time you visit Sri Lanka — those moments remind me why our friendship is so precious. We've learned that real friendship doesn't need constant physical presence; it thrives on genuine care and effort. And girl, you've always put in the effort.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="message-box">', unsafe_allow_html=True)
    st.markdown('<div class="author">🎂 Growing Up Together</div>', unsafe_allow_html=True)
    st.write("From 12-year-old you to 21-year-old you — I've had the privilege of watching you grow into an incredible woman. I've seen you overcome challenges, chase your dreams, and become someone you're genuinely proud of. And honestly, I'm so incredibly proud of you too.")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; padding: 30px; color: #87ceeb; margin-top: 40px; border-top: 2px solid #3b82f6;'>
    <p style='font-size: 1.1em;'>💙 Made with love for my best friend 💙</p>
</div>
""", unsafe_allow_html=True)
