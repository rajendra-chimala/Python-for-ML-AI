import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.0)

tips = sns.load_dataset("tips")
# --------------------------
#Violin plot
#---------------------------
plt.figure(figsize=(8,5))
sns.violinplot(data = tips, x = "day", y = "total_bill", hue = "sex")
plt.title("Violin Plot of total_bill by day and sex")
plt.show()

#------------------------
#Count Plot
#------------------------
plt.figure(figsize = (7,4))
sns.countplot(data = tips, x = "day", hue = "sex")
plt.title("Count Plot of records by day and sex")
plt.show()


# -----------------------
# Facet Grid
# -----------------------
g = sns.FacetGrid(tips, col="time", row="smoker", margin_titles=True)
g.map(sns.scatterplot, "total_bill", "tip", alpha=0.7   )
g.add_legend()
plt.subplots_adjust(top=0.9)
g.fig.suptitle('Scatter Plot of Total Bill vs Tip by Time and Smoker Status')
plt.show()



# ------------------------
# LM Plot or Regression Plot
# ------------------------

sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker",  palette="Set1")
plt.title("Regression Plot of Tip vs Total Bill by Smoker Status")
plt.show()