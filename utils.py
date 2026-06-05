import base64
import streamlit as st

# ------------------------------------------------
# HOME BUTTON
# ------------------------------------------------

def home_button():
    with open("media/home-icon.png", "rb") as f:
        logo_image_data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <a href="home" target="_self">
            <img src="data:image/png;base64,{logo_image_data}" 
                 style="width:32px;height:32px;cursor:pointer;" />
        </a>
        """,
        unsafe_allow_html=True
    )