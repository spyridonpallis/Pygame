import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = input("Enter stock ticker: ")

# Get the last month of data
start = pd.to_datetime('today').date() - pd.Timedelta(days=30)
end = pd.to_datetime('today').date()
df = yf.download(ticker, start=start, end=end)

# Create a line chart
fig, ax = plt.subplots()

# Plot the data
df['Close'].plot(ax=ax, color='blue')

# Set the chart labels and title
plt.title(f"{ticker} Price - Last 30 Days")
plt.xlabel("Date")
plt.ylabel("Price")

# Show the chart
plt.show()
