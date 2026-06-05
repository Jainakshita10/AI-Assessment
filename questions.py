# questions.py

import pandas as pd

EXCEL_FILE = "Copy of AI App data sample.xlsx"

def load_questions():
    df = pd.read_excel(EXCEL_FILE, engine="openpyxl")

    df.columns = df.columns.str.strip()

    structured = {}

    for _, row in df.iterrows():
        dim = str(row["Dimension"]).strip()
        sub_dim = str(row["Sub Dimension"]).strip()
        question_text = str(row["Questions"]).strip()

        # ✅ build options safely
        raw_options = {
            5: row.get("5"),
            4: row.get("4"),
            3: row.get("3"),
            2: row.get("2"),
            1: row.get("1"),
            0: row.get("0"),
        }

        options = {
            k: v for k, v in raw_options.items()
            if pd.notna(v) and str(v).strip() != ""
        }

        # ✅ build structure correctly
        if dim not in structured:
            structured[dim] = []

        structured[dim].append({
            "question": question_text,
            "sub_dimension": sub_dim,
            "options": options
        })

    # ✅ DEBUG (keep temporarily)
    for dim, qs in structured.items():
        print(dim, len(qs))

    return structured

def get_dimension_list():
    return [
        "Strategy and Operating Model",
        "Value Realisation",
        "Data Foundation",
        "People and Culture",
        "Trusted and Responsible AI",
        "Advanced Capabilities",
        "AI Engineering"
    ]