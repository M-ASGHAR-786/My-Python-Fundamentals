# ---------------- Arithmetic Operators ---------------- #


# Arithmetic operators perform mathematical calculations like 
# addition, subtraction, multiplication, and division.
# Operators: Addition(+), Subtraction(-), Multiplication(*), Division(/) etc
a = 10
b = 20.5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("(a * b) / b =", (a * b)/b)


# ---------------- Arithmetic Operators ---------------- #


# ---------------- Assignment Operators ---------------- #


# Assignment operators are used to store values in variables,
# or to update a variable's value.
# Operators: =, +=, -=, *=, /= etc
c = 15                      # |
d = 5                       # |---> Initializing Variables
e = 20                      # |
f = 200                     # |

c += 3                      # |
d -= 1                      # |---> Using Assignment Operators
e *= d                      # |
f /= d                      # |

print(f"""
        c = {c}
        d = {d}
        e = {e}
        f = {f}
      """)


# ---------------- Assignment Operators ---------------- #


# ---------------- Comparison Operators ---------------- #


# Comparison operators let you compare values and return Boolean value as
# or False based on the result.
# Operators: ==, <, >, <=, >=, != etc
print(f"{a<b},  because a = {a} and b = {b}")  # Boolean Output: True
print(f"{d>=b}, because b = {b} and d = {d}")  # Boolean Output: False
print(f"{d!=1}, because d = {d}")              # Boolean Output: True
print(f"{f==1}, because f = {f}")              # Boolean Output: False


# ---------------- Comparison Operators ---------------- #


# ------------------ Logical Operators ------------------ #


# Logical operators evaluate the combined outcome of 
# conditional statements in an expression.
# Operators: and, or, not etc
is_student = True
cs_degree = True
se_degree = False
use_git_github = True
have_internship = False
in_hostel = False

# In "and" operator both conditions must be "True" to get output as "True"
print(is_student and cs_degree)         # Boolean Output: True    
print(use_git_github and se_degree)     # Boolean Output: False  
print(se_degree and cs_degree)          # Boolean Output: False
print(se_degree and in_hostel)          # Boolean Output: False

# In "or" operator at least one condition must be "True" to get output as "True"
print(is_student or cs_degree)         # Boolean Output: True    
print(use_git_github or se_degree)     # Boolean Output: True  
print(se_degree or cs_degree)          # Boolean Output: True
print(se_degree or in_hostel)          # Boolean Output: False

# "not" operator gives the opposite output from the input and only single input is given in "not" operator
print(not is_student)                 # Boolean Output: False    
print(not use_git_github)             # Boolean Output: False  

# Although Python doesn't have "NAND" and "NOR" operators,
# line 93 shows how to do it by combining `not` with `or`.
# Similarly, line 94 shows NAND by combining `not` with `and`.
print(not (se_degree or cs_degree))   # Boolean Output: False
print(not (se_degree and in_hostel))  # Boolean Output: True


# ------------------ Logical Operators ------------------ #
