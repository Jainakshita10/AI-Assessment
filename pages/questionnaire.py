# questionnaire.py
import base64

import streamlit as st
import streamlit.components.v1 as components
from questions import load_questions, get_dimension_list
#from ui_style import apply_global_style

with open("media/logo.png", "rb") as f:
    logo_image_data = base64.b64encode(f.read()).decode()
with open("media/back-icon.png", "rb") as f:
    back_icon_data = base64.b64encode(f.read()).decode()

#apply_global_style()

st.markdown("""
<style> 
     #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

/* Full App Background */
.stApp {
    background: #000031;
    font-family: 'Segoe UI', sans-serif;
}

/* Hide scrollbar */
    ::-webkit-scrollbar { display: none; }
    body {
        -ms-overflow-style: none;
        scrollbar-width: none;
    }

/* .stApp, .stApp * {color: white !important;} */

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
    border-radius: -10px;
    box-shadow: none;
    min-height: 100vh;
}

    /* Titles */
    h1, h2, h3 {
        color: #00c6ff;
        font-weight: 600;
        margin-top: 0;
        margin-bottom: 0.5rem;
    }

    h2 {
        font-size: 1.3rem !important;
    }

    h3 {
        font-size: 1rem !important;
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
            /* Buttons */
    .stButton > button {
        margin-top: 0px;
        background-color: #0f2f5f;
        color: white;
        border-radius: -10px;
        padding: 0px 0px;
        border: 1px solid #1f5fa3;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: #0077b6;
        transform: scale(1.05);
    }
    /* Target ONLY the top back button */
    div[data-testid="stButton"] button[key="back_home_button"] {
        padding: 0px 0px;
        height: 10px;
        width: 10px;
        font-size: 8px;
        line-height: 1;
        border-radius: 50%;
    }

/* Remove extra spacing around button */
div[data-testid="stButton"]:has(button[key="back_home_button"]) {
    margin-bottom: 0px;
    padding: 0px 0px;
    height: 10px;
    width: 10px;
    font-size: 8px;
    line-height: 1;
    border-radius: 50%;
}

/* Target both buttons using their keys */
div[data-testid="stButton"] > button[kind="secondary"] {
    border-radius: 50% !important;
    width: 50px;
    height: 50px;
    padding: 0px;
    font-size: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Optional: tighter look */
button#back_button, button#next_button {
    border-radius: 50% !important;
}

    /* Cards for options */
    .option-card {
        padding: 16px;
        margin-bottom: 10px;
        border-radius: 10px;
        background-color: #0f2f5f;
        border: 1px solid #1f5fa3;
        cursor: pointer;
    }

    .option-selected {
        background-color: #0077b6 !important;
        border: 2px solid #00c6ff;
    }

    /* Top Nav pills */
    .pill {
        display: inline-block;
        padding: 8px 14px;
        margin-right: 6px;
        border-radius: 12px;
        background-color: #0f2f5f;
    }

    /* Score Table */
    .custom-table {
        background-color: #0f2f5f;
        border-radius: 10px;
        padding: 10px;
    }

    /* Radio Options */
    div[data-testid="stRadio"] label {
        background: rgba(255,255,255,0.08);
        padding: 8px 12px;
        padding-right: 20px;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.10);
        color: white !important;
        font-size: 13px;
        font-weight: 600;
        min-height: 40px;
        display: flex;
        align-items: center;
        transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
        cursor: pointer;
        margin-bottom: 6px;
        color: #FFFFFF !important;
    }

    div[data-testid="stRadio"] label input[type="radio"] {
        position: absolute;
        opacity: 0;
        width: 300%;
        height: 100%;
        margin: 0;
        z-index: 1;
        cursor: pointer;
    }

    div[data-testid="stRadio"] label:has(input[type="radio"]:checked),
    div[data-testid="stRadio"] label input[type="radio"]:checked + div,
    div[data-testid="stRadio"] label input[type="radio"]:checked ~ div {
        background: #1b9400;
        border-color: #1b9400;
        color: #FFFFFF !important;
    }
/* Target each radio option container */
div[data-testid="stRadio"] label {
    padding: 15px 20px;       /* ✅ increases height + inner spacing */
    border-radius: 12px;      /* rounded corners */
    width: 100%;              /* full width box */
    display: flex;
    align-items: center;
    gap: 10px;
    color: #FFFFFF !important;
}

div[data-testid="stRadio"] label * {
   color: #FFFFFF !important;
   fill: #FFFFFF !important;
}
/* Increase spacing between options */
div[data-testid="stRadio"] > div {
    gap: 12px;
}

    .tabs-wrapper-container {
        width: 400px;
        max-width: 280px;
        overflow-x: auto;
        padding: 6px 0;
        margin-top: 6px;
        display: flex;
        justify-content: flex-start;
    }

    .tabs-wrapper {
        display: flex;
        gap: 6px;
        min-width: max-content;
    }

    .question-tab {
        background-color: #0f2f5f;
        color: white;
        padding: 6px 10px;
        border-radius: 10px;
        min-width: 42px;
        width: 42px;
        height: 38px;
        line-height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        font-weight: 600;
        font-size: 12px;
        border: 1px solid #1f5fa3;
        flex: 0 0 auto;
        white-space: nowrap;
        transition: transform 0.2s ease, background-color 0.2s ease;
    }

    .question-tab:hover {
        background-color: #0077b6;
        transform: scale(1.03);
    }

    .active-tab {
        background-color: #00c6ff !important;
        color: #071b3a !important;
        border-color: #ffffff;
    }

    .tabs-wrapper-container::-webkit-scrollbar {
        height: 8px;
    }

    .tabs-wrapper-container::-webkit-scrollbar-track {
        background: transparent;
    }

    .tabs-wrapper-container::-webkit-scrollbar-thumb {
        background: rgba(255,255,255,0.35);
        border-radius: 4px;
    }

    .tabs-wrapper-container::-webkit-scrollbar-thumb:hover {
        background: rgba(255,255,255,0.6);
    }

.navigation-bar {
   position: fixed !important;
   top: 0px !important;
   left: 20px !important;
   margin: 0 !important;
   padding: 0 !important;
   display: flex;
   align-items: flex-start !important;
   z-index: 9999;
   border-radius: 50px !important;
}
</style>
""", unsafe_allow_html=True)
# ── Dimension heading (outside box) + compact grey question box ───────────────
st.markdown("""
<style>
/* Full-width grey question container */
.question-box {
   background: rgba(242, 242, 242, 1);
   border-radius: 12px;
   padding: 12px 32px;
   margin-top: 6px;
   margin-bottom: 14px;
   border: 1px solid rgba(180,180,200,0.5);
   box-shadow: 0 2px 10px rgba(0,0,0,0.18);
   width: 100%;
   box-sizing: border-box;
}
.question-box .q-text {
   font-size: 13.5px;
   font-weight: 600;
   color: #0d1b2e !important;
   line-height: 1.4;
   margin: 0;
   white-space: nowrap;
   overflow: hidden;
   text-overflow: ellipsis;
}
/* Centre and compact the radio options — dark option boxes */
div[data-testid="stRadio"] > div[role="radiogroup"] {
   display: flex !important;
   flex-direction: column !important;
   align-items: center !important;
   gap: 6px !important;
   width: 100% !important;
}
div[data-testid="stRadio"] label {
   width: 100% !important;
   min-height: 34px !important;
   padding: 6px 14px !important;
   font-size: 12px !important;
   border-radius: 8px !important;
   justify-content: flex-start !important;
   margin-bottom: 0 !important;
   background: #1a1a2e !important;
   border: 1px solid #2e2e4a !important;
   color: #FFFFFF !important;
}
div[data-testid="stRadio"] label:hover {
   background: #252540 !important;
   border-color: #4a4a7a !important;
}
/* Hide empty radio label / wrapper */
div[data-testid="stRadio"] > label {
   display: none !important;
   height: 0 !important;
   margin: 0 !important;
   padding: 0 !important;
}
div[data-testid="stRadio"] {
   margin-top: 0 !important;
   padding-top: 0 !important;
}
div[data-testid="stRadio"] > div:first-child {
   background: transparent !important;
   border: none !important;
   box-shadow: none !important;
   padding: 0 !important;
   margin: 0 !important;
   width: 100% !important;
}
            
/* Icon-only circular nav buttons */
button[key="back_button"],
button[key="next_button"] {
   width: 24px !important;
   height: 24px !important;
   border-radius: 50% !important;
   padding: 0 !important;
   font-size: 48px !important;
   display: flex !important;
   align-items: center !important;
   justify-content: center !important;
   min-width: 0 !important;
}
/* Target ONLY the top back button */
    div[data-testid="stButton"] button[key="back_home_button"] {
        padding: 0px 0px;
        height: 10px;
        width: 10px;
        font-size: 24px;
        line-height: 1;
        border-radius: -10px;
        weight: 1000 !important;
    }

    /* Remove extra spacing around button */
    div[data-testid="stButton"]:has(button[key="back_home_button"]) {
        padding: 0px 0px;
        height: 10px;
        width: 10px;
        font-size: 28px;
        line-height: 1;
        border-radius: -10px;
        margin-top: 0px;
        margin-bottom: 0px;
    }
/* NAV BUTTON */
button[kind="secondary"] {
    background-color: transparent !important;
    border: 2px solid white !important;
    border-radius: 50% !important;

    width: 48px !important;
    height: 48px !important;

    display: flex !important;
    align-items: center;
    justify-content: center;

    padding: 0 !important;
}
/* 🔥 Force inner arrow to scale */
button[kind="secondary"] * {
    font-size: 36px !important;
    line-height: 1 !important;
}
/* Hover */
button[kind="secondary"]:hover {
    background-color: rgba(255,255,255,0.1) !important;
}

/* Disabled */
button[kind="secondary"]:disabled {
    opacity: 0.3 !important;
}
.navigation-bar {
   position: fixed !important;
   top: 0px !important;
   left: 20px !important;
   margin: 0 !important;
   padding: 0 !important;
   display: flex;
   align-items: flex-start !important;
   z-index: 9999;
   border-radius: -10px !important;
}
/* --- RADIO GROUP WRAPPER --- */
div[role="radiogroup"] {
    gap: 6px;
}

/* --- EACH OPTION ROW --- */
div[role="radiogroup"] > label {
    background-color: #1c1f2e;
    padding: 8px 12px !important;   /* ✅ smaller container */
    border-radius: 8px;
    border: 1px solid #2a3350;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
}

/* --- REMOVE BIG DEFAULT SPACING --- */
div[role="radiogroup"] label div {
    margin: 0 !important;
    padding: 0 !important;
}

/* --- TEXT STYLE --- */
div[role="radiogroup"] label p {
    font-size: 13px !important;   /* ✅ smaller text */
    line-height: 1.3;
    color: #e6e9f2;
    margin: 0;
}
/* --- RADIO BUTTON COLOR (BLUE) --- */
div[role="radiogroup"] input[type="radio"] {
    accent-color: #00c6ff !important;
    transform: scale(0.9);   /* ✅ slightly smaller */
    margin-right: 10px;
}
/* --- SELECTED ROW STYLE --- */
div[role="radiogroup"] label:has(input[type="radio"]:checked) {
    background-color: #213a63;
    border: 1px solid #00c6ff;
}
/* --- REMOVE STREAMLIT GREEN HIGHLIGHT --- */
div[data-testid="stMarkdownContainer"] mark {
    background: none !important;
    color: inherit !important;
}
/* 🔴 REMOVE the green highlight completely */
mark {
    background-color: transparent !important;
    color: inherit !important;
}

/* also target Streamlit container just in case */
div[data-testid="stMarkdownContainer"] mark {
    background-color: transparent !important;
    color: inherit !important;
}
<style>

/* Compact options */
div[role="radiogroup"] > label {
    padding: 8px 12px !important;
    border-radius: 8px;
    border: 1px solid #2a3350;
    margin-bottom: 6px;
    background-color: #1c1f2e;
    display: flex;
    align-items: center;
}

/* Smaller text */
div[role="radiogroup"] label p {
    font-size: 13px !important;
    margin: 0;
}

/* Blue radio */
div[role="radiogroup"] input[type="radio"] {
    accent-color: #00c6ff !important;
    transform: scale(0.9);
}

/* Selected row */
div[role="radiogroup"] label:has(input[type="radio"]:checked) {
    background-color: #213a63;
    border: 1px solid #00c6ff;
}
</style>
""", unsafe_allow_html=True)
questions_data = load_questions()
dimensions = get_dimension_list()
# ── Session-state defaults ────────────────────────────────────────────────────
if "selected_dimension" not in st.session_state:
   st.session_state.selected_dimension = 0
if "current_original_number" not in st.session_state:
   st.session_state.current_original_number = 1
if "answers" not in st.session_state:
   st.session_state.answers = {}
# ── Build CANONICAL question list (fixed order, never rotated) ───────────────
all_questions = []
counter = 1

for dim, q_list in questions_data.items():
    for q in q_list:
        q["original_number"] = counter
        all_questions.append({
                "question": q,
                "dimension": dim,
                "original_number": counter
            })
        counter += 1
total_questions = len(all_questions)
# ── Handle ?q= query-param (tab clicks) ──────────────────────────────────────
query_params = st.query_params
# Handle back icon click
if "nav" in query_params: 
    if query_params["nav"] == "home":
        st.switch_page("pages/assessment_home.py")
if "q" in query_params:
   raw = query_params["q"]
   if isinstance(raw, list):
       raw = raw[0]
   try:
       qnum = int(raw)
   except (ValueError, TypeError):
       qnum = None
   if qnum is not None and 1 <= qnum <= total_questions:
       if qnum != st.session_state.current_original_number:
           st.session_state.current_original_number = qnum
           st.rerun()
# ── Jump to first question of selected dimension (from Assessment Home) ───────
selected_dim_idx = st.session_state.selected_dimension
if selected_dim_idx > 0 and st.session_state.current_original_number == 1:
   chosen_dim_name = dimensions[selected_dim_idx] if selected_dim_idx < len(dimensions) else None
   if chosen_dim_name:
       for entry in all_questions:
           if entry["dimension"] == chosen_dim_name:
               st.session_state.current_original_number = entry["original_number"]
               break
   # ✅ Reset selected dimension so it only applies once
   st.session_state.selected_dimension = 0
# ── Resolve active question ───────────────────────────────────────────────────
cur_num = max(1, min(st.session_state.current_original_number, total_questions))
st.session_state.current_original_number = cur_num
active_entry = all_questions[cur_num - 1]
question     = active_entry["question"]
dimension    = active_entry["dimension"]
# ── HEADER ROW ────────────────────────────────────────────────────────────────
st.markdown(f"""
        <div style="
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 9999;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 16px;
        ">
            <a href="?nav=home" target="_self">
                <img src="data:image/png;base64,{back_icon_data}" width="30"/>
            </a>
            <img src="data:image/png;base64,{logo_image_data}" width="40"/>
        </div>
        <div style="height:50px;"></div>
    """, unsafe_allow_html=True)
#-------------------------------------------------------------------------------------
c3, c4 = st.columns([3.5, 1.5])
with c3:
    sub_dimension = question.get("sub_dimension", "")

    st.markdown(f"""
    <div style="
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-bottom: 0px;
        margin-left: 20px;
        padding-top: 0px;
        margin-top: -30px;   /* ✅ pull it UP (key fix) */
    ">
        <!-- Dimension (small label) -->
        <div style="
            font-size:16px;
            font-weight:900;
            color:rgb(18, 171, 219);
            opacity:1;
            filter:none;
            text-transform:uppercase;
            letter-spacing:0.5px;
            margin-bottom:6px;
        ">
            {dimension}
        </div>
        <!-- Sub-dimension (main title) -->
        <div style="
            font-size: 25px;
            font-weight: 800;
            color: #FFFFFF;
            line-height: 1.2;
        ">
            {sub_dimension}
        </div>
    </div>
    """, unsafe_allow_html=True)
with c4:
   # Build set of answered question numbers for green highlighting
   answered_nums = set()
   for entry in all_questions:
       q_key = (entry["dimension"], entry["question"]["question"])
       if q_key in st.session_state.answers:
           answered_nums.add(entry["original_number"])
   tabs_html_items = ""
   for entry in all_questions:
       onum      = entry["original_number"]
       is_active = onum == cur_num
       is_answered = onum in answered_nums
       active_id = 'id="active-question-tab"' if is_active else ""
       # Priority: active > answered > default
       if is_active:
           bg     = "#00c6ff"
           color  = "#071b3a"
           border = "2px solid #ffffff"
       elif is_answered:
           bg     = "#1b6e00"
           color  = "#ffffff"
           border = "1px solid #3ddc00"
       else:
           bg     = "#0f2f5f"
           color  = "#ffffff"
           border = "1px solid #1f5fa3"
    #    tabs_html_items += (
    #        f'<div {active_id} title="Question {onum}" '
    #     #    f'onclick="window.parent.postMessage({{isStreamlitMessage: true, type: \'streamlit:setComponentValue\', value: {onum}}}, \'*\')"'
    #        f'onclick="window.location.search='?q={onum}'"'
    #        f'style="background-color:{bg};color:{color};'
    #        f'padding:6px 10px;border-radius:10px;min-width:42px;width:42px;height:38px;'
    #        f'line-height:20px;display:inline-flex;align-items:center;justify-content:center;'
    #        f'text-align:center;font-weight:600;font-size:12px;border:{border};'
    #        f'flex:0 0 auto;white-space:nowrap;font-family:Segoe UI,sans-serif;cursor:pointer;">'
    #        f'Q{onum}</div>'
    #    )
       tabs_html_items += (
    f'<div {active_id} title="Question {onum}" '
    f'onclick="window.location.search=\'?q={onum}\'" '
    f'style="background-color:{bg};color:{color};'
    f'padding:6px 10px;border-radius:10px;min-width:42px;width:42px;height:38px;'
    f'line-height:20px;display:inline-flex;align-items:center;justify-content:center;'
    f'text-align:center;font-weight:600;font-size:12px;border:{border};'
    f'flex:0 0 auto;white-space:nowrap;font-family:Segoe UI,sans-serif;cursor:pointer;">'
    f'Q{onum}</div>'
)
   component_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
 * {{ margin: 0; padding: 0; box-sizing: border-box; }}
 body {{ background: transparent; overflow: hidden; }}
 /* Outer framed box */
 #tabs-box {{
   background: rgba(15, 47, 95, 0.55);
   border: 1px solid rgba(0, 198, 255, 0.30);
   border-radius: 14px;
   padding: 7px 10px 6px 10px;
   box-shadow: 0 2px 12px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06);
 }}
 /* Scrollable inner strip */
 #scroll-container {{
   width: 100%;
   overflow-x: scroll;
   display: flex;
   align-items: center;
   padding-bottom: 7px;
   scrollbar-width: auto;
   scrollbar-color: #00c6ff rgba(0, 80, 160, 0.55);
 }}
 /* Chrome / Safari / Edge scrollbar */
 #scroll-container::-webkit-scrollbar {{ height: 8px; display: block; }}
 #scroll-container::-webkit-scrollbar-track {{
   background: rgba(0, 80, 160, 0.55);
   border-radius: 8px;
   border: 1px solid rgba(0, 198, 255, 0.20);
 }}
 #scroll-container::-webkit-scrollbar-thumb {{
   background: linear-gradient(90deg, #0077b6 0%, #00c6ff 100%);
   border-radius: 8px;
   border: 1px solid rgba(255,255,255,0.25);
   min-width: 28px;
 }}
 #scroll-container::-webkit-scrollbar-thumb:hover {{
   background: linear-gradient(90deg, #00c6ff 0%, #ffffff 100%);
 }}
 #tabs-row {{
   display: flex;
   gap: 6px;
   min-width: max-content;
 }}
</style>
</head>
<body>
<div id="tabs-box">
<div id="scroll-container">
<div id="tabs-row">
       {tabs_html_items}
</div>
</div>
</div>
<script>
(function() {{

  // ✅ Navigate using query param (most reliable)
  function navigateTo(qnum) {{
    try {{
      var base = window.parent.location.href.split('?')[0];
      window.parent.location.href = base + '?q=' + qnum;
    }} catch (e) {{
      window.location.search = '?q=' + qnum;
    }}
  }}

  // ✅ Attach click handlers AFTER DOM loads
  window.addEventListener("load", function() {{

    var tabs = document.querySelectorAll('#tabs-row div');

    for (var i = 0; i < tabs.length; i++) {{

      tabs[i].addEventListener('click', function() {{

        var q = this.getAttribute('data-q');

        // ✅ Use navigation (NO postMessage complexity)
        navigateTo(q);

      }});
    }}

  }});

  // ✅ Scroll active tab into view
  function centerActiveTab() {{
    var container = document.getElementById('scroll-container');
    var active    = document.getElementById('active-question-tab');
    if (!container || !active) return;

    var cw = container.clientWidth;
    var tw = active.offsetWidth;
    var al = active.offsetLeft;

    container.scrollLeft = al - (cw / 2) + (tw / 2);
  }}

  centerActiveTab();
  setTimeout(centerActiveTab, 100);
  setTimeout(centerActiveTab, 300);

}})();
</script>
</body>
</html>
"""
   # height: tab pill (38) + scrollbar (8) + box padding (13) + buffer (9)
   clicked_q=components.html(component_html, height=74 , scrolling=False)
   
if clicked_q:
    try:
        qnum = int(clicked_q)
        if 1 <= qnum <= total_questions:
            st.session_state.current_original_number = qnum
            st.rerun()
    except:
        pass
# Full-width grey box — question text only, single line with ellipsis
#---------old----
# st.markdown(
#    f'<div class="question-box"><div class="q-text" title="{question["question"]}">Q{cur_num}.&nbsp;&nbsp;{question["question"]}</div></div>',
#    unsafe_allow_html=True,
# )
#---------new (with more spacing and better styling)----
st.markdown(
    f"""
    <div style="
        background: rgba(242, 242, 242, 0.7);
        padding: 16px 20px;
        border-radius: 0px;
        position: relative;
        margin-top: 10px;
        margin-bottom: 20px;
        font-size: 16px;
        font-weight: 600;        
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw
        width: 100vw;
        color: RGBA(0, 56, 87, 1);
    ">
        <b>Q{cur_num}.</b>&nbsp;&nbsp;{question["question"]}
    </div>
    """,
    unsafe_allow_html=True,
)
# ── Options as radio buttons ──────────────────────────────────────────────────
o1,o2,o3 = st.columns([0.5,10,0.5])
with o2:
    options      = question["options"]
    option_items = list(reversed(list(options.items())))
    display_options = [text for _, text in option_items]
    question_key = (dimension, question["question"])
    radio_key = f"radio_{cur_num}"

    # ✅ Get saved score (if any)
    saved_score = st.session_state.answers.get(question_key, None)

    # ✅ Build mapping
    score_to_label = {score: text for score, text in option_items}
    label_to_score = {text: score for score, text in option_items}

    # ✅ Restore ONLY if not already set (critical fix)
    if radio_key not in st.session_state:
        if saved_score is not None:
            st.session_state[radio_key] = score_to_label[saved_score]
        else:
            st.session_state[radio_key] = None  # ✅ no default selection

    
    selected_label = st.radio(
        "",
        options=[text for _, text in option_items],
        key=radio_key,
        label_visibility="collapsed",
    )
    # ✅ Save answer ONLY when user selects something
    if selected_label is not None:
        st.session_state.answers[question_key] = label_to_score[selected_label]
# ── Bottom navigation — centred icon-only buttons ─────────────────────────────
_, nav_col, _ = st.columns([1.5, 1, 1.5])

with nav_col:
    warning_placeholder = st.empty()   # ✅ placeholder for full-width warning

    left_spacer, b_col, mid_spacer, n_col, right_spacer = st.columns([1, 2, 4, 2, 1])

    with b_col:
        #back_clicked = st.button("⬅", key="back_button", disabled=(cur_num == 1))
        st.markdown('<div style="display:flex; justify-content:flex-start;">', unsafe_allow_html=True)
        back_clicked = st.button("←", key="back_button",type="secondary", disabled=(cur_num == 1))
        st.markdown('</div>', unsafe_allow_html=True)
        if back_clicked:
            st.session_state.current_original_number = cur_num - 1
            st.rerun()

    with n_col:
        # is_last = cur_num >= total_questions
        # button_label = "✅" if is_last else "➡"
        # next_clicked = st.button(button_label, key="next_button")
        
        st.markdown('<div style="display:flex; justify-content:flex-end;">', unsafe_allow_html=True)
        is_last = cur_num >= total_questions
        button_label = "✅" if is_last else "→"
        next_clicked = st.button(button_label, key="next_button",type="secondary")
        st.markdown('</div>', unsafe_allow_html=True)
        if next_clicked:
            if is_last:
                answered = len(st.session_state.answers)

                # if answered < total_questions:
                #     warning_placeholder.markdown(
                #         f"""
                #         <div style="
                #             background-color:#fff3cd;
                #             color:#664d03;
                #             padding:4px 12px;
                #             border-radius:5px;
                #             border:1px solid #ffecb5;
                #             width:100%;
                #             text-align:center;
                #             font-weight:600;
                #             margin:5px 0;
                #         ">
                #             ⚠️ Please answer all questions before submitting ({answered}/{total_questions} completed)
                #         </div>
                #         """,
                #         unsafe_allow_html=True
                #     )
                # else:
                st.switch_page("pages/score.py")
            else:
                st.session_state.current_original_number = cur_num + 1
                st.rerun()
