# Scatter Plots
# When the both variables are discrete than we use scatter plots.
# model fastapi vs django rest framework vs flask

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(r"sample_data\2019-05-31-data.csv")


views_count = df['view_count']
likes = df['likes']
ratio = df['ratio']
plt.style.use('fivethirtyeight')


plt.xscale("log")
plt.yscale("log")
plt.scatter(views_count,likes,c=ratio,cmap="rainbow",edgecolor='black',linewidth=0.7,alpha=0.7)


cbar = plt.colorbar()
cbar.set_label("Like / Dislike Ratio")
plt.title("Tranding YouTube Videos")
plt.xlabel("Views Count")
plt.ylabel("Total Likes")
plt.tight_layout()
plt.grid()


plt.show()
print(plt.colormaps())
# print(plt.style.available)