"""
Day 3 - Loops & Control Flow

Concepts covered:
- for loop, while loop
- range()
- break, continue, pass
"""

# Program 1 - Print numbers from 1 to N using a for loop.
# N=int(input("Enter The number: "))
# for i in range(1,N+1):
#     print(i)

# Program 2 -Print numbers from N to 1 using range() (reverse loop).
# N1=int(input("Enter the number: "))
# for i in range(N1,0,-1):
#     print(i)
#
# Program 3 -Print only even numbers between 1 and N.
# N2= int(input("Enter the number"))
# for i in range(1,N2+1):
#     if i % 2 == 0:
#         print(i)
#
# Program 4-Calculate the sum of numbers from 1 to N using a while loop.
# N3= int(input("Enter the number"))
# i=1
# total=0
# while i<=N3:
#     total=total + i
#     i = i+1
# print(f"The sum is: {total}")
#
# Program 5- Count the number of digits in a given number.
# N4= int(input("Enter the number"))
# count =0
# if N4 == 0:
#     count =1
# else:
#     while N4 > 0:
#         count = count + 1
#         N4= N4//10
#
# print(f"The number count is: {count}")
#
# Program 6-Check whether a number is prime.
# Prime number is = Greater than 1 and Divisible only by 1 and itself
# N5= int(input("Enter the number"))
# if N5 <=1:
#     print("Number is not prime")
# for i in range(2,N5):
#     if N5 % i == 0:
#         print ("not prime")
#         break
#     else:
#         print("prime")
# #
# Program 7-Print all prime numbers between 1 and N.
# N5= int(input("Enter the number"))
# for num in range(2,N5 + 1):
#     is_prime = True
#
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)
#
# Program 8-Find the factorial of a number.
# number= int(input("Enter the number"))
# if number <0:
#     print("Factorial is not defined for negative numbers")
# else:
#     factorial= 1
#     for i in range(1,number+1):
#         factorial= factorial * i
# print(f"factorial of {number} is {factorial}")

# Program 9-Reverse a number ..Example: 123 → 321
# number=int(input("enter the number"))
# reverse = 0
# original= number
# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number= number // 10

# print(f"reverse of {original} is {reverse}")
#
# # Program 10- Check if a number is a palindrome.
# num = int(input("Enter a number: "))
#
# original = num
# reverse = 0
#
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
#
# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Program 11- Find the first number divisible by 7 between 1 and N (use break).
# N = int(input("Enter N: "))
#
# for i in range(1, N + 1):
#     if i % 7 == 0:
#         print(f"First number divisible by 7 is {i}")
#         break
# else:
#     print("No number divisible by 7 found.")
# Program 12 -Print numbers from 1 to 20 but skip multiples of 3 (use continue).
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)
# Program 13 -Stop reading numbers when the user enters a negative number.
# while True:
#     number = int(input("Enter a number: "))
#
#     if number < 0:
#         print("Negative number entered. Stopping...")
#         break
#
#     print(f"You entered: {number}")
# Program 14 -Keep taking numbers from the user until 0 is entered, then stop.
# while True:
#     number = int(input("Enter a number (0 to stop): "))
#
#     if number == 0:
#         print("Zero entered. Stopping...")
#         break
#
#     print(f"You entered: {number}")
# Program 15- Password retry system — allow maximum 3 attempts.
# correct_password = "hello123"
# attempts = 0
#
# while attempts < 3:
#     entered_password = input("Enter password: ")
#
#     if entered_password == correct_password:
#         print("Access granted")
#         break
#     else:
#         attempts += 1
#         print("Incorrect password")
#
# if attempts == 3:
#     print("Account locked. Maximum attempts reached.")
# Program 16 -Guess-the-number game (stop when guessed correctly).
# secret_number = 7
# attempts = 0
#
# while True:
#     guess = int(input("Guess the number: "))
#     attempts += 1
#
#     if guess == secret_number:
#         print(f"Correct! You guessed it in {attempts} attempts.")
#         break
#     elif guess < secret_number:
#         print("Too low.")
#     else:
#         print("Too high.")
# Program 17 -Create an empty if block using pass.
# number = int(input("Enter a number: "))
#
# if number > 0:
#     pass  # Logic to be added later
#
# print("Program finished.")
#
# Program 18 -Menu-driven program skeleton using pass for unimplemented options.
# while True:
#     print("\n===== MENU =====")
#     print("1. View Profile")
#     print("2. Update Profile")
#     print("3. Delete Profile")
#     print("4. Exit")
#
#     choice = input("Enter your choice (1-4): ")
#
#     if choice == "1":
#         print("Viewing profile...")
#
#     elif choice == "2":
#         pass  # TODO: Implement update logic later
#
#     elif choice == "3":
#         pass  # TODO: Implement delete logic later
#
#     elif choice == "4":
#         print("Exiting program...")
#         break
#
#     else:
#         print("Invalid choice. Please try again.")