# questionnaire.py
import base64

import streamlit as st
import streamlit.components.v1 as components
from questions import load_questions, get_dimension_list
from ui_style import apply_global_style

with open("media/logo.png", "rb") as f:
    logo_image_data = base64.b64encode(f.read()).decode()

apply_global_style()

st.markdown("""
<style>

.logo-container {

    position: fixed !important;

    top: 5px;

    right: 5px;

    z-index: 999;

}

.logo-container img {

    width: 35px !important;

    height: auto !important;

}
</style>

""", unsafe_allow_html=True)
# ── Dimension heading (outside box) + compact grey question box ───────────────
st.markdown("""
<style>
/* Full-width grey question container */
.question-box {
   background: #c8c8d0;
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
   width: 70% !important;
   min-height: 34px !important;
   padding: 6px 14px !important;
   font-size: 12px !important;
   border-radius: 8px !important;
   justify-content: flex-start !important;
   margin-bottom: 0 !important;
   background: #1a1a2e !important;
   border: 1px solid #2e2e4a !important;
   color: #e8e8f0 !important;
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
   width: 48px !important;
   height: 48px !important;
   border-radius: 50% !important;
   padding: 0 !important;
   font-size: 22px !important;
   display: flex !important;
   align-items: center !important;
   justify-content: center !important;
   min-width: 0 !important;
}
.navigation-bar {
   position: fixed !important;
   top: 20px !important;
   left: 20px !important;
   margin: 0 !important;
   padding: 0 !important;
   display: flex;
   align-items: flex-start !important;
   z-index: 9999;
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
for dim in dimensions:
   for q in questions_data.get(dim, []):
       q["original_number"] = counter
       all_questions.append({"question": q, "dimension": dim, "original_number": counter})
       counter += 1
total_questions = len(all_questions)
# ── Handle ?q= query-param (tab clicks) ──────────────────────────────────────
query_params = st.query_params
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
# ── Resolve active question ───────────────────────────────────────────────────
cur_num = max(1, min(st.session_state.current_original_number, total_questions))
st.session_state.current_original_number = cur_num
active_entry = all_questions[cur_num - 1]
question     = active_entry["question"]
dimension    = active_entry["dimension"]
# ── HEADER ROW ────────────────────────────────────────────────────────────────
c1, c2 = st.columns([4, 1])
with c1:
   st.markdown("<div class='navigation-bar'>", unsafe_allow_html=True)
   back_home = st.button("⬅", key="back_home_button")
   if back_home:
       st.session_state.selected_dimension = 0
       st.session_state.current_original_number = 1
       st.switch_page("pages/assessment_home.py")
#    st.markdown("</div>", unsafe_allow_html=True)
   # Dimension as plain heading outside the box
   st.markdown(f"## {dimension}")
# ── TAB BAR — rendered via components.html so <script> actually executes ─────
with c2:
   st.markdown(
    f"""
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_image_data}">
    </div>
    """,
    unsafe_allow_html=True
    )
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
   clicked_q=components.html(component_html, height=74, scrolling=False)
   
if clicked_q:
    try:
        qnum = int(clicked_q)
        if 1 <= qnum <= total_questions:
            st.session_state.current_original_number = qnum
            st.rerun()
    except:
        pass
# Full-width grey box — question text only, single line with ellipsis
st.markdown(
   f'<div class="question-box"><div class="q-text" title="{question["question"]}">Q{cur_num}.&nbsp;&nbsp;{question["question"]}</div></div>',
   unsafe_allow_html=True,
)
# ── Options as radio buttons ──────────────────────────────────────────────────
options      = question["options"]
option_items = list(reversed(list(options.items())))
display_options = [text for _, text in option_items]
question_key   = (dimension, question["question"])
selected_score = st.session_state.answers.get(question_key, None)
selected_index = None  # no default pre-selection
if selected_score is not None:
   for idx, (score, _) in enumerate(option_items):
       if score == selected_score:
           selected_index = idx
           break
selected_label = st.radio(
   "",
   options=display_options,
   index=selected_index,
   key=f"radio_{cur_num}",
   label_visibility="collapsed",
)
if selected_label is not None:
   selected_score = option_items[[text for _, text in option_items].index(selected_label)][0]
   st.session_state.answers[question_key] = selected_score
# ── Bottom navigation — centred icon-only buttons ─────────────────────────────
_, nav_col, _ = st.columns([2, 1, 2])
with nav_col:
   b_col, n_col = st.columns(2)
   with b_col:
       back_clicked = st.button("⬅", key="back_button", disabled=(cur_num == 1))
       if back_clicked:
           st.session_state.current_original_number = cur_num - 1
           st.rerun()
   with n_col:
       is_last      = cur_num >= total_questions
       button_label = "✅" if is_last else "➡"
       next_clicked = st.button(button_label, key="next_button")
       if next_clicked:
           if is_last:
               answered = len(st.session_state.answers)
               if answered < total_questions:
                   st.warning(
                       f"Please answer all questions before submitting "
                       f"({answered}/{total_questions} completed)"
                   )
               else:
                   st.switch_page("pages/score.py")
           else:
               st.session_state.current_original_number = cur_num + 1
               st.rerun()