import base64
import streamlit as st

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="AI Maturity Assessment",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# ------------------------------------------------
# IMAGE DATA
# ------------------------------------------------
def get_base64(file):
       with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()
Background_image_data = get_base64("media/Redesigned_Home_Bg.png")
get_started = get_base64("media/cropped_get_started.png")
# ------------------------------------------------
# CSS
# ------------------------------------------------
st.markdown(f"""
<style>
html, body {{
    margin: 0;
    padding: 0;
}}
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header {{visibility: hidden;}}
/* Full App Background */
.stApp {{
    background-image: url("data:image/png;base64,{Background_image_data}");
   background-size: cover;
   background-position: center;
   background-repeat: no-repeat;
   min-height: 100vh;
}}
/* Full Width Content */
.block-container {{
    max-width: 100% !important;
    width: 100% !important;
    margin: 0;
    padding-top: 0rem !important;
    padding-bottom: 2rem !important;
    padding-left: 0rem !important;
    padding-right: 2rem !important;
    background: transparent;
    border-radius: 0;
    box-shadow: none;
    min-height: 100vh;
}}
/* Welcome */
.welcome-text {{
    position: absolute;
    top: 2rem;
    right: 2.5rem;
    text-align: right;
    color: white;
    font-size: 18px;
    font-weight: 600;
    z-index: 10;
}}
/* Main Title */
.main-title {{
    color: white;
    font-family: 'Ubuntu', sans-serif;
    font-size: 3.2rem;
    font-weight: 700;
    line-height: 1.05;
    margin: 0 0 1rem 0;
    max-width: 460px;
    letter-spacing: -0.8px;
}}
/* Subtitle */
.sub-text {{
    color: #e9f1ff;
    font-family: 'Ubuntu', sans-serif;
    font-size: 0.98rem;
    font-weight: 300;
    line-height: 1.6;
    margin: 0 0 1.8rem 0;
    max-width: 480px;
    padding-right: 0;
}}
/* Info Box */
.info-box {{
   width: 450px;
   background: rgba(6,25,60,0.82);
   padding: 24px 10px;
   border-radius: -20px;
   margin-top: 3.5rem;
   margin-left: -10px;
   text-align: center;
   height: 180px;
}}
/* Info Text */
.info-text {{
    color: white;
    font-size: 0.98rem;
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: -20px;
    padding-bottom: 0px
}}
.content-wrapper {{
    position: relative;
    z-index: 2;
    max-width: 600px;
    padding: 1rem 2rem 1rem 2rem;
    margin: 0;
}}
.custom-btn {{
   margin-top: 28px;
   width: 230px;
   height: 58px;
   border-radius: 40px;
   border: none;
   background: linear-gradient(
       90deg,
       #2f63ff,
       #55d6ff
   );
   color: white;
   font-size: 18px;
   font-weight: 700;
   cursor: pointer;
   box-shadow:
       0px 4px 12px rgba(0,0,0,0.25);
}}
.custom-btn:hover {{
   transform: scale(1.02);
}}
div.stButton {{
   margin-top: 25px;
   margin-left: 15px;
}}
div.stButton > button {{
   width: 230px;
   height: 58px;
   border-radius: 40px;
   border: none;
   background: linear-gradient(
       90deg,
       #2f63ff,
       #55d6ff
   );
   color: white;
   font-size: 18px;
   font-weight: 700;
   cursor: pointer;
   box-shadow:
       0px 4px 12px rgba(0,0,0,0.25);
}}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# USERNAME
# ------------------------------------------------
username = "Akshita"

# ------------------------------------------------
# TOP RIGHT
# ------------------------------------------------
st.markdown(
    f"<div class='welcome-text'>Welcome {username}</div>",
    unsafe_allow_html=True
)
# ------------------------------------------------
# CONTENT
# ------------------------------------------------
st.markdown(
    f"""
    <div class='content-wrapper'>
        <div class='main-title'>
            AI Maturity Assessment Form
        </div>
        <div class='sub-text'>
            Our maturity assessment helps your organization
            gauge its progress in adopting AI technologies
            and best practices across the workplace
        </div>
        <div class='info-box'>
            <div class='info-text'>
                Every journey begins with knowing where you are —
                this is our first step toward AI excellence
            </div>
            <a href="login" target="_self">
                <img src="data:image/png;base64,{get_started}"
                     style="width:700px;height:200px;cursor:pointer;margin-top:-20px;margin-bottom: 0px" />
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
