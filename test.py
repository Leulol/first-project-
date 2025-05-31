#1 Personal Information Collector
from leul import my_time


def personal_info_collector():
    print("=== Personal Information Collector ===")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    grade = input("Enter your grade: ")
    hobby = input("Enter your hobby: ")

    print("=== Collected Information ===")
    print(f"Hello, my name is {name}. I'm {age} years old and in Grade {grade}. I love {hobby}.")
    print(f"And I will be {age + 1} years old next year.")

if __name__ == "__main__":
    # This code runs only if the script is executed directly, not if imported
    personal_info_collector()

#2 Lucky Number Game
import random

def lucky_number_game():
    print("=== Lucky Number Game ===")
    lucky_number = random.randint(1, 10)  # Generate a random number between 1 and 10

    while True:
        guess = int(input("Guess my lucky number (between 1 and 10): "))
        if guess == lucky_number:
            print(f"Congratulations! You guessed it right. The number is {guess}")
            break
        elif guess < lucky_number:
            print("The lucky number is higher")
        elif guess > lucky_number:
            print("The lucky number is lower")

# To run only the lucky number game:
if __name__ == "__main__":
    lucky_number_game()

#3 simple chatbot
def chat_bot():
    print("=== Chat Bot ===")
    print("Hello! I'm a chat bot. What is your name?")
    name = input("Enter your name: ")
    print(f"Nice to meet you, {name}! I want to get some information about you.")

    while True:#loop to keep asking questions
        print("How old are you? And where do you learn?")
        age = int(input("Enter your age: "))
        school = input("Enter your school: ")
        print(f"So you are {age} years old and you learn at {school}. Nice!")

        print("What is your favorite subject?")
        subject = input("Enter your favorite subject: ")
        if subject.lower() == "ict":
            print("That's great! ICT is also my favorite subject.")
        else:
            print(f"{subject} is a great subject.")

        more = input("Do you want to answer more questions? (yes/no): ")
        if more.lower() != "yes":
            print("Thank you for chatting! Goodbye!")
            break

if __name__ == "__main__":
    chat_bot()

#5 temperature converter
def temperature_converter():
    print("=== Temperature Converter ===")
    print("Type 'C' to convert from Fahrenheit to Celsius.")
    print("Type 'F' to convert from Celsius to Fahrenheit.")
    print("Type 'K' to convert from Celsius to Kelvin")
    print("Type 'C!' to change from Kelvin to Celsius")
    print("Type 'F!' tp change from Kelvin to Fahrenheit")
    print("Type 'K!' to change from Fahrenheit to Kelvin")
    choice = input("Your choice (C/F/K/C!/F!/K!): ").strip().upper()

    if choice == 'C':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5 / 9
        print(f"{f}°F is {c:.2f}°C")#.2f will format the float number to 2 decimal places
    elif choice == 'F':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9 / 5) + 32
        print(f"{c}°C is {f:.2f}°F")#.2f will format the float number to 2 decimal places
    elif choice == 'K':
        c = float(input("Enter temperature in Celsius: "))
        k = c + 273
        print(f"{c}°C is {k:.2f}K")
    elif choice == 'C!':
        k = float(input("Enter temperature in Kelvin: "))
        c = k - 273
        print(f"{k}K is {c:.2f} Celsius")
    elif choice == 'F!':
        k = float(input("Enter temperature in Kelvin: "))
        f = 9 / 5 * (k - 273) + 32
        print(f"{k}Kelvin is {f:.2f}Fahrenheit")
    elif choice == 'K!':
        f = float(input("Enter temperature in Fahrenheit: "))
        k = 5 / 9 * (f-32) + 273
        print(f"{f} is {k:.2f}")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    temperature_converter()
#python calculater
def simple_calculater():
    print("which do you want (+)/(-)/(*)/(/)")
    arithmatic = input("(+)/(-)/(*)/(/): ")
    x = int(input("the value of x: "))
    y = int(input("the value of y: "))
    if arithmatic == "+":
        result = x + y
        print(int(result))
    elif arithmatic == "-":
        result = x - y
        print(int(result))
    elif arithmatic == "*":
        result = x * y
        print(int(result))
    elif arithmatic == "/":
        result = x / y
        print(int(result))
    else:
        print("invalid input")
if __name__ == "__main__":
    simple_calculater()
    # circumference
    print("===Circumference===")
    import math


def circumference():
    r = float(input("Enter the radius of the circle: "))
    c = float(2 * math.pi * r)
    print(f"The circumference of the circle is {c:.3f}")


if __name__ == "__main__":
    circumference()
# area
print("===Area===")


def area():
    r = float(input("Enter the radius of the circle: "))
    a = float(math.pi * pow(r, 2))
    print(f"The Area of the circle is {a:.3f}")
if __name__ == "__main__":
    area()
#Username validation
def user():
    username = input("Enter your user name:")
    if len(username) > 12:
        print("your user name is not valid")
    elif username.find(" ") == -1:
        print("There should not be any space in the user name")
    elif not username.isalpha():
        print("there should not be any digit")
    else:
        print(f"Welcome {username}!")
if __name__ == "__main__":
    user()

#count down by sec and min
import time
def timer():
my_time = int(input("enter the time in secondes: "))
for x in range(my_time, -1, -1):
    min = x / 60
    seconds = x % 60
    print(f"00:{min:.02}:{seconds:02}")
    time.sleep(1)#after each iteration you will sleep for 1 second or pause the program

print("TIMES UP!!")
if __name__ == "__main__":
    timer()
