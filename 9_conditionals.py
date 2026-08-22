# ---------------- Understanding Conditionals ---------------- #

"""
CONCEPTUAL ANALOGY:
Think of conditionals as an Automated Railway Dispatch System. 
A train (the execution flow) moves along a track. At junction switches (conditional checks),
the system inspects signals (Boolean True/False expressions) to route the train down 
specific tracks (code blocks). 

- Multiple independent 'if' switches test every single junction even if the train already changed tracks.
- An 'if-elif-else' switchboard routes the train to the first valid branch and locks all other tracks, 
  saving massive computational energy.
"""

# ==============================================================================
# 1. Comparison Operators & Boolean Evaluations
# ==============================================================================
print("1. Comparison Operators & Boolean Evaluations")

# Standard comparison operators return raw bool values (True or False)
# >  : Greater than
# <  : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
# == : Equal to (comparison, NOT assignment)
# != : Not equal to

val_a: int = 15
val_b: int = 20

is_less: bool = val_a < val_b
is_equal: bool = val_a == val_b

print(f"Is {val_a} < {val_b}? -> {is_less}")
print(f"Is {val_a} == {val_b}? -> {is_equal}")

# Beginner Trap / Syntax Error:
# # if val_a = val_b: # Invalid: Single '=' is assignment operator, not comparison (SyntaxError).
# # if is_less == True: # Anti-pattern: Redundant comparison; boolean variables evaluate directly.

print("-" * 50)

# ==============================================================================
# 2. Control Flow: if, elif, and else
# ==============================================================================
print("2. Control Flow: if, elif, and else")

# An if-elif-else ladder evaluates top-to-bottom and halts on the first True condition.
temperature_celsius: int = 28

if temperature_celsius > 35:
    status: str = "Severe Heat Warning"
elif temperature_celsius >= 25:
    status: str = "Optimal Warm Temperature"
elif temperature_celsius >= 15:
    status: str = "Moderate Temperature"
else:
    status: str = "Cold Environment"

print(f"Temperature: {temperature_celsius}°C -> Status: {status}")

# Beginner Trap / Performance Pitfall:
# # if temperature_celsius > 35: print("Hot")
# # if temperature_celsius >= 25: print("Warm") # Bad: Uses multiple standalone 'if's, forcing CPU to evaluate all conditions needlessly.

print("-" * 50)

# ==============================================================================
# 3. Logical Operators (and, or) & Chained Comparisons
# ==============================================================================
print("3. Logical Operators & Chained Comparisons")

auth_token_present: bool = True
user_age: int = 22

# Using 'and' (both must be True) & 'or' (at least one must be True)
if auth_token_present and user_age >= 18:
    access_decision: str = "Access Granted"
else:
    access_decision: str = "Access Rejected"

print(f"Authorization: {access_decision}")

# Pythonic Chained Comparison (cleaner than: score >= 80 and score <= 90)
exam_score: int = 85
is_grade_b: bool = 80 <= exam_score < 90
print(f"Is exam score {exam_score} in range [80, 90)? -> {is_grade_b}")

# Beginner Trap:
# # if score >= 80 and <= 90: # Invalid: Left operand must be restated or written as chained (80 <= score <= 90).

print("-" * 50)

# ==============================================================================
# 4. Modulo Arithmetic & Pythonic Predicate Functions
# ==============================================================================
print("4. Modulo Arithmetic & Pythonic Predicates")


def is_even(number: int) -> bool:
    """Returns True if number is divisible by 2 with no remainder."""
    return number % 2 == 0


sample_number: int = 42
print(f"Number {sample_number} is even? -> {is_even(sample_number)}")

# Beginner Trap / Verbose Anti-Pattern:
# # def is_even(number: int) -> bool:
# #     if number % 2 == 0:
# #         return True
# #     else:
# #         return False  # Bad: Unnecessarily verbose. 'number % 2 == 0' already yields a bool.

print("-" * 50)

# ==============================================================================
# 5. Structural Pattern Matching (match-case) [Python 3.10+]
# ==============================================================================
print("5. Modern Structural Pattern Matching (match-case)")


def get_http_status_message(status_code: int) -> str:
    match status_code:
        case 200 | 201:
            return "Success: Resource Processed"
        case 400:
            return "Client Error: Bad Request"
        case 401 | 403:
            return "Security Error: Unauthorized / Forbidden"
        case 404:
            return "Client Error: Resource Not Found"
        case 500 | 502 | 503:
            return "Server Error: Backend Failure"
        case _:
            return "Unknown HTTP Status Code"


test_code: int = 403
print(f"HTTP {test_code} -> {get_http_status_message(test_code)}")

# Beginner Trap:
# # case 200 or 201: # Invalid in match-case: Pattern alternative syntax requires pipe '|', not 'or'.
# # match without 'case _': # Dangerous: Missing wildcard catch-all means unmatched values silently fall through.

print("-" * 50)


# ==============================================================================
# Execution Guard
# ==============================================================================
def main() -> None:
    print("Conditionals module executed successfully.")


if __name__ == "__main__":
    main()
