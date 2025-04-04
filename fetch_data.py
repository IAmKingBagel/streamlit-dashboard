import requests
import pandas as pd

# Your FRED API Key
FRED_API_KEY = "ab2d751fdb05fffac9d03c2ef2055eeb"  # Replace this with your actual FRED API key

# Define FRED series IDs
data_series = {
    "CPI": "CPIAUCSL",  # Consumer Price Index
    "Interest Rate": "FEDFUNDS",  # Federal Funds Rate
    "Consumer Spending": "PCE"  # Personal Consumption Expenditures
}

# Function to fetch data from FRED
def fetch_fred_data(series_id):
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()["observations"]
        df = pd.DataFrame(data)[["date", "value"]].astype({"value": "float"})
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")
        return df
    else:
        print(f"Error fetching {series_id}")
        return None

# Fetch datasets
cpi_data = fetch_fred_data(data_series["CPI"])
interest_rate_data = fetch_fred_data(data_series["Interest Rate"])
spending_data = fetch_fred_data(data_series["Consumer Spending"])

# Save data to CSV
cpi_data.to_csv("cpi_data.csv", index=False)
interest_rate_data.to_csv("interest_rate_data.csv", index=False)
spending_data.to_csv("spending_data.csv", index=False)

print("Data saved successfully!")
