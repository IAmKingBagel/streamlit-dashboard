import pandas as pd
import matplotlib.pyplot as plt

# Load Data
cpi_data = pd.read_csv("cpi_data.csv")
interest_rate_data = pd.read_csv("interest_rate_data.csv")
spending_data = pd.read_csv("spending_data.csv")

# Convert 'date' column to datetime
cpi_data["date"] = pd.to_datetime(cpi_data["date"])
interest_rate_data["date"] = pd.to_datetime(interest_rate_data["date"])
spending_data["date"] = pd.to_datetime(spending_data["date"])

# Plot CPI (Inflation) as a line (no dots)
plt.figure(figsize=(10,5))
plt.plot(cpi_data["date"], cpi_data["value"], linestyle="-", label="CPI", linewidth=1)  # Removed marker="o"
plt.xlabel("Date")
plt.ylabel("CPI (Consumer Price Index)")
plt.title("Inflation Over Time")
plt.legend()
plt.grid()
plt.show()

# Plot Interest Rates as a line (no dots)
plt.figure(figsize=(10,5))
plt.plot(interest_rate_data["date"], interest_rate_data["value"], linestyle="-", color="red", label="Fed Funds Rate", linewidth=1)  # Removed marker="o"
plt.xlabel("Date")
plt.ylabel("Interest Rate (%)")
plt.title("Federal Funds Rate Over Time")
plt.legend()
plt.grid()
plt.show()

# Plot Consumer Spending as a line (no dots)
plt.figure(figsize=(10,5))
plt.plot(spending_data["date"], spending_data["value"], linestyle="-", color="green", label="Consumer Spending", linewidth=1)  # Removed marker="o"
plt.xlabel("Date")
plt.ylabel("Spending ($ Billion)")
plt.title("Consumer Spending Over Time")
plt.legend()
plt.grid()
plt.show()
