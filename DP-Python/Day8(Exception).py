# Exception Handling

while True:
            try:
                x = int(input("Enter a number: "))
                print(f"number = {x}")

            except ValueError:
                              print("Please Enter an Integer!!")
    
            else:
                 break