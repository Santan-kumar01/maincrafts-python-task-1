# MAINCRAFTS TECHNOLOGY
# Python Programming Internship - Task 1
# Core Python Challenges


# 1. Sum of Two Numbers
def sum_of_two_numbers():
    print("\n--- 1. Sum of Two Numbers ---")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Sum =", num1 + num2)


# 2. Odd or Even Checker
def odd_or_even():
    print("\n--- 2. Odd or Even Checker ---")

    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")


# 3. Factorial Calculation
def factorial_calculation():
    print("\n--- 3. Factorial Calculation ---")

    num = int(input("Enter a non-negative integer: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return

    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print(f"Factorial of {num} =", factorial)


# 4. Fibonacci Sequence
def fibonacci_sequence():
    print("\n--- 4. Fibonacci Sequence ---")

    n = int(input("Enter the number of Fibonacci terms: "))

    if n <= 0:
        print("Please enter a positive number.")
        return

    first = 0
    second = 1

    print("Fibonacci Sequence:")

    for _ in range(n):
        print(first, end=" ")
        first, second = second, first + second

    print()


# 5. String Reverse
def string_reverse():
    print("\n--- 5. String Reverse ---")

    text = input("Enter a string: ")

    print("Reversed string:", text[::-1])


# 6. Palindrome Check
def palindrome_check():
    print("\n--- 6. Palindrome Check ---")

    text = input("Enter a word: ")
    text = text.lower()

    if text == text[::-1]:
        print(f"{text} is a Palindrome")
    else:
        print(f"{text} is NOT a Palindrome")


# 7. Leap Year Check
def leap_year_check():
    print("\n--- 7. Leap Year Check ---")

    year = int(input("Enter a year: "))

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")


# 8. Armstrong Number
def armstrong_number():
    print("\n--- 8. Armstrong Number ---")

    num = int(input("Enter a number: "))

    if num < 0:
        print("Negative numbers are not considered Armstrong numbers.")
        return

    order = len(str(num))

    sum_val = sum(int(digit) ** order for digit in str(num))

    if num == sum_val:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is NOT an Armstrong number")


# Main Program
def main():
    print("=" * 55)
    print("MAINCRAFTS TECHNOLOGY")
    print("Python Programming Internship - Task 1")
    print("Core Python Challenges")
    print("=" * 55)

    sum_of_two_numbers()
    odd_or_even()
    factorial_calculation()
    fibonacci_sequence()
    string_reverse()
    palindrome_check()
    leap_year_check()
    armstrong_number()

    print("\n" + "=" * 55)
    print("All 8 challenges completed successfully!")
    print("=" * 55)


if __name__ == "__main__":
    main()