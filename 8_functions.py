# ---------------- Understanding Functions & Return Values ---------------- #

# What is a Function?
# - Think of a function like a specialized kitchen appliance (e.g., a toaster or blender).
# - You pass ingredients into it (Parameters/Arguments).
# - It executes a specific, reusable set of instructions.
# - It hands you back the finished product (Return Value).
#
# Crucial Rule (print vs. return):
# - print(): Only displays text on the screen for humans to see. It returns None in memory.
# - return: Hands the actual computed data back to your program so another variable or 
#   function can continue doing calculations with it.

# 1. Defining a Basic Function with Parameters & Type Hints
def greet_user(name: str) -> None:
    """Prints a greeting to the terminal."""
    print(f"Hello, {name}!")

greet_user("Asghar")

print("-" * 50)  # Visual separator

# 2. Functions with Default Parameters (Fallback Values)
# If the caller does not supply an argument, the default 'to="world"' is used.
def hello(to: str = "world") -> None:
    print(f"Hello, {to}!")

hello("David")     # Overrides the default -> Outputs: Hello, David!
hello()            # Uses the default      -> Outputs: Hello, world!

print("-" * 50)

# 3. Returning Values vs. Printing (The Output Trap)
# Function A: Only prints (Returns None)
def add_print(x: int, y: int) -> None:
    print(x + y)

# Function B: Returns the actual calculated value
def add_return(x: int, y: int) -> int:
    return x + y

# Capturing results in memory:
result_a = add_print(5, 10)     # Prints 15, but stores None in 'result_a'
result_b = add_return(5, 10)    # Silently stores the integer 15 in 'result_b'

print(f"Stored in result_a (print):  {result_a}")  # Outputs: None
print(f"Stored in result_b (return): {result_b}")  # Outputs: 15

# Common Beginner Mistake:
# # total = result_a + 5   # Invalid: TypeError! Cannot add int to NoneType (uncomment to test)
total = result_b + 5       # Valid: 15 + 5 = 20
print(f"Valid calculation with returned value: {total}")

print("-" * 50)

# 4. Standard Python Main Function Pattern (Entry Point)
# In professional code, we organize logic inside functions and trigger execution via main().
def square(number: float) -> float:
    """Calculates and returns the square of a number."""
    return number ** 2

def main() -> None:
    user_num: float = 4.0
    calc_result: float = square(user_num)
    print(f"The square of {user_num} is: {calc_result}")

# Triggering the program:
main()

# ---------------- Understanding Functions & Return Values ---------------- #