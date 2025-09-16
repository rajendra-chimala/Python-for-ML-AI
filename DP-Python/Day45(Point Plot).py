import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.0)

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")

# -----------------------------
# Point Plot
# -----------------------------

# sns.pointplot(data=tips, x="day", y="total_bill")
# plt.title("Point Plot of total_bill by day")
# plt.show()



#------------------
#Correlation Heatmap
#------------------
# cor = tips.corr(numeric_only = True) # Tip, Total_bill and Size

# sns.heatmap(cor, annot = True,  fmt = ".2f")
# plt.title("Correlation Heatmap of Tips Dataset")
# plt.show()



# ------------------------------
#Pivot Table and Heatmap
# ------------------------------

pt = pd.pivot_table(flights, values="passengers", index="month", columns="year")
sns.heatmap(pt, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("Heatmap of Passengers by Month and Year")
plt.show()