# Functions

# Functions to add two number 
def add(x, y):
    return x + y

# Functions to subtract two number
def subtract(x, y):
    return x - y

# Functions to multiply two number 
def multiply(x, y):
    return x * y

# Functions to divide two number 
def divide(x, y):
    return x / y

# Functions to find the remainder of two number 
def remainder(x, y):
    return x % y

# Functions to find the exponent of two number
def exponent(x, y):
    return x ** y 

# showing user calc menu
print("Select operation.") 
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Remainder")
print("6.Exponent")
# Take input from the user 
choice = input("Enter choice(1/2/3/4/5/6): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1' :
    print(num1,"+",num2,"=", add(num1,num2))

if choice == '2' :
   print(num1,"-",num2,"=", subtract(num1,num2))                                         
                                     
if choice == '3' :
    print(num1,"*",num2,"=", multiply(num1,num2))
         
    if choice == '4': 
        if num2 == 0:
            print("ERROR! NO ZEROS ALLOWED 😔")
        else:
            print(num1, "/", num2, "=", divide(num1, num2))
def divide(x, y):
    if y == 0:
        return "ERROR! NO ZEROS ALLOWED 😔"
    else:
        return x / y
if choice == '5' : 
    print(num1,"%",num2,"=", remainder(num1, num2)) 

if choice == '6' : 
  print(num1,"**",num2,"=", exponent(num1, num2)) 

else:
    print("Keep the caculator running")
   
    # Keep the calculator running
    
    while True:
       
        # show user calc menu
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Remainder")
        print("6.Exponent")
        print( "7.Exit")

        print("Type '7' '7' '7' to exit")
        
        # Take input from the user
        choice = input("Enter choice(1/2/3/4/5/6/7): ")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
       
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
       
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
       
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            print(num1, "%", num2, "=", remainder(num1, num2))
       
        elif choice == '6':
            print(num1, "**", num2, "=", exponent(num1, num2))
        
        elif choice == '7':
            break
        
        else:
            print("Keeps the calculator running")