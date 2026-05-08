# Applied Analytics Mini Project

A beginner-friendly project demonstrating data loading, KPI calculations, and SQL injection protection.

## Project Structure
```
vibe-kpi-demo/
├── data/
│   ├── raw/
│   │   └── customers_raw.csv     # Sample customer data
│   └── db/
│       └── analytics.db          # SQLite database (auto-generated)
├── src/
│   ├── etl_load_sqlite.py        # ETL script to load CSV into SQLite
│   └── kpi_city.py              # KPI calculation with SQL injection protection
├── tests/
│   └── test_kpi_city.py         # Pytest tests for KPI functions
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # This file
```

## Setup and Run Commands

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run ETL Script (Load CSV into SQLite)
```bash
cd src
python etl_load_sqlite.py
```

### 3. Run KPI Script
```bash
cd src
python kpi_city.py
```

### 4. Run Tests
```bash
pytest
```

## File Explanations
- `data/raw/customers_raw.csv`: Sample customer data with 12 rows across 4 cities
- `src/etl_load_sqlite.py`: Loads CSV data into SQLite database
- `src/kpi_city.py`: Calculates city-specific KPIs with SQL injection protection
- `tests/test_kpi_city.py`: Tests for KPI functionality and SQL injection safety
- `requirements.txt`: Python dependencies (pandas, pytest)
- `.gitignore`: Ignores virtual environment, cache, and database files

## Features Demonstrated
- Data loading from CSV to SQLite
- Parameterized SQL queries (SQL injection protection)
- KPI calculations (average spend, churn rate)
- Unit testing with pytest
- Clean project structure