# score.py
import base64

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from questions import load_questions, get_dimension_list
# ✅ NEW: DB import
from database import insert_assessment, get_category
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# ------------------------------------------------
# IMAGE DATA
# ------------------------------------------------
with open("media/logo.png", "rb") as f:
    logo_image_data = base64.b64encode(f.read()).decode()

st.set_page_config(
    page_title="Score Details",
    layout="wide",
    initial_sidebar_state="collapsed",
)
#---------------CSS--------------------
st.markdown("""
<style>
/* Full App Background */
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
    padding-left: 1rem;
    padding-right: 0rem;

    background: #000031;

    border-radius: 0;

    box-shadow: none;
    min-height: 100vh;
}
/* Title */
.top-title { 
    text-transform: uppercase;
    color: #12ABDB;
    font-weight: bold;
    font-size: 20px;
    text-align: left;
    margin-top: 2px;
    margin-bottom: 2px;
    margin-left: 10px;
}
.sub-title {
    text-transform: uppercase;
    text-align: left;
    font-size: 24px;
    color: #FFFFFF;
   font-weight: 700;
   text-shadow: 0 0 6px rgba(255,255,255,0.4);
    margin-top: 2px;
    margin-bottom: 2px;
    margin-left: 10px;
}
/* Ai maturity assessment result */
.summary-box {
   background: #12ABDB;
   color: #FFFFFF;
   border-radius: 0px 25px 25px 0px;
   padding: 10px 20px;
   font-weight: 600;
   text-align: center;
   border: none;
   width: 300px;
   font-size: 15px;
   box-shadow: 0 4px 10px rgba(0,0,0,0.25);
   margin-left: -20px; /* adjust this value */
}
.summary-box-right {
   background: #12ABDB;
   color: #FFFFFF;
   border-radius: 25px 0px 0px 25px;
   padding: 10px 20px;
   font-weight: 600; 
   text-align: center;
   border: none;
   width: 350px;
   font-size: 15px;
   box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    margin-right: -20px;
    float: right;
}
.maturity-table {
   width: 180px;
   border-collapse: collapse;
   font-family: Arial, sans-serif;
    font-size: 6px;
    float: right;
}
.maturity-table td {
   border: 1px solid white;
   padding: 2px 4px;
   font-weight: bold;
   color: white;
   text-align: center;
   font-size: 8px;
    height: 15px;
}
/* Left percentage column */
.range {
    font-size: 8px;
   background-color: #0B1026;
   width: 20%;
}
/* Right maturity level colors */
.lagging {
    font-size: 8px;
   background-color: #8B5A7A;
    width: 20%;
}
.emerging {
    font-size: 8px;
   background-color: #A89A00;
    width: 20%;
}
.defined {
    font-size: 8px;
   background-color: #5E8E99;
    width: 20%;
}
.scaled {
    font-size: 8px;
   background-color: #3F79A8;
    width: 20%;
}
.leading {
    font-size: 8px;
   background-color: #5C7F2B;
    width: 20%; 
}
.recommendation {
            font-size: 16px;
            font-weight: 400;
            fonrt-family: 'Segoe UI', sans-serif;
            color: white;
            margin-top: -20px;
            }
.disclaimer {
            font-size: 14px;
            font-weight: 200;
            fonrt-family: 'Segoe UI', sans-serif;
            color: white;
            margin-top: -5px;
            padding-top: 0px;
            }

div[data-testid="column"] {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}
</style>
""", unsafe_allow_html=True)
# --------------------- DATA ---------------------
questions_data = load_questions()
dimensions = get_dimension_list()
answers = st.session_state.answers

# ✅ REMOVE old maturity fn (use DB one instead)
# def get_maturity(score_pct): ...

results = []
total_score = 0
total_max = 0

# ✅ NEW: structures for DB
dim_scores = {}
dim_pct = {}
dim_category = {}

for dim in dimensions:
    qs = questions_data[dim]
    max_score = len(qs) * 5

    # ⚠️ FIX: using correct key format from questionnaire
    obtained = sum(
        score for (d, _), score in answers.items() if d == dim
    )

    pct = (obtained / max_score) * 100 if max_score else 0
    category = get_category(pct)

    # ✅ store for DB
    dim_scores[dim] = obtained
    dim_pct[dim] = pct
    dim_category[dim] = category

    results.append({
        "Pillar": dim,
        "Response Score": obtained,
        "Max Score": max_score,
        "Score %": round(pct, 2),
        "Maturity": category
    })

    total_score += obtained
    total_max += max_score

total_pct = (total_score / total_max) * 100 if total_max else 0
# ------------------------------------------------
# PAGE UI
# ------------------------------------------------
top_left, top_right = st.columns([2.2,1.8])

with top_left:
    st.markdown(
        """
        <div class='top-title'>
            AI Maturity Assessment
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class='sub-title'>
            WEIGHTED ANALYSIS
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
        <div class="summary-box">
            AI Maturity Assessment Summary
        </div>
    """, unsafe_allow_html=True)
with top_right:
    st.markdown("""
        <table class="maturity-table">
        <tr>
        <td class="range">1–20%</td>
        <td class="lagging">Lagging</td>
        </tr>
        <tr>
        <td class="range">21–45%</td>
        <td class="emerging">Emerging</td>
        </tr>
        <tr>
        <td class="range">46–65%</td>
        <td class="defined">Defined</td>
        </tr>
        <tr>
        <td class="range">66–85%</td>
        <td class="scaled">Scaled</td>
        </tr>
        <tr>
        <td class="range">86–100%</td>
        <td class="leading">Leading</td>
        </tr>
        </table>
    """, unsafe_allow_html=True)
# --------------------- Table Style ---------------------
table_style = """
<style>
.custom-table {
    width: auto;
    border-collapse: collapse;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 12px;
    margin-bottom: -10px;
    border: 2px solid rgba(255,255,255,0.6); /* 🔥 bold outer border */
}

/* Header */
.custom-table th {
    background: #1fa3c6;
    color: #ffffff;
    padding: 5px 6px;
    text-align: center;
    font-weight: 600;   
    width: 110px;   /* 🔹 reduced width */
    height: 20px;
    border: 2px solid rgba(255,255,255,0.5); /* 🔥 thicker lines */
}

/* Cells */
.custom-table td {
    background: #1c1f3a;
    color: #ffffff;
    padding: 5px 6px;
    border: 2px solid rgba(255,255,255,0.4); /* 🔥 bold grid */
    text-align: center;
    font-weight: 600;
    width: 110px;   /* 🔹 reduced width */
    height: 20px;

}
.custom-table td, 
.custom-table th {
    line-height: 1.1;
    white-space: normal;     /* ✅ allows wrapping */
    word-break: break-word;  /* ✅ force wrap if long */
    vertical-align: middle;
}
/* First column (left aligned like image) */
.custom-table td:first-child {
    width: 95px;
    text-align: left;
    padding-left: 5px;
}

/* Maturity colors (closer to reference) */
.initial { background: #5b3a70 !important; }
.emerging { background: #8a6f00 !important; }
.defined  { background: #3f6f7a !important; }
.scaled   { background: #3a6ea5 !important; }
.leading  { background: #5a7f2c !important; }

/* Total row (blue highlight) */
.total-row td {
    background: #1fa3c6;
    font-weight: bold;
    border: 2px solid rgba(255,255,255,0.7); /* 🔥 strongest emphasis */
}

/* Special total maturity cell */
.total-row td:last-child {
    background: #8a6f00 !important;
}

/* Subtle hover */
.custom-table tr:hover td {
    background: #2a2f55;
    transition: 0.2s;
}
</style>
"""
col1 , col2 = st.columns([2.2, 1.8])
with col1:
    table_html = table_style + """
        <table class="custom-table">
        <tr>
        <th>Pillar</th>
        <th>Response Score</th>
        <th>Max Score</th>
        <th>Score %</th>
        <th>Maturity</th>
        </tr>
    """

    # ✅ Function stays here (OK)
    def get_maturity_class(pct):
        if pct <= 20:
            return "initial"
        elif pct <= 45:
            return "emerging"
        elif pct <= 65:
            return "defined"
        elif pct <= 85:
            return "scaled"
        else:
            return "leading"

    # ✅ Loop (FIXED)
    for r in results:
        # 🔥 IMPORTANT: convert % to number
        score_pct = float(str(r["Score %"]).replace("%", ""))

        maturity_class = get_maturity_class(score_pct)

        table_html += f"""
            <tr>
            <td>{r["Pillar"]}</td>
            <td>{r["Response Score"]}</td>
            <td>{r["Max Score"]}</td>
            <td>{score_pct}%</td>
            <td class="{maturity_class}">{r["Maturity"]}</td>
            </tr>
        """

    # ✅ Total row (FIXED)
    total_class = get_maturity_class(total_pct)

    table_html += f"""
        <tr class="total-row">
        <td><b>Total</b></td>
        <td>{total_score}</td>
        <td>{total_max}</td>
        <td>{round(total_pct, 2)}%</td>
        <td class="{total_class}"><b>{get_category(total_pct)}</b></td>
        </tr>
        </table>
    """
    #st.markdown("<div style='margin-top:10px'></div>", unsafe_allow_html=True)
    # ✅ Increase height so last row shows
    #components.html(table_html, height=500)  
    row_count = len(results) + 2  # header + total
    height = row_count * 35      # approx row height
    components.html(table_html, height=height, scrolling=False)
# --------------------- CHART ---------------------
with col2:
        #st.markdown("<div style='margin-top:10px'></div>", unsafe_allow_html=True)
        st.markdown("""
            <div class="summary-box-right">
                AI Maturity Dimensional Analysis
            </div>
        """, unsafe_allow_html=True)
        #st.markdown('<div style="padding-left: 40px;">', unsafe_allow_html=True)
        chart_df = pd.DataFrame({
            "Dimension": [r["Pillar"] for r in results],
            "Score": [r["Score %"] if r["Score %"] is not None else 0 for r in results]
        })
        st.markdown("<div style='display:flex;justify-content:right;margin-bottom: -10px;'>", unsafe_allow_html=True)
        #labels = chart_df["Dimension"].tolist()
        labels = [l.replace(" and ", "<br>") for l in chart_df["Dimension"].tolist()]
        scores = chart_df["Score"].tolist()

        # Close loop for polygon
        labels += [labels[0]]
        scores += [scores[0]]

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=scores,
            theta=labels,
            fill='toself',
            line=dict(color='#4AA3FF', width=2),
            fillcolor='rgba(74, 163, 255, 0.35)',  # bluish area
            marker=dict(size=6, color='#4AA3FF')
        ))

        fig.update_layout(
            polar=dict(
            radialaxis=dict(
            visible=True,                 # ✅ enable axis (needed for gridlines)
            range=[0, 100],
            showticklabels=False,         # ✅ hide numbers but keep lines
            ticks='',  
            nticks=10,                  # ✅ remove tick marks
            gridcolor='rgba(255,255,255,0.5)',
            gridwidth=1,
            linecolor='white',
            linewidth=1
        ),
            angularaxis=dict(
            tickfont=dict(size=9, color='white'),   # ✅ slightly bigger labels
            gridcolor='rgba(255,255,255,0.5)',
            gridwidth=1,
            linecolor='white',
            linewidth=1
        ),
            gridshape='linear',
            bgcolor='rgba(0,0,0,0)'
        ),

        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',

        # ✅ critical for label visibility
        margin=dict(l=60, r=60, t=40, b=40),

        font=dict(color='white'),
        showlegend=False,
        height=300,   # ✅ smaller height
        width=700     # ✅ controlled width
        )
# ✅ let column control size (important for alignment)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
# --------------------- SAVE TO DB ---------------------
# st.subheader("Save your results")

# if st.button("Save Results"):

#     name = st.session_state.get("name")
#     email = st.session_state.get("email")

#     if not name or not email:
#         st.error("User information missing. Please restart assessment.")
#     else:
#         insert_assessment(
#             name,
#             email,
#             dim_scores,
#             dim_pct,
#             dim_category,
#             total_score,
#             total_pct
#         )

#         st.success("✅ Results saved successfully!")
name = st.session_state.get("name")
email = st.session_state.get("email")
insert_assessment(
            name,
            email,
            dim_scores,
            dim_pct,
            dim_category,
            total_score,
            total_pct
        )
# --------------------- FOOTER ---------------------
st.markdown(
    """
    <div class="recommendation">
        <b>Recommendation:</b> Based on the AI maturity assessment across seven dimensions,we recommend a prioritized roadmap to progress toward scaled and leading AI capabilities
    </div>
    """,
    unsafe_allow_html=True,
)
# --------------------- RESET ---------------------
x,y = st.columns([8,1])
with x:
    st.markdown(
        """
        <div class='disclaimer'>
            Disclaimer: This assessment is based on a high-level survey of 30 questions and is intended to provide an indicative view of AI maturity. For a comprehensive and detailed assessment, please reach out to our Data & AI Strategy team
        </div>
        """,
        unsafe_allow_html=True
    )
with y:

    with open("media/re-assess-button.png", "rb") as f:
        re_assess_button = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <a href="home" target="_self">
            <img src="data:image/png;base64,{re_assess_button}" 
                 style="width:128px;height:64px;cursor:pointer;" />
        </a>
        """,
        unsafe_allow_html=True
    )
    # if st.button("RE-ASSESS"):
    #     st.session_state.clear()
    #     st.switch_page("pages/assessment_home.py")