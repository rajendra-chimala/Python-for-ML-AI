#20
# products = [" apple", "-Banana", "apricot", "banana ","mango","momo","------orange"]
# cleaned_data = [p.strip(" -").capitalize() for p in products]
# grouped_data = {}
# for p in cleaned_data:
#  key = p[0].upper()
#  grouped_data.setdefault(key, []).append(p)
 
# print(grouped_data)











# 19
# my_list = ["#Development", "#AI", "ML","#DSA","NLP"]
# C_D = [x.lstrip("#") if x.startswith("#") else x for x in my_list] 

# print("Cleaned Data: ", C_D)











#18
# raw_data = "$$$$@@@@&!!!Rajendra*___*---*^^^"
# cleaned_data = raw_data.strip("*-$!_-^@&") 
# print("Cleaned Data: ", cleaned_data)








# 17
# names = [" RAM ", "       sita", "gita  ", "HarI    ","    sita","hari  ", "   ram", "gita   ", " sita  ", "hari", "siTa ", "gita  ", "  ram", "SITA"]
# C_D = list(set(i.strip().capitalize() for i in names)) 
# print("Names After Cleaning and Capitalization: ",C_D)






# 16
# raw_data = {"name_": "Raju", "age_": 20, "city_": "Dhangadhi", "country_": "Nepal", "profession_": "Developer"}
# cleaned_data = {y.rstrip("_"): x for y, x in raw_data.items()} 

# print("Cleaned Data: ", cleaned_data)













# 15
# data = " good morning!           "
# output = data.strip().capitalize()

# print("Data After Cleaning and Capitalize : ", output)









# 14
# nestedList = [["  Rajendra Chimala  ", "  Binod Kumar  "], ["  Suresh Yadav  ", "  Karthik Sharma  "], ["  Ram Prasad  ", "  Sita Devi  "], ["  Gita Kumari  ", "  Sanjay Singh  "]]
# cleaned = [[item.strip() for item in sublist] for sublist in nestedList]

# print("Cleaned Nested List:", cleaned)










# 13
# text = "12345Welcome to Digital Pathshala"
# cleaned = text.lstrip("12345") 
# print("Data After Cleaning:", cleaned)







# 12
# raw_emails = [" ram@gmail.com", "sita@yahoo.com ","           rajendra@xmail.com"]
# cleanedEmails = [e.strip() for e in raw_emails] 
# print(cleanedEmails)





#11
# text = " WellCome to dIGITAl PathShala "

# formatedData = text.strip().title()

# print("Formated Data : ",formatedData)










#10
# myList = ["hello world", "good morning", "python programming", "data science"]
# result = [ml.title() for ml in myList] 
# print("Data After Title Case:")
# for item in result:
#     print(item)








# 9
# data = {"name": "Rajendra    ", "city": "Dhanghadhi   ", "country": "Nepal   ","age": "25   "}
# cleanedData = {k: v.rstrip() for k, v in data.items()} 
# print("Data After Cleaning:")
# for key, value in cleanedData.items():
#     print(f"{key}: {value}")





# 8
# rawNames = ["rajendra","binod","suresh","karthik","ram","sita","gita","sanjay"]

# capitalizeData = [name.capitalize() for name in rawNames]
# print("Names After Capitalization:")
# for name in capitalizeData:
#     print(name) 










#7 
# text = " *$!#  Rajendra Chimala    **$$!! "

# cleanText = text.strip("*$!# ")

# print(f"Data After Cleaning :  {cleanText}")





#6
# fruitNames = [" Apple        ", "    Banana    ", " Mango", "  Pomegranet   ", "  Pineapple   "]

# cleanedNames = [fName.strip() for fName in fruitNames]

# print("Cleaned Fruit Names:")
# for name in cleanedNames:
#     print(name)










# 5
# fullName = "rajendra chimala"

# TitledData = fullName.title()
# print(f"Data Before Title Case :  {fullName}")
# print(f"Data After Title Case :  {TitledData}")






# 4
# text = "he is one of the best programmers in the world."

# capitalizeData = text.capitalize()

# print(f"Data Before Capitalization :  {text}")
# print(f"Data After Capitalization :  {capitalizeData}")







# 3
# text  = "Rajenrda Chimala**$$!!"
# cleanData = text.rstrip("**$$!!")

# print(f"Data Before Cleaning :  {text}")
# print(f"Data After Cleaning :  {cleanData}")





# 2
# text = "*****###Rajendra Chimala"
# cleanData = text.lstrip("*#")

# print(f"Data Before Cleaning :  {text}")
# print(f"Data After Cleaning :  {cleanData}")









# 1
# text = "   Rajendra Chimala     "
# cleanData = text.strip()

# print(f"Data Before Cleaning :  {text}")
# print(f"Data After Cleaning :  {cleanData}")


