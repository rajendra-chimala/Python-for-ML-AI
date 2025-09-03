import matplotlib.pyplot as plt

# Bar Chart : It is used to show the discrete data.
# plt.style.use('fivethirtyeight')

department = ["Computer Science", "Electrical", "Civil", "Mechanical","Aerospace", "Computer Engineering", "AI/Ml", "Physics"]

no_of_students = [120, 60, 90, 80, 40, 50, 30, 60]


plt.bar(department, no_of_students, edgecolor = "black")


for i, value in enumerate(no_of_students):
    plt.text(i,value+2,str(value),ha="center")

plt.xlabel("Departments")
plt.ylabel("Number of Students")
plt.title("Number of students in each department of a college")
plt.xticks(rotation=45) 

plt.show()




# Histogram : It is help to show the distribution of continuous data.

plt.style.use('fivethirtyeight')

ages = [18, 19, 20, 21, 21, 22, 22, 23, 24, 24,
        25, 26, 26, 27, 28, 29, 30, 30, 31, 32]

plt.hist(ages,bins=10,color='skyblue', edgecolor='black')
plt.title("Age Distribution Histogram")
plt.xlabel("Age Range")
plt.ylabel("Number of Student")
plt.tight_layout()
plt.show()
