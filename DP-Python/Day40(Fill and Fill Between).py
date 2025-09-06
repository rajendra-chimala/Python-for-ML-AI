import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv(r"sample_data/data.csv")
ages = data["Age"]
dev_salaries = data["All_Devs"]
py_salaries = data["Python"]
js_salaries = data["JavaScript"]

plt.plot(ages, dev_salaries, linestyle = "-",
         label = "Full Stack Devs")
# plt.fill_between(ages,dev_salaries, color = "skyblue", alpha = 0.25)

plt.plot(ages, py_salaries, label = "Pyhton Devs")

plt.fill_between(ages, py_salaries, dev_salaries, where = (py_salaries > dev_salaries),
                 interpolate = True, color = "blue", alpha = 0.25, label = "Above Full Stack Devs")

plt.fill_between(ages, py_salaries, dev_salaries, where = (py_salaries <= dev_salaries),
                 interpolate = True, color = "red", alpha = 0.25, label = "Below Full Stack Devs")

plt.legend()
plt.title("Median Salaries in USD by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary in USD")

plt.tight_layout()
plt.show()


# =============================================================================================================================


import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv(r"sample_data/data-2.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

most_repeated = language_counter.most_common(10)
language = []
popularity = []

for item in most_repeated:
    language.append(item[0])
    popularity.append(item[1])

language.reverse()
popularity.reverse()
plt.barh(language, popularity)
plt.title("Most Popular Languages")
plt.xlabel("Popularity")
plt.ylabel("Programming Languages")
plt.show()
plt.tight_layout()


