#basic calculator

def add(num1 , num2):
    return num1+num2

def sub(num1 , num2):
    return num1-num2

def mul(num1 , num2):
    return num1*num2

def div(num1 , num2):
    return num1/num2

print("Please select from the option below")
print("1. Addition")
print("2. Subraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice 1/2/3/4: ")

    if choice in ('1' , '2' , '3' , '4'):
        try:
            num1 = float(input("Enter the num1: "))
            num2 = float(input("Enter the num2: "))
        except:
            print("Invalid choice")
            continue

        if choice == '1':
            print(num1,"+" ,num2 ,"=",add(num1 , num2))
        elif choice == '2':
            print(num1 , "-", num2, "=",sub(num1 , num2))
        elif choice == '3':
            print(num1 , "*",num2 , "=" , mul(num1 , num2))
        elif choice == '4':
            print(num1 , "/" , num2 , "=" , div(num1 , num2))
        
        #Check if user want to continue
        next_cal = input("Want to do another calculation:(y/n): ")
        if next_cal == 'n':
            break #exit the loop
    else:
        print("Invalid choice")
