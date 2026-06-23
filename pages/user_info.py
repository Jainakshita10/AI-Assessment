import base64
import json

import streamlit as st
import streamlit.components.v1 as components
import re
from database import create_tables, get_saved_respondents, insert_respondent
# ------------------------------------------------
# SECURITY CHECK
# ------------------------------------------------
if "logged_in" not in st.session_state:
    st.switch_page("pages/login.py")
# ------------------------------------------------
# IMAGE DATA
# ------------------------------------------------
with open("media/logo.png", "rb") as f:
    logo_image_data = base64.b64encode(f.read()).decode()
# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Respondent Details",
    layout="wide",
    initial_sidebar_state="collapsed",
)
# ------------------------------------------------
# EMAIL VALIDATION
# ------------------------------------------------
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def sync_saved_values(saved_map):
    selected = st.session_state.get("user_info_client_name", "")
    if selected in saved_map:
        selected_data = saved_map[selected]
        for field in ["industry", "domain", "name", "designation", "role", "email"]:
            st.session_state[f"user_info_{field}"] = selected_data[field]

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

/* Form */
.form-box {
    width: 100%;
    max-width: 560px;
    margin: auto;
    padding: 18px 16px;
    color: white;
    background: rgba(255,255,255,0.04);
    border-radius: 18px;
}

/* Subtitle */
.sub-text {
    text-align: left;
    font-size: 13px;
    margin-top: 10px;
    margin-bottom: 20px;
    color: #d9d9d9;
    font-family: 'Open Sans', sans-serif;
    font-style: italic;
}

/* Labels */
label {
    color: white !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* Inputs */
.stTextInput input {
    background-color: white;
    color: black;
    border-radius: 8px;
    padding: 10px;
    max-width: 100%;
    width: 100%;
    box-sizing: border-box;
    margin: 0;
}

/* Button */
.stButton > button {
    width: 220px;
    background: linear-gradient(to right, #4a90ff, #6aa8ff);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
    display: block;
    margin: auto;
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

# ------------------------------------------------
# PAGE UI
# ------------------------------------------------
top_left, top_center, top_right = st.columns([1, 5, 1])

with top_left:
    st.write("")


with top_center:
    st.markdown(
        "<h1 style='text-align:center; margin:0; font-size:25px; font-weight:bold; color:white; font-family:\'Segoe UI\', sans-serif;'>Respondent Details</h1>",
        unsafe_allow_html=True
    )

with top_right:
    st.markdown(
        f"""
        <div style="display:flex; justify-content:flex-end; align-items:center; height:100%;">
            <img src="data:image/png;base64,{logo_image_data}" width="40">
        </div>
        """,
        unsafe_allow_html=True
    )
a1, a2 = st.columns([0.7, 2])
with a2:
    st.markdown(
            "<div class='login-box'>"
            "<div class='sub-text'>Kindly provide the details below to start assessment. Ensure all fields are filled.</div>",
            unsafe_allow_html=True
        )

left, center, right = st.columns([0.8,2,1.2])

with center:
    #create_tables()
    saved_respondents = get_saved_respondents()
    field_names = ["client_name", "industry", "domain", "name", "designation", "role", "email"]
    saved_values_by_field = {
        field: sorted({resp[field] for resp in saved_respondents if resp[field]})
        for field in field_names
    }
    saved_map = {resp["client_name"]: resp for resp in saved_respondents}
    saved_data_json = json.dumps(saved_respondents)

    for field in field_names:
        session_key = f"user_info_{field}"
        if session_key not in st.session_state:
            st.session_state[session_key] = ""

    col1, col2 = st.columns([0.5, 1.5])
    with col1:
        st.markdown(
            "<p style='color:white; font-size:18px; font-weight:600;'>Client Name</p>",
            unsafe_allow_html=True,
        )
    with col2:
        client_name = st.text_input(
            "",
            placeholder="Enter Client Name",
            label_visibility="collapsed",
            key="user_info_client_name",
            on_change=sync_saved_values,
            args=(saved_map,),
        )

    col3, col4 = st.columns([0.5, 1.5])
    with col3:
        st.markdown(
            "<p style='color:white; font-size:18px; font-weight:600;'>Industry</p>",
            unsafe_allow_html=True,
        )
    with col4:
        industry = st.text_input(
            "",
            placeholder="Enter Industry",
            label_visibility="collapsed",
            key="user_info_industry",
        )

    col5, col6 = st.columns([0.5, 1.5])
    with col5:
        st.markdown(
            "<p style='color:white; font-size:18px; font-weight:600;'>Domain</p>",
            unsafe_allow_html=True,
        )
    with col6:
        domain = st.text_input(
            "",
            placeholder="Enter Domain",
            label_visibility="collapsed",
            key="user_info_domain",
        )

    col7, col8 = st.columns([0.5, 1.5])
    with col7:
        st.markdown(
            "<p style='color:white; font-size:18px; font-weight:600;'>Name</p>",
            unsafe_allow_html=True,
        )
    with col8:
        name = st.text_input(
            "",
            placeholder="Enter Name",
            label_visibility="collapsed",
            key="user_info_name",
        )

    col9, col10 = st.columns([0.5, 1.5])
    with col9:
        st.markdown(
            "<p style='color:white; font-size:18px; font-weight:600;'>Designation</p>",
            unsafe_allow_html=True,
        )
    with col10:
        designation = st.text_input(
            "",
            placeholder="Enter Designation",
            label_visibility="collapsed",
            key="user_info_designation",
        )

    col11, col12 = st.columns([0.5, 1.5])
    with col11:
        st.markdown(
            "<p style='color:white; font-size:18px; font-weight:600;'>Role</p>",
            unsafe_allow_html=True,
        )
    with col12:
        role = st.text_input(
            "",
            placeholder="Enter Role",
            label_visibility="collapsed",
            key="user_info_role",
        )

    col13, col14 = st.columns([0.5, 1.5])
    with col13:
        st.markdown(
            "<p style='color:white; font-size:18px; font-weight:600;'>Email</p>",
            unsafe_allow_html=True,
        )
    with col14:
        email = st.text_input(
            "",
            placeholder="Enter Email",
            label_visibility="collapsed",
            key="user_info_email",
        )

    if saved_respondents:
        field_datalist_map = {
            "client_name": [resp["client_name"] for resp in saved_respondents],
            "industry": [resp["industry"] for resp in saved_respondents],
            "domain": [resp["domain"] for resp in saved_respondents],
            "name": [resp["name"] for resp in saved_respondents],
            "designation": [resp["designation"] for resp in saved_respondents],
            "role": [resp["role"] for resp in saved_respondents],
            "email": [resp["email"] for resp in saved_respondents],
        }
        component_html = f"""
<script>
  const savedData = {saved_data_json};
  const fieldNames = ["client_name", "industry", "domain", "name", "designation", "role", "email"];
  const savedValuesByField = {json.dumps(saved_values_by_field)};

  function attachAutofill() {{
    try {{
      const pdoc = window.parent.document;
      const inputs = Array.from(pdoc.querySelectorAll('.stTextInput input'));
      if (inputs.length < fieldNames.length) return;

      inputs.forEach((input, idx) => {{
        const fieldName = fieldNames[idx];
        input.setAttribute('autocomplete', 'off');
        const listId = `saved_${{fieldName}}_datalist`;
        input.setAttribute('list', listId);

        let datalist = pdoc.getElementById(listId);
        if (!datalist) {{
          datalist = pdoc.createElement('datalist');
          datalist.id = listId;
          pdoc.body.appendChild(datalist);
        }}
        datalist.innerHTML = '';
        const values = savedValuesByField[fieldName] || [];
        values.forEach(value => {{
          const option = pdoc.createElement('option');
          option.value = value;
          datalist.appendChild(option);
        }});

        input.removeEventListener('change', input._savedAutofillHandler);
        const handler = () => {{
          const selectedValue = input.value;
          const selection = savedData.find(row => row[fieldName] === selectedValue);
          if (!selection) return;
          fieldNames.forEach((targetField, targetIdx) => {{
            const targetInput = inputs[targetIdx];
            if (targetInput) {{
              targetInput.value = selection[targetField] || '';
              targetInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
            }}
          }});
        }};
        input._savedAutofillHandler = handler;
        input.addEventListener('change', handler);
      }});
    }} catch (error) {{
      console.log('autofill init error:', error);
    }}
  }}

  attachAutofill();
  setTimeout(attachAutofill, 200);
  setTimeout(attachAutofill, 800);
</script>
"""
        components.html(component_html, height=0)

# Track if user has tried submitting
    t1, t2 = st.columns([0.7, 2])
    with t2:
        if "submitted" not in st.session_state:
            st.session_state.submitted = False
        # Show errors at TOP (before the button)
        if st.session_state.submitted:
            if not client_name or not industry or not domain or not name or not designation or not role or not email:
                st.markdown("""
                        <div style="
                        background-color:#f8d7da;
                        color:#842029;
                        padding:2px;
                        border-radius:5px;
                        width: 430px;
                        text-align:center;
                        font-weight:600;
                        margin-bottom: 5px;
                        margin-top: 5px;
                        ">
                        Please fill all the fields
                        </div>
                        """, unsafe_allow_html=True)
                
            elif not is_valid_email(email):
                st.markdown("""
                        <div style="
                        background-color:#f8d7da;
                        color:#842029;
                        padding:2px;
                        border-radius:5px;
                        width: 430px;
                        text-align:center;
                        font-weight:600;
                        margin-bottom: 5px;
                        margin-top: 5px;
                        ">
                        Please enter a valid email
                        </div>
                        """, unsafe_allow_html=True)
    # Then the button
    b1, b2 = st.columns([0.7, 2])
    with b2:
        submit = st.button("Submit", use_container_width=True)

    if submit:
        st.session_state.submitted = True
        if not client_name or not industry or not domain or not name or not designation or not role or not email:
            st.rerun()  # triggers re-render, errors show at top
        elif not is_valid_email(email):
            st.rerun()
        else:
            # ✅ NEW: Create table
            insert_respondent(
                client_name,
                industry,
                domain,
                name,
                designation,
                role,
                email
            )
        # ✅ NEW: Save in session (IMPORTANT)
            st.session_state.name = name
            st.session_state.email = email

            st.success("Details submitted successfully!")
            st.switch_page("pages/assessment_home.py")
    st.markdown("</div>", unsafe_allow_html=True)
