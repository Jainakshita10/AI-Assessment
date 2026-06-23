import os
from dotenv import load_dotenv
import sqlite3
import json

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
# Views
# =========================================================

def create_views():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP VIEW IF EXISTS User_Responses")
    cursor.execute("""

CREATE VIEW User_Responses AS

WITH dim1 AS (
    SELECT
        id,
        question,
        MAX(score) AS score,
        MAX(text) AS text,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY question) AS rn
    FROM (
        SELECT
            a.id,
            elem->>'question' AS question,
            elem->>'response' AS score,
            NULL::text AS text
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Strategy_and_Operating_Model_Response_Score) = 'array'
                THEN a.Strategy_and_Operating_Model_Response_Score
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE

        UNION ALL

        SELECT
            a.id,
            elem->>'question',
            NULL,
            elem->>'response'
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Strategy_and_Operating_Model_Response_Text) = 'array'
                THEN a.Strategy_and_Operating_Model_Response_Text
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE
    ) x
    GROUP BY id, question
),

dim2 AS (
    SELECT
        id,
        question,
        MAX(score) AS score,
        MAX(text) AS text,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY question) AS rn
    FROM (
        SELECT a.id, elem->>'question', elem->>'response', NULL::text
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Value_Realisation_Response_Score) = 'array'
                THEN a.Value_Realisation_Response_Score
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE

        UNION ALL

        SELECT a.id, elem->>'question', NULL, elem->>'response'
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Value_Realisation_Response_Text) = 'array'
                THEN a.Value_Realisation_Response_Text
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE
    ) x(id, question, score, text)
    GROUP BY id, question
),

dim3 AS (
    SELECT
        id,
        question,
        MAX(score) AS score,
        MAX(text) AS text,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY question) AS rn
    FROM (
        SELECT a.id, elem->>'question', elem->>'response', NULL::text
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Data_Foundation_Response_Score) = 'array'
                THEN a.Data_Foundation_Response_Score
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE

        UNION ALL

        SELECT a.id, elem->>'question', NULL, elem->>'response'
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Data_Foundation_Response_Text) = 'array'
                THEN a.Data_Foundation_Response_Text
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE
    ) x(id, question, score, text)
    GROUP BY id, question
),

dim4 AS (
    SELECT
        id,
        question,
        MAX(score) AS score,
        MAX(text) AS text,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY question) AS rn
    FROM (
        SELECT a.id, elem->>'question', elem->>'response', NULL::text
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.People_and_Culture_Response_Score) = 'array'
                THEN a.People_and_Culture_Response_Score
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE

        UNION ALL

        SELECT a.id, elem->>'question', NULL, elem->>'response'
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.People_and_Culture_Response_Text) = 'array'
                THEN a.People_and_Culture_Response_Text
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE
    ) x(id, question, score, text)
    GROUP BY id, question
),

dim5 AS (
    SELECT
        id,
        question,
        MAX(score) AS score,
        MAX(text) AS text,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY question) AS rn
    FROM (
        SELECT a.id, elem->>'question', elem->>'response', NULL::text
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Trusted_and_Responsible_AI_Response_Score) = 'array'
                THEN a.Trusted_and_Responsible_AI_Response_Score
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE

        UNION ALL

        SELECT a.id, elem->>'question', NULL, elem->>'response'
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Trusted_and_Responsible_AI_Response_Text) = 'array'
                THEN a.Trusted_and_Responsible_AI_Response_Text
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE
    ) x(id, question, score, text)
    GROUP BY id, question
),

dim6 AS (
    SELECT
        id,
        question,
        MAX(score) AS score,
        MAX(text) AS text,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY question) AS rn
    FROM (
        SELECT a.id, elem->>'question', elem->>'response', NULL::text
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Advanced_Capabilities_Response_Score) = 'array'
                THEN a.Advanced_Capabilities_Response_Score
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE

        UNION ALL

        SELECT a.id, elem->>'question', NULL, elem->>'response'
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.Advanced_Capabilities_Response_Text) = 'array'
                THEN a.Advanced_Capabilities_Response_Text
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE
    ) x(id, question, score, text)
    GROUP BY id, question
),

dim7 AS (
    SELECT
        id,
        question,
        MAX(score) AS score,
        MAX(text) AS text,
        ROW_NUMBER() OVER (PARTITION BY id ORDER BY question) AS rn
    FROM (
        SELECT a.id, elem->>'question', elem->>'response', NULL::text
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.AI_Engineering_Response_Score) = 'array'
                THEN a.AI_Engineering_Response_Score
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE

        UNION ALL

        SELECT a.id, elem->>'question', NULL, elem->>'response'
        FROM assessment_scores a
        LEFT JOIN LATERAL jsonb_array_elements(
            CASE 
                WHEN jsonb_typeof(a.AI_Engineering_Response_Text) = 'array'
                THEN a.AI_Engineering_Response_Text
                ELSE '[]'::jsonb
            END
        ) elem ON TRUE
    ) x(id, question, score, text)
    GROUP BY id, question
)

SELECT
    COALESCE(d1.id,d2.id,d3.id,d4.id,d5.id,d6.id,d7.id) AS id,

    d1.question AS d1_question, d1.score AS d1_score, d1.text AS d1_text,
    d2.question AS d2_question, d2.score AS d2_score, d2.text AS d2_text,
    d3.question AS d3_question, d3.score AS d3_score, d3.text AS d3_text,
    d4.question AS d4_question, d4.score AS d4_score, d4.text AS d4_text,
    d5.question AS d5_question, d5.score AS d5_score, d5.text AS d5_text,
    d6.question AS d6_question, d6.score AS d6_score, d6.text AS d6_text,
    d7.question AS d7_question, d7.score AS d7_score, d7.text AS d7_text

FROM dim1 d1
FULL JOIN dim2 d2 ON d1.id=d2.id AND d1.rn=d2.rn
FULL JOIN dim3 d3 ON COALESCE(d1.id,d2.id)=d3.id AND COALESCE(d1.rn,d2.rn)=d3.rn
FULL JOIN dim4 d4 ON COALESCE(d1.id,d2.id,d3.id)=d4.id AND COALESCE(d1.rn,d2.rn,d3.rn)=d4.rn
FULL JOIN dim5 d5 ON COALESCE(d1.id,d2.id,d3.id,d4.id)=d5.id AND COALESCE(d1.rn,d2.rn,d3.rn,d4.rn)=d5.rn
FULL JOIN dim6 d6 ON COALESCE(d1.id,d2.id,d3.id,d4.id,d5.id)=d6.id AND COALESCE(d1.rn,d2.rn,d3.rn,d4.rn,d5.rn)=d6.rn
FULL JOIN dim7 d7 ON COALESCE(d1.id,d2.id,d3.id,d4.id,d5.id,d6.id)=d7.id 
                 AND COALESCE(d1.rn,d2.rn,d3.rn,d4.rn,d5.rn,d6.rn)=d7.rn
    """)
    conn.commit()
    conn.close()

create_views()