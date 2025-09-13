import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.0)

tips = sns.load_dataset("tips")

# ----------------------------
# 1. Plot Histogram + KDE
# ----------------------------

# plt.figure(figsize=(8,3))
# sns.histplot(tips["tip"], stat="density", alpha=0.5)  # histogram only
# sns.kdeplot(tips["tip"], color="green", linewidth=2)  # KDE curve
# plt.title("Histogram + KDE (tip)")
# plt.tight_layout()
# plt.show()




# ----------------------------
# 2. Scatter with hue & size
# ----------------------------

# plt.figure(figsize=(7,5))
# sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", size="size", sizes=(20,200))
# plt.title("Tip vs Total Bill (hue=day, size=party size)")
# plt.show()
# plt.tight_layout()


# ----------------------------
# 3. Box + swarm combined
# ----------------------------



# plt.figure(figsize=(8,5))
# sns.boxplot(data=tips, x="day", y="total_bill")
# sns.swarmplot(data=tips, x="day", y="total_bill", color="k", alpha=0.6)
# plt.title("Boxplot with swarm overlay")
# plt.tight_layout()
# plt.show()