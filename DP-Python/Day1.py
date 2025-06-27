print("Hello World !")
# name = "Rajendra Chimala"
# age = 19
# height = 5.7

name= input("Enter Your Name : ")
age = int(input("Enter your Age : "))
height = float(input("Enter Your Height : "))

if(age>=18):
    isAdult = True
else:
    isAdult = False

print(name," Type : ",type(name))
print(age," Type : ",type(age))
print(height," Type : ",type(height))
print(isAdult," Type : ",type(isAdult))

