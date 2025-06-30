# split()
# capitalize()
# title()

# name = "   ---- rajendra @@ chmala 1 2 3 4 ___ "

# # Result : Rajendra Chimala

# new_name = name.strip(" -1234_")
# print(new_name)

# data = new_name.replace(" @@ ", " ").title()
# print(data)

# first_name,last_name = data.split()
# # ndata = data.split()

# # print(type(ndata))
# print("First Name : ",first_name)
# print("Last Name : ",last_name)


# name = "  __--&*)firoj ##&& karki 123 @@(*"
# data = name.strip(" _-@123()*&").replace(" ##&& "," ")
# first_name,last_name = data.split()
# print("First Name : ",first_name.title(),"\nLast Name : ",last_name)

# pn = "(+977)9868821573"
# number = pn.split(")")
# print(number[1])

text = " $$ Samip ** % (+977)9800000000"

data = text.split(")")
name = data[0]
new_name = name.split()

print("first_name : ",new_name[1])
print("ph_no : " ,data[1])

