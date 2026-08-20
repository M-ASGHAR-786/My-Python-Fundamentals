"""
TASK 2: Storage Growth & Exponentiation

Scenario:
A cloud database starts with 250 GB of data and grows by 12% per year (1.12 multiplier).
The mathematical formula for growth over time is:
    Final Storage = Initial Storage * (growth_multiplier ** years)

Goals:
1. Create variables: initial_storage = 250, growth_multiplier = 1.12, and years = 4.
2. Calculate the projected storage after 4 years using the power operator (**) and store it in final_storage.
3. Use the round() function to round final_storage to 2 decimal places and print the result using an f-string.
4. Answer this question in a comment: Is the final output an int or a float, and why?
"""

# --- Solution ---
initial_storage = 250
growth_multiplier = 1.12
years = 4

# Calculate growth using exponentiation (**)
final_storage = initial_storage * (growth_multiplier ** years)
rounded_storage = round(final_storage, 2)

# Display result
print(f"The Projected Storage after 4 years: {rounded_storage} GB")

# Explanation:
# The result is a float because growth_multiplier (1.12) is a float.
# In Python, any arithmetic operation involving a float automatically promotes
# the result to a float to preserve decimal precision.

"""
Expected Output:
The Projected Storage after 4 years: 393.38 GB
"""
