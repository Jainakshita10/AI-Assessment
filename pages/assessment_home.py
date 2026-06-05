import base64

import streamlit as st

from utils import home_button
# ✅ ADD HERE
if "answers" not in st.session_state:
    st.session_state.answers = {}


# ------------------------------------------------
# SECURITY CHECK
# ------------------------------------------------
# if (
#     "logged_in" not in st.session_state
#     or
#     not st.session_state.logged_in
# ):
#     st.switch_page("pages/login.py")
# ------------------------------------------------
# IMAGE DATA
# ------------------------------------------------
with open("media/logo.png", "rb") as f:
    logo_image_data = base64.b64encode(f.read()).decode()
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
    background: #000031;
}

/* Full Width Content */
.block-container {

    max-width: 100% !important;
    width: 100% !important;

    margin: 0;

    padding-top: 0rem;
    padding-bottom: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;

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
    margin-top: 0px;
    margin-bottom: 20px;
    font-family: 'Segoe UI', sans-serif;
            top: 5px;
}

/* Headings */
.section-heading {
    color: white;
    font-size: 16px;
    font-weight: bold;
    margin-top: 0px;
    margin-bottom: 1px;
}
/* objective Text */
.objective-text {
    color: white;
    font-size: 16px;
    line-height: 1.5;
    font-family: 'Segoe UI', sans-serif;
    margin-top: -10px;
    margin-bottom: -10px;
}
/* Body Text */
.body-text {
    color: white;
    font-size: 13px;
    line-height: 1.4;
    font-family:Segoe UI;
    margin-bottom: -10px;
}

/* Bullet spacing */
ul {
    padding-left: 20px;
}
 /* Global dimension buttons - light blue */
       .stButton > button {
            background: #357ABD !important;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
           color: #1a1a2e !important;
           border: none !important;
           border-radius: 5px !important;
           font-size: 16px !important;
           font-weight: bold !important;
            height: 55px !important;
       }

/* Inputs */
.stTextInput input {
    background-color: white;
    color: black;
    border-radius: 5px;
    padding: 10px;
    max-width: 360px;
    width: 100%;
    box-sizing: border-box;
}
/* Logo */
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

# ------------------------------------------------
# TOP BAR
# ------------------------------------------------

col1, col2, col3 = st.columns([1, 6, 1], vertical_alignment="center")

# Left: Home icon
with col1:
    home_button()

# Center: Title
with col2:  
    st.markdown(
            """
            <h1 style='
                text-align:center;
                margin-top:0px;
                margin-bottom:20px;
                font-size:25px;
                font-weight:bold;
                color:white;
                font-family:"Segoe UI", sans-serif;
            '>
                AI Maturity Assessment
            </h1>
            """,
            unsafe_allow_html=True
        )
# Right: Logo
with col3:
    st.markdown(
        f"""
        <div style="display:flex; justify-content:flex-end; align-items:center;">
            <img src="data:image/png;base64,{logo_image_data}" style="height:40px;">
        </div>
        """,
        unsafe_allow_html=True
    )
# ------------------------------------------------
# OBJECTIVE
# ------------------------------------------------
st.markdown(
    """
    <div class='objective-text'>
    <b>Objective of the assessment:</b>
    To evaluate the organization’s current AI maturity
    across strategy, data, technology, and governance areas.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------------------------
# CONTENT COLUMNS
# ------------------------------------------------
left, right = st.columns(2)

# ------------------------------------------------
# LEFT COLUMN
# ------------------------------------------------
with left:
   st.markdown("""
<div class='section-heading'>
<p><strong>Areas of Assessment:</strong></p>
</div>
<div class='body-text'>
<p>
   The assessment covers the following dimensions:
</p>
<ul>
<li>
<b>Strategy and Operating Model:</b>
       To evaluate how clearly AI ambition connects
       to enterprise purpose and strategic priorities.
</li>
<li>
<b>Value Realization:</b>
       To measure how effectively AI investments
       translate into measurable business outcomes.
</li>
<li>
<b>Data Foundation:</b>
       To assess the quality and scalability
       of data ecosystems in the organization.
</li>
<li>
<b>People & Culture:</b>
       To examine how organizations attract,
       retain, and develop multidisciplinary talent.
</li>
<li>
<b>Trusted AI:</b>
       To improve trust while protecting
       from potential AI risks.
</li>
<li>
<b>Advanced Capabilities:</b>
       To operationalize, customize,
       and scale AI technologies.
</li>
<li>
<b>AI Engineering:</b>
       To build and scale production-grade AI systems.
</li>
</ul>
</div>
   """, unsafe_allow_html=True)
# ------------------------------------------------
# RIGHT COLUMN
# ------------------------------------------------
with right:
   st.markdown("""
<div class='section-heading'>
       Scoring Methodology:
</div>
<div class='body-text'>
<p>
   Each question is scored on a 1–5 maturity scale:
</p>
<ul>
<li>
<b><span style='color:#28a745;'>5 – LEADING:</span></b>
       Leaders that have industrialized AI across strategy,
       operations, and governance.
</li>
<li>
<b><span style='color:#007bff;'>4 – SCALED:</span></b>
       Companies with strong AI foundations
       scaling enterprise use cases.
</li>
<li>
<b><span style='color:#17a2b8;'>3 – DEFINED:</span></b>
       AI is moving beyond pilots with measurable outcomes.
</li>
<li>
<b><span style='color:#ffc107;'>2 – EMERGING:</span></b>
       Organizations are experimenting
       through pilots and proofs of concept.
</li>
<li>
<b><span style='color:#e83e8c;'>1 – LAGGING:</span></b>
       Minimal or no formal AI activity.
</li>
</ul>
</div>
   """, unsafe_allow_html=True)
# ------------------------------------------------
# BOTTOM SECTION
# ------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

bottom_left, bottom_right = st.columns(2)

with bottom_left:

    st.markdown(
        """
        <div class='section-heading'>
            How to answer questions:
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='body-text'>

        <ul>
            <li>Choose the option that most clearly matches the organization.</li>
            <li>
            If the organization is between two levels,
            select the lower score unless strong evidence exists.
            </li>
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )

with bottom_right:

    st.markdown(
        """
        <div class='section-heading'>
            Confidentiality Note:
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='body-text'>

        All responses will be treated as confidential
        and used solely for assessment and advisory purposes.

        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------
# DIMENSIONS
# ------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div class='section-heading'>
        Click on any Dimension to proceed:
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------
# BUTTON ROW
# ------------------------------------------------
c1, c2, c3, c4, c5, c6, c7 = st.columns(7)

with c1:
   if st.button("Strategy and\nOperating Model", key="dimension-btn-1",use_container_width=True):
       st.session_state.selected_dimension = 0
       st.session_state.question_index = 0
       st.switch_page("pages/questionnaire.py")

with c2:
    if st.button("Value Realisation", key="dimension-btn-2", use_container_width=True):
        st.session_state.selected_dimension = 1
        st.session_state.question_index = 0
        st.switch_page("pages/questionnaire.py")

with c3:
    if st.button("Data Foundation", key="dimension-btn-3", use_container_width=True):
        st.session_state.selected_dimension = 2
        st.session_state.question_index = 0
        st.switch_page("pages/questionnaire.py")

with c4:
    if st.button("People and\nCulture", key="dimension-btn-4", use_container_width=True):
        st.session_state.selected_dimension = 3
        st.session_state.question_index = 0
        st.switch_page("pages/questionnaire.py")
with c5:
    if st.button("Trusted and\nResponsible AI", key="dimension-btn-5", use_container_width=True):
        st.session_state.selected_dimension = 4
        st.session_state.question_index = 0
        st.switch_page("pages/questionnaire.py")

with c6:
    if st.button("Advanced\nCapabilities", key="dimension-btn-6", use_container_width=True):
        st.session_state.selected_dimension = 5
        st.session_state.question_index = 0
        st.switch_page("pages/questionnaire.py")

with c7:
   if st.button("AI Engineering", key="dimension-btn-7", use_container_width=True):
       st.session_state.selected_dimension = 6
       st.session_state.question_index = 0
       st.switch_page("pages/questionnaire.py")