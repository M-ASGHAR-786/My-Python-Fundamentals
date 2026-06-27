# What are Data Types and Typecasting?
# - Data Types: Think of data types like different building materials (e.g., wood vs. water).
#   You can build a chair with wood, but you cannot build it with water. Similarly, Python 
#   needs to know the "material" of a variable to perform the correct operations.
# - String (str): Text data wrapped in quotes (e.g., "5", "watching anime").
# - Integer (int): Whole numbers without decimals (e.g., 100).
# - Float (float): Numbers with decimal values (e.g., 365.25).
# - Typecasting: The process of manually converting a value from one data type to 
#   another (e.g., converting the string "5" to the number 5 so we can perform math).
# - IMPORTANT RULE: Typecasting only works if the source data is a VALID representation of 
#   the target type. You can convert the text "5" into an integer, but you cannot convert 
#   the text "Asghar" into an integer.

# 1. Defining Variables with Different Data Types
a = "5"                                 # String (text representation of a number)
b = "100"                               # String (text representation of a number)
day_in_year = 365.25                    # Float (decimal number)
fav_hobby = "watching anime"            # String (text value)
age = "21"                              # String (text representation of a number)
practice_hours = "5"                    # String (text representation of a number)

# 2. Checking Data Types using type()
# The type() function tells Python to reveal what data type is stored in a variable.
print(f"Data-Type of 'a': {type(a)}")                       # Outputs: <class 'str'>
print(f"Data-Type of 'day_in_year': {type(day_in_year)}")   # Outputs: <class 'float'>
print(f"Data-Type of 'fav_hobby': {type(fav_hobby)}")       # Outputs: <class 'str'>

print("-" * 50)  # Visual separator for the output console

# 3. String Concatenation vs. Arithmetic Addition
# When using "+" between two strings, Python joins (concatenates) them instead of doing math.
print(f"Adding 'a' and 'b' (As Strings): {a + b}")          # Outputs: 5100 (joins "5" and "100")

# To perform actual addition, we must typecast both string values into integers using int().
print(f"Adding 'a' and 'b' (Typecast to Int): {int(a) + int(b)}")  # Outputs: 105 (math addition)

print("-" * 50)

# 4. Coding Practice Calculations (Practical Scenario)
# Scenario: Calculating how many hours you will spend coding over a decade (10 years)
# if you practice exactly "practice_hours" every single day.

# Invalid Attempt:
# This causes an error because Python cannot multiply a Float (result of day_in_year * 10) by a String.
# # print(f"Total Hours: {day_in_year * 10 * practice_hours}")  # Invalid, yields TypeError (float multiplied by str)

# Valid Attempt with Typecasting:
# By typecasting "practice_hours" into a float (or int) first, the mathematical formula works.
total_hours = day_in_year * 10 * float(practice_hours)
print(f"Total Practice Hours in a decade: {total_hours}")   # Outputs: 18262.5

print("-" * 50)

# 5. Typecasting Limitations (Valid vs. Invalid Values)
# Python will throw a ValueError if you try to convert a value that does not look like the target type.

# # bad_conversion1 = int(fav_hobby)     # Invalid: Can't convert "watching anime" into an integer (ValueError)
# # bad_conversion2 = float("Asghar")     # Invalid: Can't convert name text into a float (ValueError)
# # bad_conversion3 = int("365.25")       # Invalid: Can't convert a decimal string directly into an integer (ValueError)

# Valid alternative for decimal text:
# To convert a decimal text to an integer, you must first convert it to a float, then to an integer.
valid_integer = int(float("365.25"))
print(f"Successfully converted '365.25' to Int: {valid_integer}")  # Outputs: 365