"""
Exercise 5: Basic Operator Calculator
Create a program that takes two numbers and a math operator (+, -, *, /) from the user, performs the corresponding calculation, and prints the result.

Sample Input: num1=15, num2=3, operator='/'
Sample Output: Result: 5.0

"""

def main():
    num1 = int(input("num1= "))
    num2 = int(input("num2= "))
    operator = input("operator= ")

    if operator == '+':
        print(f"{num1} + {num2} = {num1+num2}")
    elif operator == '-':
        print(f"{num1} - {num2} = {num1-num2}")
    elif operator == '*':
        print(f"{num1} * {num2} = {num1*num2}")
    elif operator == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"{num1} / {num2} = {num1/num2}")
    else:
        print(f"{operator} is an invalid operator.")

main()