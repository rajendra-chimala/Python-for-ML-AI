
# User Define Function
# def addition(x, y):
#     return (f"Sum : {x + y}")

# sum_result = addition(5, 10)
# print(type(sum_result)) 

# print("Sum of 5 and 10 is:", sum_result)

# ---------------------------------------------------------------------
# Task 1
# def great(name):
#     print(f"Hello {name}, Welcome to Python Programming!")
    
# name = input("Enter your name: ")
# great(name)

# Task 1 Update


# def main():
#     user_name = input("Enter your name: ")
#     greet(user_name)

# def greet(name= "Rajendra"):
#     print(f"Hello, {name}!")

# if __name__ == "__main__":
#     main()

# def choice():
#     print("1. Celsius to Fahrenheit")
#     print("2. Fahrenheit to Celsius")
#     print("3. Exit")
#     ch = int(input("Enter your choice: "))
#     match ch:
#         case 1:
#             c = float(input("Enter temperature in Celsius: "))
#             f = ctof(c)
#         case 2:
#             f = float(input("Enter temperature in Fahrenheit: "))
#             c = ftoc(f)
#         case 3:
#             print("Exiting the program.")
#             return None
    
# def ctof(c):
#     fahrenheit = (c * 9/5) + 32
#     print(f"{fahrenheit} Fahrenheit")

# def ftoc(f):
#     celsius = (f - 32) * 5/9
#     print(f"{celsius} Celsius")

# def main():
   
#     choice()

# if __name__ == "__main__":
#     main()

# --------------------------------------------------------------------------------------

# Task 3

# def max_number(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
    
# print(max_number(10, 20, 30)," is Maximum Number")

# def main():
#     print("Enter three numbers to find the maximum:")
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     num3 = float(input("Enter third number: "))
    
#     max_num = max_number(num1, num2, num3)
#     print(f"The maximum number is: {max_num}")
    
# main()
    
# --------------------------------------------------------------------------------------------
# Task 4

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    if y == 0:
        return "Division by zero error."
    return x / y

def main():
    print("Enter your operation [x operator y] : ")
    data = input()
    datas = data.split()
    
    if(datas[1] == '+'):
        result = addition(float(datas[0]), float(datas[2]))
        print(f"Result: {result}")
    elif(datas[1] == '-'):
        result = subtraction(float(datas[0]), float(datas[2]))
        print(f"Result: {result}")
    elif(datas[1] == '*'):
        result = multiplication(float(datas[0]), float(datas[2]))
        print(f"Result: {result}")
    elif(datas[1] == '/'):
        result = division(float(datas[0]), float(datas[2]))
        print(f"Result: {result}")
    else:
        print("Invalid operation")
   
    
main()