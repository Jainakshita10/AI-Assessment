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
# CSS
# ------------------------------------------------
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Full App Background */
.stApp {
    background: linear-gradient(
        135deg,
        #4da3ff 0%,
        #2874e8 25%,
        #0b3c8c 60%,
        #001a4d 100%
    );
}

/* Full Width Content */
.block-container {

    max-width: 100% !important;
    width: 100% !important;

    margin: 0;

    padding-top: 1rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;

    background: linear-gradient(
        135deg,
        #4da3ff 0%,
        #2874e8 25%,
        #0b3c8c 60%,
        #001a4d 100%
    );

    border-radius: 0;

    box-shadow: none;
    min-height: 100vh;
}

/* Welcome */
.welcome-text {

    text-align: right;

    color: white;

    font-size: 18px;

    font-weight: 600;
}

/* Main Title */
.main-title {

    text-align: left;

    color: white;

    font-size: 58px;

    font-weight: 900;

    line-height: 1.05;

    margin-top: 10px;

    margin-bottom: 20px;
}

/* Subtitle */
.sub-text {

    color: #e5e5e5;

    font-size: 20px;

    width: 420px;

    line-height: 1.5;

    margin-top: 10px;
}

/* Info Box */
.info-box {

    width: 420px;

    background: rgba(0,0,0,0.28);

    padding: 20px;

    border-radius: 8px;

    margin-top: 30px;

    text-align: center;
}

/* Info Text */
.info-text {

    color: white;

    font-size: 17px;

    font-weight: 600;

    line-height: 1.5;
}

/* PowerApps Button */
div.stButton > button {

    width: 240px;

    height: 56px;

    border-radius: 40px;

    border: none;

    background: linear-gradient(
        90deg,
        #2f63ff,
        #55d6ff
    );

    color: white;

    font-size: 18px;

    font-weight: 800;

    display: block;

    margin-top: 20px;

    box-shadow:
        0px 4px 12px rgba(0,0,0,0.25);
}

/* Hover */
div.stButton > button:hover {

    transform: scale(1.02);

    color: white;

    border: none;
}

/* Branding */
.branding {

    margin-top: 25px;

    color: white;

    font-size: 30px;

    font-weight: 700;

    white-space: nowrap;
}

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
# LAYOUT
# ------------------------------------------------
left, right = st.columns([1.1,0.9])

# ------------------------------------------------
# LEFT SIDE
# ------------------------------------------------
with left:

    st.markdown(
        """
        <div class='main-title'>
            AI Maturity<br>
            Assessment<br>
            Form
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='sub-text'>
            Our maturity assessment helps your organization
            gauge its progress in adopting AI technologies
            and best practices across the workplace
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
   """
<div class='info-box'>
<div class='info-text'>
           Every journey begins with knowing where you are -
           this is our first step toward AI excellence
</div>
</div>
   """,
   unsafe_allow_html=True
)

    # ------------------------------------------------
    # BUTTON
    # ------------------------------------------------
    if st.button("GET STARTED  ➜"):

        st.switch_page("pages/login.py")

    # ------------------------------------------------
    # BRANDING
    # ------------------------------------------------
    st.markdown(
        """
        <div class='branding'>
            Capgemini invent
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------
# RIGHT SIDE
# ------------------------------------------------
with right:
   st.markdown(
       "<div style='height: 220px;'></div>",
       unsafe_allow_html=True
   )
   st.image(
       "media/home-photo.jpeg",
       width=420
   )