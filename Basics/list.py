marks = [12,32,49]
# print(marks[-2])

marks.append(100) #it is used to append element in the list after the last element
marks.insert(3,20) #It is used to insert the element in the particulat index field
print("That is returning the element that is exist in the list or not : [12] ",12 in marks) #It is used to find the element in the list 
print("That is the length of the list : ",len(marks)) #It is used to find the length of the list


for mark in marks:
    print(mark)