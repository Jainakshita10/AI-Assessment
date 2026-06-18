import os
from dotenv import load_dotenv
import sqlite3

# ✅ ADD THIS
import psycopg

# ------------------------------------------------
# LOAD ENV VARIABLES
# ------------------------------------------------
load_dotenv()
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

DB_NAME = os.getenv("DB_NAME", "assessment.db")


# =========================================================
# ✅ CONNECTION HANDLER (SQLITE + POSTGRES)
# =========================================================
def get_connection():
    if ENVIRONMENT == "production":
        return psycopg.connect(
            host=os.getenv("PGHOST"),
            dbname=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            port=os.getenv("PGPORT", 5432),
            sslmode="require"
        )

    # ✅ Default: SQLite (dev)
    db_path = DB_NAME
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)

    return sqlite3.connect(db_path)


# =========================================================
# ✅ HELPER (QUERY PLACEHOLDERS)
# =========================================================
def is_postgres():
    return ENVIRONMENT == "production"
def get_placeholder():
    return "%s" if is_postgres() else "?"
# =========================================================
# ✅ CREATE TABLES
# =========================================================
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    if is_postgres():
        # ✅ POSTGRES SYNTAX
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS respondents_details (
            id SERIAL PRIMARY KEY,
            client_name TEXT,
            industry TEXT,
            domain TEXT,
            name TEXT,
            designation TEXT,
            role TEXT,
            email TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessment_scores (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT,

            Strategy_and_Operating_Model_score INTEGER,
            Value_Realisation_score INTEGER,
            Data_Foundation_score INTEGER,
            People_and_Culture_score INTEGER,
            Trusted_and_Responsible_AI_score INTEGER,
            Advanced_Capabilities_score INTEGER,
            AI_Engineering_score INTEGER,

            total_score INTEGER,
            total_percentage REAL,

            Strategy_and_Operating_Model_pct REAL,
            Value_Realisation_pct REAL,
            Data_Foundation_pct REAL,
            People_and_Culture_pct REAL,
            Trusted_and_Responsible_AI_pct REAL,
            Advanced_Capabilities_pct REAL,
            AI_Engineering_pct REAL,

            Strategy_and_Operating_Model_category TEXT,
            Value_Realisation_category TEXT,
            Data_Foundation_category TEXT,
            People_and_Culture_category TEXT,
            Trusted_and_Responsible_AI_category TEXT,
            Advanced_Capabilities_category TEXT,
            AI_Engineering_category TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
    else:
        # ✅ SQLITE (your original code)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS respondents_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT,
            industry TEXT,
            domain TEXT,
            name TEXT,
            designation TEXT,
            role TEXT,
            email TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessment_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            Strategy_and_Operating_Model_score INTEGER,
            Value_Realisation_score INTEGER,
            Data_Foundation_score INTEGER,
            People_and_Culture_score INTEGER,
            Trusted_and_Responsible_AI_score INTEGER,
            Advanced_Capabilities_score INTEGER,
            AI_Engineering_score INTEGER,
            total_score INTEGER,
            total_percentage REAL,
            Strategy_and_Operating_Model_pct REAL,
            Value_Realisation_pct REAL,
            Data_Foundation_pct REAL,
            People_and_Culture_pct REAL,
            Trusted_and_Responsible_AI_pct REAL,
            Advanced_Capabilities_pct REAL,
            AI_Engineering_pct REAL,
            Strategy_and_Operating_Model_category TEXT,
            Value_Realisation_category TEXT,
            Data_Foundation_category TEXT,
            People_and_Culture_category TEXT,
            Trusted_and_Responsible_AI_category TEXT,
            Advanced_Capabilities_category TEXT,
            AI_Engineering_category TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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

    if is_postgres():
        cursor.execute("""
        INSERT INTO respondents_details
        (client_name, industry, domain, name, designation, role, email)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (email)
        DO UPDATE SET
            client_name = EXCLUDED.client_name,
            industry = EXCLUDED.industry,
            domain = EXCLUDED.domain,
            name = EXCLUDED.name,
            designation = EXCLUDED.designation,
            role = EXCLUDED.role;
        """, (client_name, industry, domain, name, designation, role, email))

    else:
        cursor.execute("""
        INSERT OR REPLACE INTO respondents_details
        (client_name, industry, domain, name, designation, role, email)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (client_name, industry, domain, name, designation, role, email))

    conn.commit()
    conn.close()


# =========================================================
# ✅ FETCH RESPONDENTS
# =========================================================
def get_saved_respondents():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT client_name, industry, domain, name, designation, role, email
        FROM respondents_details
        ORDER BY client_name, name
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "client_name": row[0],
            "industry": row[1],
            "domain": row[2],
            "name": row[3],
            "designation": row[4],
            "role": row[5],
            "email": row[6],
        }
        for row in rows
    ]
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
# ✅ INSERT ASSESSMENT
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

    placeholder = "%s" if is_postgres() else "?"

    query = f"""
    INSERT INTO assessment_scores (
        name, email,
        Strategy_and_Operating_Model_score, Value_Realisation_score, Data_Foundation_score, People_and_Culture_score, Trusted_and_Responsible_AI_score, Advanced_Capabilities_score, AI_Engineering_score,
        total_score, total_percentage,
        Strategy_and_Operating_Model_pct, Value_Realisation_pct, Data_Foundation_pct, People_and_Culture_pct, Trusted_and_Responsible_AI_pct, Advanced_Capabilities_pct, AI_Engineering_pct,
        Strategy_and_Operating_Model_category, Value_Realisation_category, Data_Foundation_category, People_and_Culture_category, Trusted_and_Responsible_AI_category, Advanced_Capabilities_category, AI_Engineering_category
    )
    VALUES ({",".join([placeholder]*25)})
    """

    cursor.execute(query, (
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