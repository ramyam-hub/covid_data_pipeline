# ================================================
# transform.py - COVID Data Transformation
# Author: Ramya | Data Engineer
# ================================================

import pandas as pd

def transform_covid_data():
    print("⚙️ Transforming COVID data...")
    
    # Load raw data
    df = pd.read_csv('data/raw_covid_data.csv')
    print(f"📥 Loaded {len(df)} records")

    # Clean nulls
    df.dropna(inplace=True)

    # Add death rate column
    df['death_rate_%'] = round(
        (df['deaths'] / df['cases']) * 100, 2)

    # Add recovery rate column
    df['recovery_rate_%'] = round(
        (df['recovered'] / df['cases']) * 100, 2)

    # Sort by cases descending
    df = df.sort_values('cases', ascending=False)

    # Add rank column
    df['rank'] = range(1, len(df) + 1)

    # Save processed data
    df.to_csv('data/processed_covid_data.csv', index=False)
    print("✅ Transformation complete!")
    print(f"💾 Saved to data/processed_covid_data.csv")
    
    print("\n🏆 Top 5 Countries by Cases:")
    print(df[['rank','country','cases',
              'deaths','death_rate_%']].head())
    return df

if __name__ == "__main__":
    transform_covid_data()