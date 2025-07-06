
#30
# headings = [" heading1 ", "  HEADING2  ", " hEADING3", "Heading4  ", "  HEADING5"]
# cleaned_headings = sorted([c.strip().title() for c in headings])

# print("Cleaned Codes: ", cleaned_headings)




# 29
# raw_text = "_-Hello-_"
# cleaned_data = raw_text.strip("_-")

# print("Cleaned Data: ", cleaned_data)








#28
# raw_data = {"m1": " hello world ", "m2": "python is fun","m3": "  data science  ", "m4": "  machine learning  "}
# cleaned = {k: v.strip().capitalize() for k, v in raw_data.items()}
# print("Cleaned Data: ", cleaned)







# 27
# sentences = [" good morning    ", "Hello Everyone "," welcome to Digital Pathshala!  ", "  Python programming is fun.  "]
# unique_words = set()
# for i in sentences:
#  unique_words.update(i.strip().title().split())

# print("Unique Words After Cleaning and Capitalization: ", unique_words)












# 26
# names = [" ram ", "Sita", " HARI","GITa",]
# for i in range(len(names)):
#  names[i] = names[i].strip().title()
 
# print("Cleaned Names: ", names)







# 25
# raw_data = "345235good morning!$234           "
# cleaned_data = raw_data.strip("0123456789").rstrip("0123456789!$ ").title() 

# print("Data After Cleaning and Title Case: ", cleaned_data)











# 24
# raw_emails = [" Ram@Example.com", "sitA@EXAMPLE.COM "]
# cleaned_emails = [i.strip().split("@")[0].capitalize() + "@" + i.strip().split("@")[1].lower() for i in raw_emails]

# print("Cleaned Emails: ", cleaned_emails)












# 23
# def c_title(r):
#  return ' '.join([i.capitalize() for i in r.split()])

# raw = input("Enter a string: ")
# res = c_title(raw) 

# print("Formatted String :", res)






# 22
# raw_data = {"animals": [" rat", "rabbit ","  tiger"], "plants": ["palm ", " apple","neem"]}
# cleaned_data = {i: [j.strip().title() for j in x] for i, x in raw_data.items()}

# print("Cleaned Data: ", cleaned_data)








#21
# raw_data = {"***ram***", "  sita    ", " Gita@@@@@@@@@@@@@@@ ","333333333hari-----"}
# cleaned_data = {rd.strip("*@3- ").capitalize() for rd in raw_data} 
# print("Cleaned Data: ", cleaned_data)









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


