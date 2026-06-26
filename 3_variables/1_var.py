# What is a Variable?
# - A variable is like a container (or a labeled box) used to store data values.
# - In Python, a variable is created the moment you first assign a value to it.
# - Python has no command for declaring a variable; it happens automatically when assigning a value.
# - The "=" symbol is called the "assignment operator" (it assigns the value on the right to the variable name on the left).

# 1. Creating (Declaring) Variables
name = "Asghar"                 # Stores a text value (String)
age = 21                       # Stores a whole number (Integer)
is_coding = True               # Stores a true/false value (Boolean)

# 2. Accessing/Using Variables
# We can use the print() function to output the value stored inside a variable.
print(name)                    # Outputs: Asghar
print(age)                     # Outputs: 21
print(is_coding)               # Outputs: True

# 3. Reassigning (Overwriting) Variables
# The value inside a variable container can change during the program execution.
fav_hobby = "Watching Anime"
print(fav_hobby)               # Outputs: Watching Anime

fav_hobby = "Coding Python"    # Overwrites the previous value
print(fav_hobby)               # Outputs: Coding Python

# 4. Dynamic Typing (Python Specific)
# In Python, a variable can change its data type at any time.
score = 100                    # Currently holds an Integer (number)
print(score)

score = "One Hundred"          # Successfully changed to hold a String (text)
print(score)
