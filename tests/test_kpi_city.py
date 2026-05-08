import pytest
import sqlite3
import pandas as pd
import os
import sys
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from kpi_city import city_kpi

@pytest.fixture
def setup_test_db():
    test_db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'db', 'test_analytics.db')
    os.makedirs(os.path.dirname(test_db_path), exist_ok=True)
    
    test_data = [
        (1, 'Mumbai', 2500.50, 0),
        (2, 'Mumbai', 3200.00, 1),
        (3, 'Delhi', 1800.75, 0),
        (4, 'Mumbai', 2800.75, 0)
    ]
    
    conn = sqlite3.connect(test_db_path)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS customers_raw')
    cursor.execute('''
        CREATE TABLE customers_raw (
            customer_id INTEGER,
            city TEXT,
            monthly_spend REAL,
            churned INTEGER
        )
    ''')
    cursor.executemany('INSERT INTO customers_raw VALUES (?, ?, ?, ?)', test_data)
    conn.commit()
    conn.close()
    
    original_db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'db', 'analytics.db')
    if os.path.exists(original_db_path):
        os.rename(original_db_path, original_db_path + '.backup')
    
    os.rename(test_db_path, original_db_path)
    
    yield
    
    if os.path.exists(original_db_path):
        os.remove(original_db_path)
    backup_path = original_db_path + '.backup'
    if os.path.exists(backup_path):
        os.rename(backup_path, original_db_path)

def test_city_kpi_happy_path(setup_test_db):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        city_kpi("Mumbai")
        output = mock_stdout.getvalue()
    
    assert "KPI for Mumbai" in output
    assert "Total Customers: 3" in output
    assert "Average Monthly Spend: $2833.75" in output
    assert "Churned Customers: 1" in output
    assert "Churn Rate: 33.33%" in output

def test_city_kpi_sql_injection_attempt(setup_test_db):
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        city_kpi("Mumbai' OR 1=1 --")
        output = mock_stdout.getvalue()
    
    assert "No data found for city: Mumbai' OR 1=1 --" in output
    assert "Total Customers: 4" not in output
