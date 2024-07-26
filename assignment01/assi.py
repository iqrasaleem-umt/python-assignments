# progrma1
# Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.
# Your code should store each person's age to a variable and print their names and ages at the end
anton_age: str = "21"  
beth_age: str = str(int(anton_age) + 6) 
chen_age: str = str(int(beth_age) + 20)
drew_age: str = str(int(chen_age) + int(anton_age)) 
ethan_age: str = chen_age

# Print the ages
print(f"Anton is {anton_age} years old.")
print(f"Beth is {beth_age} years old.")
print(f"Chen is {chen_age} years old.")
print(f"Drew is {drew_age} years old.")
print(f"Ethan is {ethan_age} years old.")

# program2
# Task: Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables

person_name : str  = "Alice"
person_age  : int  =  30
person_city : str  =  "newyork"
personinfo  : str  =  f"""
 {person_name} is {person_age} years old and live in {person_city}
"""
print(personinfo)

# program3

# Task: Given the string s, use string methods to:
# Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
# Convert to uppercase: change all characters in the string to uppercase.
# Convert to lowercase: change all characters in the string to lowercase.

sir_name : str = "sir zia"
print(sir_name.title())
print(sir_name.upper())
print(sir_name.lower())

# program4
# Task: Given the string s, use string methods to:
# Replace "Python" with "Java": substitute "Python" with "Java".

msg : str = "I love programming in Python"
updatemsg : str  = msg.replace("Python", "Java")
print(updatemsg)
  
# program5
# ask: Given the string s, use string methods to:
# Split into a list: break the string into a list of substrings based on the delimiter ,.
# Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
 
fruits : str = "apple,banana,cherry,dates"
split_list = fruits.split(',')
print(split_list)
joined_string = ' '.join(split_list)
print(joined_string)

# program6


s : str = "   Python is fun!   "
trimmed : str = s.strip()
left_justified = trimmed.ljust(20, '*')
right_justified = trimmed.rjust(20, '*')
print(trimmed)
print(left_justified)
print(right_justified)


#program7

sentence: str = "the quick brown fox jumps over the lazy dog"
index_of_fox = sentence.find("fox") 
count_the = sentence.count("the")
print(f"index of 'fox' is {index_of_fox}")
print(f"'the' appears {count_the} times")


# program8
# Convert an integer to its binary representation

# Task: Given an integer num
# Obtain the binary representation of num
num : int = 45
result : str = bin(num)
print(result)








# program9
# ask: Given two integers base and exponent
# Compute base raised to the power of exponent.
number1 : int = 3
number2 : int = 4
print(number1**number2)

# program10

# Task: Given a floating-point number value
# Round value to the nearest integer.
# Round value to two decimal places.

value : float = 12.34567
rounded_to_integer : int = round(value)
rounded_to_two_decimal_places : float = round(value, 2)
print(f"Rounded to nearest integer: {rounded_to_integer}")
print(f"Rounded to two decimal places: {rounded_to_two_decimal_places}")




s = "the quick brown fox jumps over the lazy dog"
index_of_fox = s.find("fox")
count_of_the = s.count("the")
print(f"Index of 'fox' is {index_of_fox}")
print(f"'the' appears {count_of_the} times")