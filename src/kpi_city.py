import sqlite3

ALLOWED_CITIES = {"Mumbai", "Delhi", "Bangalore", "Chennai"}

def city_kpi(city: str):
    if city not in ALLOWED_CITIES:
        print(f"Error: City '{city}' is not in the allowed cities list.")
        print(f"Allowed cities: {', '.join(sorted(ALLOWED_CITIES))}")
        return
    conn = sqlite3.connect('data/db/analytics.db')
    cursor = conn.cursor()
    
    query = """
    SELECT 
        COUNT(*) as total_customers,
        AVG(monthly_spend) as avg_monthly_spend,
        SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) as churned_customers,
        ROUND(SUM(CASE WHEN churned = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as churn_rate_percent
    FROM customers_raw 
    WHERE city = ?
    """
    
    cursor.execute(query, (city,))
    result = cursor.fetchone()
    
    if result and result[0] > 0:
        total_customers, avg_spend, churned_customers, churn_rate = result
        print(f"KPI for {city}:")
        print(f"  Total Customers: {total_customers}")
        print(f"  Average Monthly Spend: ${avg_spend:.2f}")
        print(f"  Churned Customers: {churned_customers}")
        print(f"  Churn Rate: {churn_rate}%")
    else:
        print(f"No data found for city: {city}")
    
    conn.close()

if __name__ == "__main__":
    print("=== Testing Mumbai ===")
    city_kpi("Mumbai")
    
    print("\n=== Testing SQL Injection Attempt ===")
    city_kpi("Mumbai' OR 1=1 --")
