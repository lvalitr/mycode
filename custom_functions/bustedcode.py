#!/usr/bin/env python3

def calculator():  # Added colon to function definition
    num1 = int(input("Enter your first number: "))   # Added missing quotation marks and converted input to int
    num2 = int(input("Enter your second number: "))  # Added missing quotation marks and converted input to int
    print(f"{num1} + {num2} = {num1 + num2}")        # Fixed f-string formatting for proper variable substitution

calculator()  # Added function call to execute the calculator







