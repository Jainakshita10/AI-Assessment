import base64
import os
from dotenv import load_dotenv

import streamlit as st
from PIL import Image

load_dotenv()

LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "AI_Assessment")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "Ai@assessment!2026")

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="AI Maturity Assessment",
    page_icon=Image.open('./media/logo-streamlit.png'),
    layout="wide",
    initial_sidebar_state="collapsed",
)
# ------------------------------------------------
# SESSION STATE
# ------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
# ------------------------------------------------
# IMAGE DATA
# ------------------------------------------------
with open("media/logo.png", "rb") as f:
    logo_image_data = base64.b64encode(f.read()).decode()
# ------------------------------------------------
# CSS
# ------------------------------------------------
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Full App Background */
.stApp {
    background: #000031;
}

/* Full Width Content */
.block-container {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0;
    padding-top: 0.8rem;
    padding-bottom: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
    background: #000031;
    border-radius: 0;
    box-shadow: none;
    min-height: 100vh;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    color: white;
    margin-top: -20px;
    margin-bottom: 30px;
    font-family: 'Segoe UI', sans-serif;
}

/* Login box */
.login-box {
    width: 500px;
    margin: auto;
    color: white;
}

/* Subtitle */
.sub-text {
    text-align: left;
    font-size: 13px;
    margin-top: 50px;
    margin-bottom: 30px;
    color: #d9d9d9;
    font-family: 'Open Sans', sans-serif;
    font-style: italic;
}

/* Labels */
label {
    color: white !important;
    font-size: 17px !important;
    font-weight: 600 !important;
}

/* Inputs */
.stTextInput input {
    background-color: white;
    color: black;
    border-radius: 5px;
    padding: 10px;
}

/* Button */
.stButton > button {
    width: 180px;
    background: linear-gradient(to right, #4a90ff, #6aa8ff);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px;
    font-size: 18px;
    font-weight: bold;
    display: block;
    margin: auto;
}
.white-text {
   color: white !important;
   font-size: 20px;
   font-weight: 600;
}
.logo-container {
   position: fixed;
   top: 5px;
   right: 5px;
   z-index: 999;
}
.logo-container img {
   width: 60px;
}
</style>
""", unsafe_allow_html=True)
# ------------------------
#     Top Logo
# ------------------------
top_left, top_center, top_right = st.columns([1, 5, 1])

# Left spacer
with top_left:
    st.write("")

# Center title
with top_center:
    st.markdown(
        "<h1 style='text-align:center; margin:0; font-size:25px; font-weight:bold; color:white; font-family:\'Segoe UI\', sans-serif;'>AI Maturity Assessment</h1>",
        unsafe_allow_html=True
    )
    
# Right logo (aligned right)
with top_right:
    st.markdown(
        f"""
        <div style="display:flex; justify-content:flex-end; align-items:center; height:100%;">
            <img src="data:image/png;base64,{logo_image_data}" width="40">
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------
#     Top Title
# ------------------------
a1, a2 = st.columns([0.7, 2])
with a2:
    st.markdown(
            "<div class='login-box'>"
            "<div class='sub-text'>Sign in to access your assessment</div>",
            unsafe_allow_html=True
        )
# ------------------------
#     Center Login
# ------------------------
left, center, right = st.columns([0.8,2,1.2])
with center:
   # Username row
   c1, c2 = st.columns([0.7,2])
   with c1:
       st.markdown(
           "<p style='color:white; font-size:18px; font-family: 'Open Sans', sans-serif; font-weight:800; margin-top:10px; text-align:right;'>User Name</p>",
           unsafe_allow_html=True
       )
   with c2:
    #    st.markdown("""
    #         <style>
    #         .stTextInput input {
    #         width: 320px !important;
    #         height: 45px;
    #         border-radius: 0px;!important;
    #         }
    #         </style>
    #     """, unsafe_allow_html=True)
       username = st.text_input(
           "",
           placeholder="Enter User Name",
           label_visibility="collapsed"
       )
   # Password row
   c3, c4 = st.columns([0.7,2])
   with c3:
       st.markdown(
           "<p style='color:white; font-size:18px; font-family: 'Open Sans', sans-serif; font-weight:800; margin-top:10px;'>Password</p>",
           unsafe_allow_html=True
       )
   with c4:
        # st.markdown("""
        #     <style>
        #     .stTextInput input {
        #     width: 320px !important;
        #     height: 45px;
        #     border-radius: 12px;
        #     }
        #     </style>
        # """, unsafe_allow_html=True)
        password = st.text_input(
           "",
           placeholder="Enter Password",
           type="password",
           label_visibility="collapsed"
       )   
   st.markdown("<br>", unsafe_allow_html=True)

    # Button row - match the password field structure
   b1, b2 = st.columns([0.7, 2])
   with b2:
        login = st.button("Login", use_container_width=True)

   if login:
        if username == LOGIN_USERNAME and password == LOGIN_PASSWORD:

            st.session_state.logged_in = True
            st.markdown("""
                    <div style="
                    background-color:#d4edda;
                    color:#155724;
                    padding:10px;
                    border-radius:8px;
                    text-align:center;
                    font-weight:600;
                    ">
                    Login Successful
                    </div>
                    """, unsafe_allow_html=True)
            #st.success("Login Successful")

            # Navigate to next page
            st.switch_page("pages/user_info.py")
        else:
            st.markdown("""
                    <div style="
                    background-color:#f8d7da;
                    color:#842029;
                    padding:10px;
                    border-radius:8px;
                    text-align:center;
                    font-weight:600;
                    ">
                    Invalid Username or Password
                    </div>
                    """, unsafe_allow_html=True)
            #st.error("Invalid Username or Password")

   st.markdown("</div>", unsafe_allow_html=True)    