import os
from dotenv import load_dotenv
import sqlite3

# ------------------------------------------------
# LOAD ENV VARIABLES
# ------------------------------------------------
load_dotenv()
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

DB_NAME = "assessment.db"


# =========================================================
# SQLITE CONNECTION
# =========================================================
def get_connection():
    return sqlite3.connect(DB_NAME)


# =========================================================
# ✅ CREATE TABLES
# =========================================================
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # ✅ TABLE 1: RESPONDENTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS respondents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT,
        industry TEXT,
        domain TEXT,
        name TEXT,
        designation TEXT,
        role TEXT,
        email TEXT UNIQUE
    )
    """)

    # ✅ TABLE 2: ASSESSMENT RESULTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assessment_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,

        dim1_score INTEGER,
        dim2_score INTEGER,
        dim3_score INTEGER,
        dim4_score INTEGER,
        dim5_score INTEGER,
        dim6_score INTEGER,
        dim7_score INTEGER,

        total_score INTEGER,
        total_percentage REAL,

        dim1_pct REAL,
        dim2_pct REAL,
        dim3_pct REAL,
        dim4_pct REAL,
        dim5_pct REAL,
        dim6_pct REAL,
        dim7_pct REAL,

        dim1_category TEXT,
        dim2_category TEXT,
        dim3_category TEXT,
        dim4_category TEXT,
        dim5_category TEXT,
        dim6_category TEXT,
        dim7_category TEXT
    )
    """)

    conn.commit()
    conn.close()


# =========================================================
# ✅ INSERT RESPONDENT
# =========================================================
def insert_respondent(client_name, industry, domain, name, designation, role, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO respondents
    (client_name, industry, domain, name, designation, role, email)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (client_name, industry, domain, name, designation, role, email))

    conn.commit()
    conn.close()


# =========================================================
# ✅ CATEGORY LOGIC
# =========================================================
def get_category(pct):
    if pct <= 20:
        return "Lagging"
    elif pct <= 45:
        return "Emerging"
    elif pct <= 65:
        return "Defined"
    elif pct <= 85:
        return "Scaled"
    else:
        return "Leading"


# =========================================================
# ✅ INSERT ASSESSMENT RESULT
# =========================================================
def insert_assessment(name, email, dim_scores, dim_pct, dim_category, total_score, total_pct):
    conn = get_connection()
    cursor = conn.cursor()

    dims = list(dim_scores.keys())

    def safe_get(d, i, default=0):
        try:
            return d.get(dims[i], default)
        except:
            return default

    cursor.execute("""
    INSERT INTO assessment_results (
        name, email,
        dim1_score, dim2_score, dim3_score, dim4_score, dim5_score, dim6_score, dim7_score,
        total_score, total_percentage,
        dim1_pct, dim2_pct, dim3_pct, dim4_pct, dim5_pct, dim6_pct, dim7_pct,
        dim1_category, dim2_category, dim3_category, dim4_category, dim5_category, dim6_category, dim7_category
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name, email,

        safe_get(dim_scores, 0),
        safe_get(dim_scores, 1),
        safe_get(dim_scores, 2),
        safe_get(dim_scores, 3),
        safe_get(dim_scores, 4),
        safe_get(dim_scores, 5),
        safe_get(dim_scores, 6),

        total_score,
        total_pct,

        safe_get(dim_pct, 0),
        safe_get(dim_pct, 1),
        safe_get(dim_pct, 2),
        safe_get(dim_pct, 3),
        safe_get(dim_pct, 4),
        safe_get(dim_pct, 5),
        safe_get(dim_pct, 6),

        safe_get(dim_category, 0, ""),
        safe_get(dim_category, 1, ""),
        safe_get(dim_category, 2, ""),
        safe_get(dim_category, 3, ""),
        safe_get(dim_category, 4, ""),
        safe_get(dim_category, 5, ""),
        safe_get(dim_category, 6, "")
    ))

    conn.commit()
    conn.close()