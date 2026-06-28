# ---------------------------Understanding the input() Function---------------------------#

# What is the input() Function?
# - Think of the input() function as an empty blank space on a paper form.
# - Instead of a pre-filled form (static variables), the program hands the user
#   a pen and says: "Write your answer here." 
# - The program completely pauses and waits for the user to type their answer 
#   and press the "Enter" key before it can continue.
# - CRUCIAL RULE: The input() function ALWAYS returns the user's input as a String (str).
#   Even if the user types the number 5, Python reads it as the text "5".
# - To do mathematical operations on user input, we must convert ("typecast") that string 
#   into an Integer (int) or a Floating-point number (float) first.

# 1. Capturing and Displaying Basic Text Input
# We type-hint the variable as a string (str) because input() always yields text.
user_name: str = input("Enter your name: ")
print(f"Welcome to the coding journey, {user_name}!")

print("-" * 50)  # Visual separator for console output

# 2. The String Trap (The Common Beginner Mistake)
# If we want to calculate the user's age next year, we cannot use the raw string directly.
# # age_text: str = input("Enter your age: ")
# # next_year: int = age_text + 1            # Invalid: TypeError! Cannot add integer to string (uncomment to test)

# 3. Correct Method: Capturing and Typecasting Input
# We capture the user's age as text first, then convert it to an integer to do math.
age_input: str = input("Enter your age: ")  # Captures input as a string (e.g., "21")
age: int = int(age_input)                   # Typecasts the string "21" into integer 21
print(f"Next year, you will be: {age + 1} years old!")

print("-" * 50)

# 4. Capturing Decimal Input (Floats)
# Scenario: Calculating total weekly practice hours.
practice_input: str = input("Enter your daily practice hours (decimals allowed): ")
daily_hours: float = float(practice_input)  # Typecasts the string (e.g., "2.5") into float 2.5
weekly_hours: float = daily_hours * 5
print(f"If you follow this routine, you will practice: {weekly_hours} hours in a 5-day week!")

# ---------------------------Understanding the input() Function---------------------------#