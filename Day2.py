"""
Day 2 – Conditional Logic

Concepts:
- if, elif, else
- comparison operators
- logical operators (and, or)
- nested conditions
"""

# Program 1: check whether the number is Even or Odd
number = int(input("Enter a number: "))
if (number%2) == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd.")



# Program 2: check if the number is  Positive / Negative / Zero
number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# Program 3: Largest of 3 Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f"The largest number is: {largest}")

# Program 4: Grade System based on marks
marks = float(input("Enter your marks: "))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is: {grade}")

# Program 5: simple calculator using if-else
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1/num2
else:
    print("Invalid operation")
print(f"Result: {result}")


# Program 6: Shipping cost / discount rules
order_amount = float(input("Enter order amount: "))
is_premium_member = input("Are you a premium member? (yes/no): ").strip().lower()
if is_premium_member == 'yes':
    shipping_cost = 0
else:
    if order_amount >= 100:
        shipping_cost = 0
    elif order_amount >= 50:
        shipping_cost = 5
    else:
        shipping_cost = 10
print(f"Shipping cost: ${shipping_cost}")

