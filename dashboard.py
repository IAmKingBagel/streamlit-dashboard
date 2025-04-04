import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
cpi_data = pd.read_csv("cpi_data.csv")
interest_rate_data = pd.read_csv("interest_rate_data.csv")
spending_data = pd.read_csv("spending_data.csv")

# Convert 'date' to datetime
cpi_data["date"] = pd.to_datetime(cpi_data["date"])
interest_rate_data["date"] = pd.to_datetime(interest_rate_data["date"])
spending_data["date"] = pd.to_datetime(spending_data["date"])

# Streamlit App
st.title("Inflation & Interest Rate Tracker")

# CPI Chart
st.header("Inflation (CPI)")
fig_cpi = px.line(cpi_data, x="date", y="value", title="Inflation Over Time")
st.plotly_chart(fig_cpi)

# Interest Rate Chart
st.header("Interest Rates")
fig_ir = px.line(interest_rate_data, x="date", y="value", title="Federal Funds Rate Over Time")
st.plotly_chart(fig_ir)

# Consumer Spending Chart
st.header("Consumer Spending")
fig_spending = px.line(spending_data, x="date", y="value", title="Consumer Spending Over Time")
st.plotly_chart(fig_spending)
