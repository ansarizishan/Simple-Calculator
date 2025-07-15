#for addition, subtractio, multiplication, division and average
def addition (a, b):
    return a + b
def subtraction (a, b):
    return a - b
def multiplication (a, b):
    return a * b
def division (a, b):
    return a / b
def average (a, b):
    return (a + b) / 2

select = print(f"You can perform following calcultion : \n" "1. Addition \n" "2. Subtraction \n" "3. Multiplication \n" "4. Division \n" "5. Average \n") 
select = int(input(f"Enter the number from (1-5):"))

num1 = int (input ("Enter the 1st number "))
num2 = int (input ("Enter the 2nd number "))

if select == 1:
    print(f"{num1} + {num2} = ", addition(num1, num2))
elif select == 2:
    print(f"{num1} - {num2} = ", subtraction(num1, num2))
elif select == 3:
    print(f"{num1} * {num2} = ", multiplication(num1, num2))
elif select == 4:
    print(f"{num1} / {num2} = ", division(num1, num2))
elif select == 5:
    print(f"({num1} + {num2})/2 = ", average(num1, num2))
else:
    print("Please select right number form above. Try again!")