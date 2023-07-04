import requests
import matplotlib.pyplot as plt
from matplotlib import style
import datetime

#API key for accessing Finnhub API
ApiKey = 'cifs1vhr01qhvakk7pvgcifs1vhr01qhvakk7q00'

#Prompt user to enter the stock symbol
Stock = input("Enter The Symbol: ")

#API endpoint URL for getting quote data
quote_url = f"https://finnhub.io/api/v1/quote?symbol={Stock}&token={ApiKey}"

#API endpoint URL for getting data
resolution = 'D'
historical_url = f"https://finnhub.io/api/v1/stock/candle?symbol={Stock}&resolution={resolution}&count=30&token={ApiKey}"

#To set the headers for the API requests
header = {"X-Finnhub-Secret": "cifs2h1r01qhvakk81j0"}

#To request data from the API
quote_response = requests.get(quote_url, headers=header)
quote_data = quote_response.json()

# To extract required data
Previous_day_Closing_Price = quote_data["pc"]
Opening_Price = quote_data["o"]
Price_Change = quote_data["d"]
Current_Price = quote_data["c"]
High_Price = quote_data["h"]
Low_Price = quote_data["l"]
Price_Change_in_Percentage = quote_data["dp"]

#To print the data
print("Stock Name =", Stock)
print("Current price =", Current_Price)
print("Previous day closing price =", Previous_day_Closing_Price)
print("Opening price =", Opening_Price)
print("Price change =", Price_Change)
print("Price change in percentage =", Price_Change_in_Percentage)
print("Highest Price =", High_Price)
print("Lowest price =", Low_Price)

#To request data from the API
historical_response = requests.get(historical_url, headers=header)
historical_data = historical_response.json()

#To extract price and timestamp from data
Previous_day_Closing_Price = historical_data["c"]
Timestamp = historical_data["t"]

#To convert Unix timestamp to datetime object
Timestamp = [datetime.datetime.fromtimestamp(timestamp) for timestamp in Timestamp]

#To create a plot
style.use("ggplot")
plt.plot(Timestamp, Previous_day_Closing_Price)
plt.title('Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.xticks(rotation=45)

# To display the plot
plt.show()
