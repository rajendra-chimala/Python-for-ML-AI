principal_amt = int(input("Enter The Principal Amount [Rs] : "))
rate = int(input("Enter The Interest Rate [%] : "))
time = int(input("Enter The Time [in Year] : "))

interest = (principal_amt*time*rate)/100

print("The Interest of ",principal_amt," is after",time," with the rate of ",rate," is ",interest)