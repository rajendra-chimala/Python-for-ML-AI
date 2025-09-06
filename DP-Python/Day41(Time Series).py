import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("fivethirtyeight")
dates = pd.date_range("2025-01-01", periods = 10, freq = "D")

no_of_product_sold = [100, 80, 40, 50, 60, 30, 90, 110, 40, 10] 

plt.figure(figsize = (8,4))
plt.plot_date(dates, no_of_product_sold, "r-", linestyle = "solid")
plt.plot_date(dates, no_of_product_sold, "bo")

plt.title("Time Series")
plt.xlabel("Date")
plt.ylabel("No. of product sold")
plt.show()
