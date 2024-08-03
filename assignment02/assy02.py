# problem1

first_number : int = int(input("Enter the first number: "))
second_number : int  = int(input("Enter the second number: "))
total_sum : int = first_number + second_number
print(f"The sum of {first_number} and {second_number} is {total_sum}.")

#problem2

favorite_animal: str = input("What's your favorite animal? ")
print(f"My favorite animal is also {favorite_animal}!")

#problem3



fahrenheit: float = float(input("Enter temperature in Fahrenheit: "))
celsius: float = (fahrenheit - 32) * 5.0 / 9.0
print(f"Temperature: {fahrenheit:.1f}F = {celsius:.2f}C")


# problem4

side1: float = float(input("What is the length of side 1? "))
side2: float = float(input("What is the length of side 2? "))
side3: float = float(input("What is the length of side 3? "))
perimeter: float = side1 + side2 + side3
print(f"The perimeter of the triangle is {perimeter}")

#problem5


entered_num: float = float(input("Type a number to see its square: "))
square: float = entered_num ** 2
print(f"{entered_num} squared is {square}")

# problem6

numbers: list[int] = [1, 2, 3, 4, 5]
del numbers[2]
print(numbers)

#problem7


list1: list[int] = [1, 2, 3]
list2: list[int] = [4, 5, 6]
list1.extend(list2)
print(list1)

# problem8

color_list = ['red', 'blue', 'green', 'yellow']
index_of_green = color_list.index('green')
print(f"The index of 'green' is {index_of_green}")

#problem9

def get_last_element(lst):
    
    last_element = lst[-1]
    print(last_element)
get_last_element([1, 2, 3, 4, 5])  


# problem10

def collect_values():
    values = []
    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)
    print(f"Here's the list: {values}")


collect_values()
