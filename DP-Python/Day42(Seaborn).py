import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.0)

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")   # for heatmap example
iris = sns.load_dataset("iris")         # for pairplot

# ----------------------------
# 1. Histogram + KDE
# ----------------------------
plt.figure(figsize=(8,3))
sns.histplot(tips.total_bill, kde=True)
plt.title("Histogram + KDE (total_bill)")
plt.show()

# ----------------------------
# 2. Scatter with hue & size
# ----------------------------
plt.figure(figsize=(7,5))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", size="size", sizes=(20,200))
plt.title("Tip vs Total Bill (hue=day, size=party size)")
plt.show()

# ----------------------------
# 3. Box + swarm combined
# ----------------------------
plt.figure(figsize=(8,5))
sns.boxplot(data=tips, x="day", y="total_bill")
sns.swarmplot(data=tips, x="day", y="total_bill", color="k", alpha=0.6)
plt.title("Boxplot with swarm overlay")
plt.show()

# ----------------------------
# 4. Regression per smoker status (lmplot)
# ----------------------------
sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker", height=4, aspect=1.2)
plt.title("Linear Regression by smoker status")
plt.show()

# ----------------------------
# 5. Correlation heatmap (numeric columns)
# ----------------------------
plt.figure(figsize=(6,5))
corr = tips.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation (tips dataset)")
plt.show()

# ----------------------------
# 6. FacetGrid scatter by time (Lunch/dinner)
# ----------------------------
g = sns.FacetGrid(tips, col="time", height=4)
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
plt.show()

# ----------------------------
# 7. Violin plot (distribution by category)
# ----------------------------
plt.figure(figsize=(8,5))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
plt.title("Violin plot of total_bill by day and sex")
plt.show()

# ----------------------------
# 8. Strip plot (all points with jitter)
# ----------------------------
plt.figure(figsize=(8,5))
sns.stripplot(data=tips, x="day", y="tip", hue="sex", dodge=True, jitter=True, alpha=0.7)
plt.title("Strip plot of tips by day and sex")
plt.show()

# ----------------------------
# 9. Count plot (frequency of categories)
# ----------------------------
plt.figure(figsize=(7,4))
sns.countplot(data=tips, x="day", hue="sex")
plt.title("Count of records by day and sex")
plt.show()

# ----------------------------
# 10. Point plot (mean with confidence interval)
# ----------------------------
plt.figure(figsize=(8,5))
sns.pointplot(data=tips, x="day", y="tip", hue="sex", dodge=True, markers=["o", "s"], capsize=0.1)
plt.title("Point plot (mean tip by day and sex)")
plt.show()

# ----------------------------
# 11. Joint plot (scatter + marginals)
# ----------------------------
sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg", height=6)
plt.suptitle("Joint plot of total_bill vs tip", y=1.02)
plt.show()

# ----------------------------
# 12. Pair plot (multi-variable relationships)
# ----------------------------
sns.pairplot(iris, hue="species", diag_kind="kde")
plt.suptitle("Pairplot of Iris dataset", y=1.02)
plt.show()

# ----------------------------
# 13. Residual plot (residuals from linear regression)
# ----------------------------
plt.figure(figsize=(7,4))
sns.residplot(data=tips, x="total_bill", y="tip", lowess=True)
plt.title("Residual plot: tip ~ total_bill")
plt.show()

# ----------------------------
# 14. Heatmap of pivoted data (time series like flights)
# ----------------------------
fp = flights.pivot(index="month", columns="year", values="passengers")
plt.figure(figsize=(12,6))
sns.heatmap(fp, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Heatmap of passengers by month and year")
plt.show()
