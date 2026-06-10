# ================================================
# load.py - COVID Data Loading
# Author: Ramya | Data Engineer
# ================================================

import pandas as pd
import sqlite3

def load_covid_data():
    print("🚀 Loading COVID data to database...")

    # Read processed data
    df = pd.read_csv('data/processed_covid_data.csv')
    
    # Rename columns to remove % symbol
    df.columns = df.columns.str.replace('%', 'pct')
    print(f"📥 Loaded {len(df)} records")

    # Load into SQLite database
    conn = sqlite3.connect('data/covid_data.db')
    df.to_sql('covid_stats', conn,
              if_exists='replace', index=False)

    # Verify load
    result = pd.read_sql(
        "SELECT COUNT(*) as total FROM covid_stats", conn)
    print(f"✅ {result['total'][0]} records in database!")

    # Top 10 countries
    print("\n📊 Top 10 Most Affected Countries:")
    top10 = pd.read_sql("""
        SELECT rank, country, cases, deaths
        FROM covid_stats
        ORDER BY cases DESC
        LIMIT 10
    """, conn)
    print(top10.to_string(index=False))

    # Lowest death rate
    print("\n📊 Countries with Lowest Death Rate:")
    lowest = pd.read_sql("""
        SELECT country, cases, death_rate_pct
        FROM covid_stats
        WHERE cases > 100000
        ORDER BY death_rate_pct ASC
        LIMIT 5
    """, conn)
    print(lowest.to_string(index=False))

    conn.close()
    print("\n✅ ETL Pipeline Complete!")
    print("Extract ✅ → Transform ✅ → Load ✅")

if __name__ == "__main__":
    load_covid_data()