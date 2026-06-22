# AI Assessment

AI Assessment is a Streamlit-based maturity assessment app built for evaluating AI readiness across multiple organizational dimensions.

## Overview

The application guides users through an AI maturity questionnaire, captures respondent details, computes dimension-level scores, and stores results in a local SQLite database by default. It includes a login page, respondent details form, interactive questionnaire navigation, and a score summary page.

## Key Features

- Streamlit multi-page UI with custom styling
- Login gate with configurable credentials
- Respondent details capture and saved respondent lookup
- Multi-dimensional AI maturity questionnaire loaded from `AI_App_data_sample.xlsx`
- Score calculation with maturity categories
- Local SQLite persistence and optional PostgreSQL production support
- Dockerfile included for container deployment

## Tech Stack

- Python
- Streamlit
- Pandas
- SQLite / PostgreSQL
- openpyxl
- Plotly / Matplotlib

## Requirements

Dependencies are listed in `requirements.txt`.

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the environment:

```powershell
venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The app supports optional environment configuration through `.env`:

- `ENVIRONMENT` - `development` (default) or `production`
- `DB_NAME` - SQLite database file name (default: `assessment.db`)
- `LOGIN_USERNAME` - login username (default: `AI_Assessment`)
- `LOGIN_PASSWORD` - login password (default: `Ai@assessment!2026`)

For PostgreSQL production, set:

- `PGHOST`
- `PGDATABASE`
- `PGUSER`
- `PGPASSWORD`
- `PGPORT`

## Running the App

Launch the Streamlit app from the repository root:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Data Files

- `AI_App_data_sample.xlsx` contains the questionnaire definitions and scoring options.
- `assessment.db` is the default SQLite database file used for development.

## App Flow

1. `app.py` redirects to the home page.
2. `pages/home.py` shows the landing page.
3. `pages/login.py` handles login authentication.
4. `pages/user_info.py` collects respondent details.
5. `pages/assessment_home.py` describes assessment dimensions.
6. `pages/questionnaire.py` renders the questionnaire and navigation.
7. `pages/score.py` displays computed scores and maturity categories.

## Notes

- The app is designed for internal AI maturity evaluation and can be extended with additional analytics or reporting.
- Use `ENVIRONMENT=production` to switch from SQLite to PostgreSQL.

## License

This repository does not include a license file. Add one if you plan to share or distribute the project.

