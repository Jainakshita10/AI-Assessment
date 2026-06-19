# questionnaire.py
import base64

import streamlit as st
import streamlit.components.v1 as components
from questions import load_questions, get_dimension_list

with open("media/logo.png", "rb") as f:
    logo_image_data = base64.b64encode(f.read()).decode()

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
        scrollbar-height: none;
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
/* ================= NAV BUTTONS ================= */
.st-key-navigation_back_btn button {
   background: transparent !important;
   border-radius: 50%;
    border: 2px solid #9ca3af !important;
    color: white !important;
    width: 35px;
    height: 35px;
    font-size: 30px !important;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 !important;
    margin-top: -5px !important;
}
.st-key-navigation_back_btn button p {
    font-size: 30px !important;
    margin: 0 !important;
    line-height: 1 !important;
}
.st-key-navigation_next_btn button {
   background: transparent !important;
   border-radius: 50%;
    border: 2px solid #9ca3af !important;
    color: white !important;
    width: 35px;
    height: 35px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 !important;
    margin-top: -5px !important;
}
.st-key-navigation_next_btn button p {
    font-size: 30px !important;
    margin: 0 !important;
    line-height: 1 !important;
}
.st-key-submit_btn button {
   border-radius: 6px !important;
    width: 20 !important;
    height: 20 !important;
    padding: 8px 18px !important;
    background-color: #2f66d0 !important;
    font-size: 14px !important;
    font-weight: 600;
    border: 1px solid #9ca3af !important;
    float: left
    margin-top: -100px;
    display: flex;
}
.st-key-home_btn button {
   background: transparent !important;
   border-radius: 50%;
    border: 2px solid #9ca3af !important;
    color: white !important;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 !important;
}
/* ================= RADIO GROUP ================= */
div[data-testid="stRadio"] {
    margin: 0 !important;
    padding: 0 !important;
}
div[data-testid="stRadio"] > div:first-child {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
    width: 100% !important;
}
/* Hide empty wrapper label */
div[data-testid="stRadio"] > label {
    display: none !important;
}
/* Radiogroup layout */
div[data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column;
    gap: 6px;
    width: 100%;
}
/* ================= RADIO OPTION ================= */
div[data-testid="stRadio"] label {
    position: relative;
    width: 100% !important;

    display: flex;
    align-items: center;
    gap: 5px;

    padding: 8px 14px !important;
    min-height: 28px;

    font-size: 12px;
    font-weight: 400;

    color: #ffffff !important;
    background: #1a1a2e;
    border: 1px solid #2e2e4a;
    border-radius: 8px;

    cursor: pointer;
    transition: all 0.2s ease;
}
/* Hover */
div[data-testid="stRadio"] label:hover {
    background: #252540;
    border-color: #4a4a7a;
}
/* Selected */
div[data-testid="stRadio"] label:has(input[type="radio"]:checked) {
    background: #213a63;
    border-color: #00c6ff;
}
/* Text + icons */
div[data-testid="stRadio"] label * {
    color: #ffffff !important;
    fill: #ffffff !important;
}
/* ================= RADIO INPUT ================= */
div[data-testid="stRadio"] input[type="radio"] {
    accent-color: #00c6ff !important;
    transform: scale(0.9);
    margin-right: 10px;
}
/* Remove extra spacing inside */
div[data-testid="stRadio"] label div,
div[data-testid="stRadio"] label p {
    margin: 0 !important;
    padding: 0 !important;
    font-size: 11px;
}
/* ================= REMOVE MARK HIGHLIGHT ================= */
mark,
div[data-testid="stMarkdownContainer"] mark {
    background: transparent !important;
    color: inherit !important;
}
/* ================= TEXT AREA STYLING ================= */
.stTextArea textarea {
    background-color: #1a1a2e !important;
    color: #ffffff !important;
    border: 1px solid #2e2e4a !important;
    border-radius: 8px !important;
    padding: 12px 14px !important;
    font-size: 13px !important;
    font-family: 'Segoe UI', sans-serif !important;
    transition: all 0.2s ease !important;
    margin-bottom: -10px;
    height: 30px;
}
.stTextArea textarea:focus {
    border-color: #00c6ff !important;
    box-shadow: 0 0 0 2px rgba(0, 198, 255, 0.1) !important;
    outline: none !important;
}
.stTextArea textarea::placeholder {
    color: #6b7280 !important;
}
</style>
""", unsafe_allow_html=True)
# ── Dimension heading (outside box) + compact grey question box ───────────────
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
   # ✅ Consume the param immediately so it can't override Next/Back later
   del st.query_params["q"]
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
# st.markdown(f"""
#         <div style="
#             position: fixed;
#             top: 0;
#             left: 0;
#             width: 100%;
#             z-index: 9999;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             padding: 8px 16px;
#         ">
#             <a href="?nav=home" target="_self">
#                 <img src="data:image/png;base64,{back_icon_data}" width="30"/>
#             </a>
#             <img src="data:image/png;base64,{logo_image_data}" width="40"/>
#         </div>
#         <div style="height:50px;"></div>
#     """, unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns([2, 10])

    with col1:
        if st.button("❮", key="home_btn"):
            st.switch_page("pages/assessment_home.py")  # 👈 update path to your home page   
    with col2:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: flex-end;">
                <img src="data:image/png;base64,{logo_image_data}" width="40">
            </div>
            """,
            unsafe_allow_html=True
        )
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
        margin-left: 50px;
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

   # Tabs are NATIVE Streamlit buttons (not anchor links). A button click
   # triggers a soft rerun that PRESERVES st.session_state — unlike an
   # <a href> link, which does a full page reload and wipes session state
   # (that was wiping previously answered questions). Each button is keyed,
   # so Streamlit adds a `st-key-qtab_<n>` class we use to colour each pill.
   per_tab_css = ""
   for entry in all_questions:
       onum        = entry["original_number"]
       is_active   = onum == cur_num
       is_answered = onum in answered_nums
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
       per_tab_css += (
           f".st-key-qtab_{onum} button {{"
           f"background-color:{bg} !important;"
           f"color:{color} !important;"
           f"border:{border} !important;}}"
           f".st-key-qtab_{onum} button p {{color:{color} !important;}}"
       )

   st.markdown(
       f"""
<style>
/* Outer framed box (keyed container) */
.st-key-qtabs {{
   background: rgba(15, 47, 95, 0.55);
   border: 1px solid rgba(0, 198, 255, 0.30);
   border-radius: 14px;
   padding: 7px 10px 6px 10px;
   box-shadow: 0 2px 12px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06);
}}
/* Horizontal scrollable strip of pills */
.st-key-qtabs div[data-testid="stHorizontalBlock"] {{
   flex-wrap: nowrap !important;
   overflow-x: scroll;
   align-items: center;
   gap: 6px !important;
   padding-bottom: 7px;
   scrollbar-width: auto;
   scrollbar-color: #00c6ff rgba(0, 80, 160, 0.55);
}}
.st-key-qtabs div[data-testid="stHorizontalBlock"]::-webkit-scrollbar {{ height: 8px; display: block; }}
.st-key-qtabs div[data-testid="stHorizontalBlock"]::-webkit-scrollbar-track {{
   background: rgba(0, 80, 160, 0.55);
   border-radius: 8px;
   border: 1px solid rgba(0, 198, 255, 0.20);
}}
.st-key-qtabs div[data-testid="stHorizontalBlock"]::-webkit-scrollbar-thumb {{
   background: linear-gradient(90deg, #0077b6 0%, #00c6ff 100%);
   border-radius: 8px;
   border: 1px solid rgba(255,255,255,0.25);
   min-width: 28px;
}}
.st-key-qtabs div[data-testid="stHorizontalBlock"]::-webkit-scrollbar-thumb:hover {{
   background: linear-gradient(90deg, #00c6ff 0%, #ffffff 100%);
}}
/* Each column holds one pill — keep fixed width, no shrink */
.st-key-qtabs div[data-testid="stColumn"] {{
   min-width: 42px !important;
   width: 42px !important;
   flex: 0 0 auto !important;
}}
.st-key-qtabs div[data-testid="stColumn"] > div {{ width: 42px !important; }}
/* Pill geometry (shared by all tab buttons) */
.st-key-qtabs .stButton {{ width: 42px !important; }}
.st-key-qtabs .stButton button {{
   min-width: 42px !important;
   width: 42px !important;
   height: 38px !important;
   padding: 6px 10px !important;
   border-radius: 10px !important;
   font-weight: 600 !important;
   font-size: 12px !important;
   line-height: 20px !important;
   display: flex !important;
   align-items: center !important;
   justify-content: center !important;
   white-space: nowrap !important;
   margin: 0 !important;
   transition: transform 0.2s ease, background-color 0.2s ease !important;
}}
/* Force the inner label text size/weight (overrides global button * rules) */
.st-key-qtabs .stButton button p,
.st-key-qtabs .stButton button div,
.st-key-qtabs .stButton button span,
.st-key-qtabs .stButton button * {{
   font-size: 12px !important;
   font-weight: 600 !important;
   line-height: 20px !important;
   margin: 0 !important;
}}
.st-key-qtabs .stButton button:hover {{ transform: scale(1.03) !important; }}
{per_tab_css}
</style>
""",
       unsafe_allow_html=True,
   )

   tabs_container = st.container(key="qtabs")
   with tabs_container:
       cols = st.columns(total_questions, gap="small")
       for entry, col in zip(all_questions, cols):
           onum = entry["original_number"]
           with col:
               if st.button(f"Q{onum}", key=f"qtab_{onum}"):
                   st.session_state.current_original_number = onum
                   st.rerun()

   # Zero-height helper iframe: only scrolls the active tab into view inside
   # the parent page's scroll container. DOM access to the parent is allowed
   # (allow-same-origin); navigation now happens via buttons, not the iframe.
   components.html(
       f"""
<script>
  function centerActiveTab() {{
    try {{
      var pdoc = window.parent.document;
      var box = pdoc.querySelector('.st-key-qtabs');
      if (!box) return;
      var c = box.querySelector('div[data-testid="stHorizontalBlock"]');
      var a = box.querySelector('.st-key-qtab_{cur_num}');
      if (!c || !a) return;
      var cr = c.getBoundingClientRect();
      var ar = a.getBoundingClientRect();
      c.scrollLeft += (ar.left - cr.left) - (c.clientWidth / 2) + (a.offsetWidth / 2);
    }} catch (e) {{}}
  }}
  centerActiveTab();
  setTimeout(centerActiveTab, 100);
  setTimeout(centerActiveTab, 300);
</script>
""",
       height=0,
   )
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
        padding: 8px 10px;
        border-radius: 0px;
        position: relative;
        margin-top: -20px;
        margin-bottom: 5px;
        font-size: 16px;
        font-weight: 600;        
        left: 50%;
        right: 50%;
        margin-left: -50vw;
        margin-right: -50vw;
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
    text_key = f"text_{cur_num}"

    # ✅ Get saved answer (if any) - supports both radio and text
    saved_answer = st.session_state.answers.get(question_key, None)

    # ✅ Build mapping for radio options
    score_to_label = {score: text for score, text in option_items}
    label_to_score = {text: score for score, text in option_items}

    # ✅ Restore ONLY if not already set (critical fix)
    if radio_key not in st.session_state:
        if saved_answer is not None and isinstance(saved_answer, dict) and saved_answer.get("type") == "radio":
            st.session_state[radio_key] = score_to_label.get(saved_answer.get("value"))
        else:
            st.session_state[radio_key] = None  # ✅ no default selection
    
    if text_key not in st.session_state:
        if saved_answer is not None and isinstance(saved_answer, dict) and saved_answer.get("type") == "text":
            st.session_state[text_key] = saved_answer.get("value", "")
        else:
            st.session_state[text_key] = ""

    selected_label = st.radio(
        "",
        options=[text for _, text in option_items],
        key=radio_key,
        label_visibility="collapsed",
    )
    
    # # ✅ Radio selection clears text area
    # if selected_label is not None:
    #     st.session_state.answers[question_key] = {"type": "radio", "value": label_to_score[selected_label]}
    #     st.session_state[text_key] = ""  # Clear text input when radio is selected
    #selected_label = st.radio(...)
    # ── Text area for custom answer ───────────────────────────────────────────
    #st.markdown("<div style='margin-top: 0px;'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 13px; color: #9ca3af; margin-top: 5px; margin-bottom: 0px;'><b>Or write your own answer:</b></div>", unsafe_allow_html=True)
    
    text_answer = st.text_area(
        "",
        value=st.session_state[text_key],
        key=text_key,
        height=30,
        placeholder="Type your response here...",
        label_visibility="collapsed"
    )
    
    # ✅ Text input clears radio selection
        
    # ✅ Move this ABOVE st.radio()
    # if text_key in st.session_state and st.session_state[text_key].strip():
    #     st.session_state[radio_key] = None

    # elif not text_answer.strip() and selected_label is None:
    #     # ✅ If both are empty, remove the answer
    #     if question_key in st.session_state.answers:
    #         del st.session_state.answers[question_key]
    
    # ✅ Handle answer persistence correctly
    if text_answer.strip():
        # Custom text takes priority
        st.session_state.answers[question_key] = {
            "type": "text",
            "value": text_answer.strip()
        }

    elif selected_label is not None:
        # Radio answer
        st.session_state.answers[question_key] = {
            "type": "radio",
            "value": label_to_score[selected_label]
        }

    else:
        # Neither selected → remove answer
        if question_key in st.session_state.answers:
            del st.session_state.answers[question_key]
    
    st.markdown("</div>", unsafe_allow_html=True)
# ── Bottom navigation — centred icon-only buttons ─────────────────────────────
_, nav_col, _ = st.columns([1.5, 1, 1.5])

with nav_col:
    warning_placeholder = st.empty()

    # ✅ Special layout for first question
    if cur_num == 1:
        left_spacer, center_col, right_spacer = st.columns([1, 2, 1])

        with center_col:
            #st.markdown('<div style="display:flex; justify-content:center;">', unsafe_allow_html=True)

            all_answered = len(st.session_state.answers) == total_questions
            is_last_question = cur_num == total_questions
            show_submit = all_answered or is_last_question

            button_label = "Submit" if show_submit else "→"

            # if button_label == 'Submit':
            #     next_clicked = st.button(button_label, key="submit_button", type="secondary")
            
            if show_submit:
                next_clicked = st.button("Submit", key="submit_btn")

            else:
                next_clicked = st.button(button_label, key="navigation_next_btn")

            #st.markdown('</div>', unsafe_allow_html=True)

    else:
        # ✅ Normal layout for other questions
        #left_spacer, b_col, mid_spacer, n_col, right_spacer = st.columns([1, 2, 4, 4, 1])
        left_spacer, b_col, n_col, right_spacer = st.columns([1, 2, 2, 1])

        with b_col:
            #st.markdown('<div style="display:flex; justify-content:flex-start;">', unsafe_allow_html=True)
            back_clicked = st.button("←", key="navigation_back_btn")
            #st.markdown('</div>', unsafe_allow_html=True)

            if back_clicked:
                st.session_state.current_original_number = cur_num - 1
                st.rerun()

        with n_col:
            #st.markdown('<div style="display:flex; justify-content:flex-end;">', unsafe_allow_html=True)

            all_answered = len(st.session_state.answers) == total_questions
            is_last_question = cur_num == total_questions
            show_submit = all_answered or is_last_question

            button_label = "Submit" if show_submit else "→"

            # if button_label == 'Submit':
            #     next_clicked = st.button(button_label, key="submit_button", type="secondary")
            
            if show_submit:
                next_clicked = st.button("Submit", key="submit_btn")

            else:
                next_clicked = st.button(button_label, key="navigation_next_btn")

            #st.markdown('</div>', unsafe_allow_html=True)

    # ✅ Shared click logic (outside layout)
    if next_clicked:
    
        # ✅ STEP 5: VALIDATION HERE
        has_radio = selected_label is not None
        has_text = text_answer.strip() != ""

        if not (has_radio or has_text):
            warning_placeholder.markdown(
                """
                <div style="
                    background-color:#fff3cd;
                    color:#664d03;
                    padding:4px 12px;
                    border-radius:5px;
                    border:1px solid #ffecb5;
                    width:100%;
                    text-align:center;
                    font-weight:600;
                    margin:5px 0;
                ">
                    ⚠️ Please answer this question before continuing
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        # ✅ EXISTING LOGIC continues ONLY if valid
        if show_submit:
            if all_answered:
                st.switch_page("pages/score.py")
            else:
                answered = len(st.session_state.answers)
                warning_placeholder.markdown(
                    f"""
                    <div style="
                        background-color:#fff3cd;
                        color:#664d03;
                        padding:4px 12px;
                        border-radius:5px;
                        border:1px solid #ffecb5;
                        width:100%;
                        text-align:center;
                        font-weight:600;
                        margin:5px 0;
                    ">
                        ⚠️ Please answer all the questions
                        ({answered}/{total_questions} completed)
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            if cur_num < total_questions:
                st.session_state.current_original_number = cur_num + 1
                st.rerun()
