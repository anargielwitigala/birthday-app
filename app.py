import streamlit as st
import os
from PIL import Image
import glob

st.set_page_config(
    page_title="Happy 21st Birthday! 🎉",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for blue theme with interactive gallery
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
    
    .interactive-gallery {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 25px;
        margin: 30px 0;
    }
    
    .photo-card {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.4);
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        border: 2px solid #3b82f6;
        background: #1e40af;
        cursor: pointer;
        position: relative;
    }
    
    .photo-card:hover {
        transform: translateY(-15px) scale(1.05) rotateY(5deg);
        box-shadow: 0 20px 50px rgba(135, 206, 235, 0.8);
        border-color: #87ceeb;
    }
    
    .photo-card img {
        width: 100%;
        height: 280px;
        object-fit: cover;
        display: block;
        transition: transform 0.4s ease;
    }
    
    .photo-card:hover img {
        transform: scale(1.08);
    }
    
    .photo-overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(to top, rgba(30, 58, 138, 0.9), transparent);
        padding: 20px;
        transform: translateY(100%);
        transition: transform 0.3s ease;
    }
    
    .photo-card:hover .photo-overlay {
        transform: translateY(0);
    }
    
    .message-card {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        border-left: 5px solid #87ceeb;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.3);
        font-size: 1.05em;
        line-height: 1.9;
        color: #e0f2fe;
    }
    
    .memory-author {
        color: #87ceeb;
        font-weight: bold;
        font-size: 1.3em;
        margin-bottom: 15px;
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
    
    .lightbox-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.95);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
        border-radius: 15px;
    }
    
    .lightbox-image {
        max-width: 90%;
        max-height: 90%;
        border-radius: 15px;
        box-shadow: 0 20px 60px rgba(135, 206, 235, 0.8);
    }
</style>
""", unsafe_allow_html=True)

# Play calm background music (peaceful, instrumental)
st.markdown("""
<audio autoplay loop style="width: 0; height: 0; display: none;">
    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <div class="header-title">🎉 LOOK WHO'S 21! 🎂</div>
    <div class="header-subtitle">✨ A celebration of you, from your bestie ✨</div>
</div>
""", unsafe_allow_html=True)

# Navigation
tab1, tab2, tab3 = st.tabs(["💌 MESSAGE", "📸 INTERACTIVE GALLERY", "✨ MEMORIES"])

# Load images
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

# Initialize session state for gallery
if 'selected_image' not in st.session_state:
    st.session_state.selected_image = None

# ==================== TAB 1: MESSAGE ====================
with tab1:
    st.markdown('<div class="section-title">A Message For You</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="message-card">
        <div class="memory-author">💙 From Your Bestie</div>
        <p>
        Look who's no longer a teen anymore… YES that is my bestieeee!! 
        </p>
        
        <p>
        <strong>HAPPY 21ST BIRTHDAY!</strong>
        </p>
        
        <p>
        Gosh, where do I even start? From the very first day we spoke in 2018 to now, we have definitely come such a long way together. 
        </p>
        
        <p>
        From that sweet 12-year-old girl I knew back then, to the amazing woman and friend you are today — you have truly outshined yourself. You've grown into someone I deeply admire and respect. I am immensely grateful and thankful for our friendship over these years and how we've managed to stay really close despite the distance.
        </p>
        
        <p>
        All the amazing memories we've shared, and missing each other after every call, have brought us closer with time. You are nothing but the best friend I could ever ask for. I miss you the most, Nesi. 💙
        </p>
        
        <p>
        We only meet a few times every year when you come to Sri Lanka, but I truly value those little moments we spend together. It's only then that I feel like I'm actually with someone I genuinely love as a friend — someone I truly care for. Those moments are everything to me.
        </p>
        
        <p>
        I hope we always remain as close friends and be there for each other no matter what life throws our way. You ALWAYS know that I'm just one call away. For any problem, any issue, any time you need my opinion or just someone to listen — I'm always there for you. And I know you're there for me too. That means the world to me.
        </p>
        
        <p>
        I'm so happy that you're living the life you always wanted, surrounded by people who love and care for you. But don't ever forget the girl back home! 😂 I'll always be counting down the days until we meet again — hopefully in December or January. I'm eagerly waiting to see my best friend again.
        </p>
        
        <p>
        I hope this year is definitely one for the books, and welcome to adulthood! I wish that everything you hope and pray for comes true, because you deserve absolutely everything and so much more. You're going to do amazing things, and I can't wait to see you shine even brighter.
        </p>
        
        <p>
        <strong>I LOVE YOU SO MUCH, AND I REALLY REALLY WISH I WAS THERE FOR YOUR 21ST! 💙💙💙</strong>
        </p>
        
        <p style="margin-top: 20px; font-size: 0.95em; color: #87ceeb;">
        Here's to new adventures, unforgettable memories, and a friendship that will last forever.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ==================== TAB 2: INTERACTIVE GALLERY ====================
with tab2:
    st.markdown('<div class="section-title">Photo Gallery</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center; font-size: 1.2em; color: #e0f2fe; margin-bottom: 30px;'>
    Hover over photos to see them shine ✨ Click to enlarge 💙
    </p>
    """, unsafe_allow_html=True)
    
    if len(image_paths) > 0:
        # Create interactive gallery columns
        cols = st.columns(3)
        
        for idx, img_path in enumerate(image_paths):
            col = cols[idx % 3]
            with col:
                try:
                    img = Image.open(img_path)
                    # Click to expand
                    if st.button("View", key=f"btn_{idx}", use_container_width=True):
                        st.session_state.selected_image = img_path
                    
                    # Display thumbnail
                    st.markdown(f"""
                    <div class="photo-card">
                        <img src="data:image/png;base64,{img_to_base64(img)}" alt="photo">
                        <div class="photo-overlay">
                            <p style="color: #87ceeb; text-align: center; margin: 0;">Click to view fullscreen</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"Could not load: {os.path.basename(img_path)}")
        
        # Show fullscreen image if selected
        if st.session_state.selected_image:
            col_close, col_img = st.columns([1, 10])
            with col_close:
                if st.button("✕ Close", use_container_width=True):
                    st.session_state.selected_image = None
            with col_img:
                st.image(Image.open(st.session_state.selected_image), use_column_width=True)
    else:
        st.markdown("""
        <div style='text-align: center; padding: 50px; color: #87ceeb;'>
            <p style='font-size: 1.2em;'>📸 Photos will appear here once uploaded!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ==================== TAB 3: MEMORIES ====================
with tab3:
    st.markdown('<div class="section-title">Our Memories Together</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center; font-size: 1.2em; color: #e0f2fe; margin-bottom: 30px;'>
    The moments that make our friendship unforgettable 💙
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="message-card">
        <div class="memory-author">📝 2018 - When It All Began</div>
        <p>
        That very first conversation in 2018 changed everything. We didn't know then that we'd become as close as we are now. 
        From that first moment, there was just something special — a connection that felt natural and real.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="message-card">
        <div class="memory-author">💙 The Distance & The Bond</div>
        <p>
        Distance has never been able to break what we have. Every call, every message, every time you visit Sri Lanka — 
        those moments remind me why our friendship is so precious. We've learned that real friendship doesn't need constant physical presence; 
        it thrives on genuine care and effort. And girl, you've always put in the effort.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="message-card">
        <div class="memory-author">🎂 Growing Up Together</div>
        <p>
        From 12-year-old you to 21-year-old you — I've had the privilege of watching you grow into an incredible woman. 
        I've seen you overcome challenges, chase your dreams, and become someone you're genuinely proud of. 
        And honestly, I'm so incredibly proud of you too.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 40px; color: #87ceeb; font-size: 1.1em;'>
    <p>💙 Made with love for my best friend 💙</p>
    <p style='color: #e0f2fe; font-size: 0.9em; margin-top: 20px;'>Here's to friendship, memories, and a lifetime of laughter together!</p>
</div>
""", unsafe_allow_html=True)

# Helper function to convert image to base64
def img_to_base64(img):
    import base64
    from io import BytesIO
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str
