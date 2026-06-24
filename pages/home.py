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
# SESSION STATE INITIALIZATION
# ------------------------------------------------
if "show_popup" not in st.session_state:
    st.session_state.show_popup = False

if "agreement_checked" not in st.session_state:
    st.session_state.agreement_checked = False

if "accepted_terms" not in st.session_state:
    st.session_state.accepted_terms = False


@st.dialog("Privacy Notice – AI Maturity Assessment")
def show_terms_popup():

    st.markdown("""
<div style="font-size:11px; line-height:1;">

#### Purpose
This assessment collects responses to evaluate the AI maturity of your organization and generate insights and recommendations.

#### Data Collected
We may collect:
- Survey responses  
- Organization-related inputs (if provided)  
- Technical metadata (e.g., browser or session information)  

#### How Data is Used
Your data will be used to:
- Analyze AI maturity levels  
- Generate aggregated insights and reports  
- Improve our assessment capabilities  

#### Data Storage
All data is securely stored using cloud infrastructure (e.g., Azure services).

#### Data Retention
Data may be retained for analysis purposes and will be securely managed.

#### Data Sharing
Your responses will not be shared externally.

#### Your Rights
You may:
- Withdraw consent at any time  
- Request deletion of your data  

</div>
""", unsafe_allow_html=True)
    if st.button("Accept",key='accept_btn'):
        st.session_state.accepted_terms = True
        st.session_state.show_popup = False
        st.rerun()

    # if st.button("Close"):
    #     st.session_state.show_popup = False
    #     st.rerun()

# ------------------------------------------------
# IMAGE DATA
# ------------------------------------------------
def get_base64(file):
       with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()
Background_image_data = get_base64("media/Redesigned_Home_Bg.png")
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
   margin-top: 0.5rem;
   margin-left: -10px;
   text-align: center;
   height: 100px;
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
/* Main button */
.st-key-get_started_btn button {{
    display: inline-flex;
    align-items: center;
    justify-content: flex-start;
    background: transparent !important;
    color: #7dd3fc !important;
    padding: 10px 20px !important;
    padding-right: 50px !important;
    border-radius: 999px !important;
    border: 2px solid #38bdf8 !important;

    height: 55px;
    width: auto;
    min-width: 180px;
    white-space: nowrap;
    overflow: hidden;

    position: relative;
    margin-top: 5px;

    font-weight: 600;
    font-size: 14px;
    transition: all 0.3s ease;
}}

/* Arrow */
.st-key-get_started_btn button::after {{
    content: "❯";
    position: absolute;
    right: 0px;

    width: 50px;
    height: 50px;

    background: linear-gradient(135deg, #38bdf8, #2563eb);
    color: white;

    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 20px;
    font-weight: bold;
}}

/* Hover */
.st-key-get_started_btn button:hover {{
    border-color: #60a5fa !important;
    box-shadow: 0 0 8px rgba(56, 189, 248, 0.5);
    color: #bae6fd !important;
}}
/* Target ONLY the privacy link button */
.st-key-terms_btn button {{
    background: none !important;
    border: none !important;
    padding: 0 !important;
    margin-top: 5px !important;
    color: #60a5fa !important;
    text-decoration: none;
    float: left;
    font-size: 16px;
    font-weight: 500;
    align-items: left;
    cursor: pointer;
    box-shadow: none !important;
}}

/* Ensure no arrow */
.st-key-terms_btn button::after {{
    content: none !important;
}}

/* T&C and Checkbox Section */
.tc-section {{
    margin-top: 30px;
    margin-bottom: -20px;
    margin-left: 10px;
}}

.tc-text {{
    color: white;
    font-size: 0.98rem;
    font-weight: 600;
    line-height: 1.5;
    margin-top: 10px;
    margin-bottom: -20px;
    padding-bottom: 10px;
    max-width: 380px;
    word-wrap: break-word;
    overflow-wrap: break-word;
    white-space: normal;
}}

/* Custom Checkbox - Large Size */
div[data-testid="stCheckbox"] {{
    margin-top: 3px;
}}

div[data-testid="stCheckbox"] label {{
    cursor: pointer;
}}

/* Increase checkbox input size */
div[data-testid="stCheckbox"] input[type="checkbox"] {{
    width: 20px !important;
    height: 20px !important;
    cursor: pointer;
    accent-color: #38bdf8;
}}

.privacy-link {{
    color: #60a5fa;
    font-size: 18px;
    font-weight: 500;
    border-bottom: 1px solid #38bdf8;
    text-decoration: underline !important;
    transition: all 0.2s ease;
}}
.privacy-link:hover {{
    color: #60a5fa;
    text-decoration: underline !important;
    border-bottom: 1px solid #60a5fa;
}}

/* Button disabled state - visible but grayed/blurred */
div.stButton > button:disabled {{
    opacity: 0.2;
    cursor: not-allowed;
    filter: blur(0.2px);
    background: transparent;
    border-color: #38bdf8 !important;
    color: #7dd3fc !important;
}}

div.stButton > button:disabled::after {{
    opacity: 0.8;
}}

div.stButton > button:disabled:hover {{
    border-color: #38bdf8;
    box-shadow: none;
    color: #7dd3fc;
    transform: none;
    opacity: 0.8;
}}
.st-key-accept_btn button {{
    background: linear-gradient(135deg, #38bdf8, #2563eb) !important;
    border: none !important;
    padding: 0 !important;
    margin-top: 5px !important;
    color: white !important;
    text-decoration: none;
    width: 70px;
    float: left;
    font-size: 16px;
    font-weight: 500;
    align-items: left;
    cursor: pointer;
    box-shadow: none !important;
}}
</style>
""", unsafe_allow_html=True)
# ------------------------------------------------
# TOP RIGHT
# ------------------------------------------------
st.markdown(
    f"<div class='welcome-text'>Welcome</div>",
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
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
_ , center, _ = st.columns([0.2,6,2])
_ , center, _ = st.columns([0.2,6,2])
with center: 
    # ------------------------------------------------
    # SESSION STATE FOR CHECKBOX
    # ------------------------------------------------
    if "agreement_checked" not in st.session_state:
        st.session_state.agreement_checked = False
    if "show_popup" not in st.session_state:
        st.session_state.show_popup = False
    # ------------------------------------------------
    # CHECKBOX WITH PRIVACY NOTICE LINK
    # ------------------------------------------------
    col1, col2 = st.columns([0.04, 1])
    
    with col1:
        st.session_state.agreement_checked = st.checkbox(
            label="",
            value=st.session_state.agreement_checked,
            key="agreement_checkbox",
            disabled=not st.session_state.accepted_terms
        )
    
    with col2:
        st.markdown(
            """
            <div class='tc-text'>
                I agree to the collection and processing of my responses 
                for AI maturity assessment and improvement purposes.
            </div>
            """,
            unsafe_allow_html=True
        )
        link_clicked = st.button("View Privacy Notice Before Proceeding", key="terms_btn")
        if link_clicked:
            st.session_state.show_popup = True

# ------------------------------------------------
# TRIGGER POPUP
# ------------------------------------------------
if st.session_state.show_popup:
    show_terms_popup()

# ------------------------------------------------
# GET STARTED BUTTON (Always visible, grayed when disabled)
# ------------------------------------------------
_,center,_ = st.columns([0.7,2,4])
with center:
    if st.button(
            "Get Started",
            key="get_started_btn",
            disabled=not st.session_state.agreement_checked,
            use_container_width=False
        ):
            st.switch_page("pages/login.py")