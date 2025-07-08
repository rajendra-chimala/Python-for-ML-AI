# Exception Handling


# Value Error
# while True:
#             try:
#                 x = int(input("Enter a number: "))
#                 print(f"number = {x}")

#             except ValueError:
#                               print("Please Enter an Integer!!")
    
#             else:
#                  break



# Zero Division Error

# while True:
#     try:
#         x = int(input("Enter a number [?]/[] : "))
#         y = int(input("Enter another number []/[?] : "))
#         result = x / y
#     except ZeroDivisionError:
#         print("Division by zero error. : ")
#         print(ZeroDivisionError.e)
#     except ValueError:
#         print("Please enter valid value.")
#     else:
#         print(f"Result [{x}]/[{y}] : {result}")
#         break

# def calc(x,y,z):
#     while True:
    
#         try:
#             res = (x+y)/z
#         except (ValueError,ZeroDivisionError) as x:
#             print(x)
#         else:
#             print(f"Result: {res}")
#             break
        

# def calcs(x,y,z):
#     while True:
#             try:
#                 res = x+y+z
#             except (ValueError,ZeroDivisionError) as x:
#                 print(x)
#             else:
#                 print(f"Result: {res}")
#                 break


# def calcm(x,y,z):
#     while True:
#             try:
#                 res = x*y*z
#             except (ValueError,ZeroDivisionError) as x:
#                 print(x)
#             else:
#                 print(f"Result: {res}")
#                 break
# def main():
#     myList = input("Enter any numbers [1 2 3]: ").split()
#     op = input("Enter your operation \n[1] (x+y)/z \n[2] x+y+z \n[3] x*y*z : ")
    
#     if op == '1':
#         calc(int(myList[0]), int(myList[1]), int(myList[2]))
#     elif op == '2':
#         calcs(int(myList[0]), int(myList[1]), int(myList[2]))
#     elif op == '3':
#         calcm(int(myList[0]), int(myList[1]), int(myList[2]))
#     else:
#         print("operation is not valid .")
    
    
    
# main()


# Multiple Exception at a Time

def div():
        try:
            a = int(input("Enter a number: "))
            b = int(input("Enter another number: "))
            result = a / b
        except (ValueError, ZeroDivisionError) as e:
            print(f"An error occurred: {e}")
        
        else:
            print(f"Result: {result}")


div()
    