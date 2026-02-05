"""
Day 1 - Python Basics & Syntax
Topics: variables, data types, type casting, f-strings, basic arithmetic
"""

#Program 1- Print name, age, city using variables & f-string
name="Anu"
age=30
city="SF"

print(f"My Name is {name}. I am {age} years old and I live in {city}")

# Program 2- Take two numbers and print sum, difference, product

a=10
b=20
print(f"The sum of two numbers are {a+b}")
print(f"Differences are {a-b}")
print(f"The multiplication of two numbers are {a*b}")

# Program 3-Convert string number to int and add 10

marks=int(input("Enter the marks: "))
print(marks+10)

# Program 4- Swap two variables

v1=20
v2=40
temp=v1
v1=v2
v2=temp
print(v1)
print(v2)

# Program 5-Check datatype of a variable

print(type(name))
print(type(age))
print(type(b))

# Program 6-Calculate simple interest

principal=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of interest: "))
time=float(input("Enter the time in years: "))
simple_interest=(principal*rate*time)/100
print(f"The simple interest is: {simple_interest}")