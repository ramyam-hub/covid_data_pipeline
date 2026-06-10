# ================================================
# extract.py - COVID Data Extraction
# Author: Ramya | Data Engineer
# ================================================

import requests
import pandas as pd
import json
from datetime import datetime

def extract_covid_data():
    """Extract real COVID data from public API"""
    print("📥 Extracting COVID-19 data from API...")
    
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        print(f"✅ Extracted {len(df)} countries data")
        
        # Select important columns
        df = df[['country', 'cases', 'deaths', 
                 'recovered', 'active', 'population']]
        
        # Save raw data
        df.to_csv('data/raw_covid_data.csv', index=False)
        print("💾 Raw data saved to data/raw_covid_data.csv")
        return df
    else:
        print(f"❌ API Error: {response.status_code}")
        return None

if __name__ == "__main__":
    df = extract_covid_data()
    print("\n📊 Sample Data:")
    print(df.head())