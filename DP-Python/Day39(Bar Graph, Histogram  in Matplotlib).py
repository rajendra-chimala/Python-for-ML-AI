import matplotlib.pyplot as plt

# Bar Chart : It is used to show the discrete data.
# plt.style.use('fivethirtyeight')

# department = ["Computer Science", "Electrical", "Civil", "Mechanical","Aerospace", "Computer Engineering", "AI/Ml", "Physics"]

# no_of_students = [120, 60, 90, 80, 40, 50, 30, 60]
# sd = department.sort()
# sorted = no_of_students.sort()

# plt.bar(sd, sorted, edgecolor = "black")


# # Zoom out vertically (Y-axis)
# # plt.ylim(0, 00)  # Max Y value = 40

# # Zoom out horizontally (X-axis)
# # plt.xlim(-0.5, len(labels)-0.5)


# for i, value in enumerate(no_of_students):
#     plt.text(i,value+2,str(value),ha="center")

# plt.xlabel("Departments")
# plt.ylabel("Number of Students")
# plt.title("Number of students in each department of a college")
# plt.xticks(rotation=45) 

# plt.show()




# Histogram : It is help to show the distribution of continuous data.

plt.style.use('fivethirtyeight')

datas = [2,5,3,7,5,9,78,90,23,34,12,46,6,4,34,67,54,76,34,98,7,6,67,86,49,99]

plt.hist(datas,bins=20,color='skyblue', edgecolor='black')
plt.title("Basic Histogram")
plt.xlabel("Bins (Value Ranges)")
plt.ylabel("Frequency")
plt.show()
