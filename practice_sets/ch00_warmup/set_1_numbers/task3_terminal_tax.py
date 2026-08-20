"""
TASK 3: Terminal Magic & Float Traps

Scenario:
A customer orders items from an online tech store:
- 3 items at $24.50 each
- 2 items at $9.75 each
- Tax rate: 8.5% (0.085)
- Shipping: $12.00 flat

Goals:
1. Calculate the subtotal and store it in 'sub_total'.
2. Calculate the tax amount.
3. Calculate the total bill including shipping and subtotal.
4. Display the rounded total bill using an f-string.
5. Explain the float promotion rule for floor division (//).
"""

# --- Solution ---
sub_total = (24.50 * 3) + (9.75 * 2)

# Tax calculation (7.905)
tax = sub_total * 0.085

# Total calculation ($112.905)
total_bill = sub_total + tax + 12.00

# Display rounded result
print(f"Your Total Bill: {round(total_bill, 2)}")

# Rule Clarification:
# Performing `total_bill // 1` results in `112.0` (a float).
# In Python, if ANY operand in an arithmetic operation is a float,
# the result is ALWAYS guaranteed to be a float.

"""
Expected Output:
Your Total Bill: 112.91
"""
