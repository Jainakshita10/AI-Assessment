# questionnaire.py

import streamlit as st
from questions import load_questions, get_dimension_list
from ui_style import apply_global_style

apply_global_style()

questions_data = load_questions()
dimensions = get_dimension_list()

if "selected_dimension" not in st.session_state:
    st.session_state.selected_dimension = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# Build an ordered list of all questions starting from the selected dimension.
selected_dim = st.session_state.selected_dimension
if 0 <= selected_dim < len(dimensions):
    ordered_dimensions = dimensions[selected_dim:] + dimensions[:selected_dim]
else:
    ordered_dimensions = dimensions

ordered_questions = []
ordered_question_dimensions = []
for dimension in ordered_dimensions:
    for q in questions_data.get(dimension, []):
        ordered_questions.append(q)
        ordered_question_dimensions.append(dimension)

if st.session_state.question_index >= len(ordered_questions):
    st.session_state.question_index = 0

# Handle query param navigation for question tabs
query_params = st.query_params
if "q" in query_params:
    clicked_q = query_params["q"]
    if isinstance(clicked_q, list):
        clicked_q = clicked_q[0]
    try:
        clicked_q = int(clicked_q)
    except (ValueError, TypeError):
        clicked_q = None
    if clicked_q is not None and 0 <= clicked_q < len(ordered_questions) and clicked_q != st.session_state.question_index:
        st.session_state.question_index = clicked_q
        st.rerun()

q_index = st.session_state.question_index
question = ordered_questions[q_index]

dimension = ordered_question_dimensions[q_index]

# HEADER + QUESTION TAB BAR
st.markdown("<div class='navigation-bar'>", unsafe_allow_html=True)
back_home = st.button("⬅", key="back_home_button")
if back_home:
    st.switch_page("pages/assessment_home.py")
st.markdown("</div>", unsafe_allow_html=True)

top_cols = st.columns([4, 1])
with top_cols[0]:
    st.markdown(f"## {dimension}")
    st.markdown(f"### Q{q_index + 1}. {question['question']}")

with top_cols[1]:
    tab_html = "<div class='tabs-wrapper-container'><div class='tabs-wrapper'>"
    for i in range(len(ordered_questions)):
        active = "active-tab" if i == q_index else ""
        tab_html += (
            f'<a href="?q={i}" target="_self">'
            f'<div class="question-tab {active}" title="Question {i+1}">Q{i+1}</div>'
            f'</a>'
        )
    tab_html += "</div></div>"
    st.markdown(tab_html, unsafe_allow_html=True)

# ✅ OPTIONS AS RADIO BUTTONS
options = question["options"]
option_items = list(reversed(list(options.items())))

# Create display options with placeholder
placeholder = "- Select an option -"
display_options = [placeholder] + [text for _, text in option_items]

question_key = (dimension, question["question"])
selected_score = st.session_state.answers.get(question_key, None)
selected_index = 0

# Only set index if an answer already exists for this question
if selected_score is not None:
    for index, (score, _) in enumerate(option_items):
        if score == selected_score:
            selected_index = index + 1  # +1 because of placeholder
            break

selected_label = st.radio(
    "",
    options=display_options,
    index=selected_index,
    key=f"{dimension}_{q_index}_radio",
)

# Map selected label back to the internal score value (only if not placeholder)
if selected_label != placeholder:
    selected_score = option_items[[text for _, text in option_items].index(selected_label)][0]
    st.session_state.answers[question_key] = selected_score
elif question_key in st.session_state.answers:
    # Clear the answer if placeholder is selected
    del st.session_state.answers[question_key]

# NAVIGATION
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    back_clicked = st.button("⬅ Back", key="back_button", disabled=(q_index == 0))
    if back_clicked:
        st.session_state.question_index = q_index - 1
        st.rerun()


with col3:
    is_last_question = q_index >= len(ordered_questions) - 1
    button_label = "Finish ✅" if is_last_question else "Next ➡"
    button_clicked = st.button(button_label, key="next_button")

    if button_clicked:
        if is_last_question:

            # ✅ NEW: validate all questions answered
            total_questions = len(ordered_questions)
            answered_questions = len(st.session_state.answers)

            if answered_questions < total_questions:
                st.warning(
                    f"Please answer all questions before submitting "
                    f"({answered_questions}/{total_questions} completed)"
                )
            else:
                st.switch_page("pages/score.py")

        else:
            st.session_state.question_index = q_index + 1
            st.rerun()
