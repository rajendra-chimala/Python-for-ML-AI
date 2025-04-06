num1 = int(input("Enter first number : "))
operator = input("Enter operator [+ , - , x , / , % ]: ")
num2 = int(input("Enter second number : "))

if operator == '+':
    print("The sum is : ",num1+num2)
elif operator == '-' :
    print("The Sub is : ",num1-num2)
elif operator == 'x' :
    print("The product is : ",num1*num2)
elif operator == '/' :
    if num2!= 0:
        print("The division is : ",num1/num2)
    else:
        print("Error! Division by zero is not allowed.")
elif operator == '%':
    if num2!= 0:
        print("The modulus is : ",num1%num2)
    else:
        print("Error! Division by zero is not allowed.")
else :
    print("Invalid operator! Please use one of the following: +, -, x, /, %.")


