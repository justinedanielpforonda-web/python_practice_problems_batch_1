# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

number_1 = float(input("Input the number: "))
number_2 = float(input("Input the second numer:"))

if number_1 > number_2:
    print(f"{number_1} is higher")
elif number_1 == number_2:
    print("Equal")
else:
    print(f"{number_2} is higher")