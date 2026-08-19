"""
TASK 1: Security Token Extraction & Dynamic Masking

Scenario:
In a production backend, API authentication tokens must be partially masked 
in server logs to prevent security leaks.

Given Data:
token = "PROD_AUTH_9482710395"

Goals:
1. Create the variable token = "PROD_AUTH_9482710395".
2. Extract the environment prefix ("PROD_") using slice notation with an omitted start index ([:5]).
3. Extract the last 4 digits ("0395") using negative slicing ([-4:]).
4. Dynamically construct 'masked_token' keeping the prefix, the last 4 digits, and replacing everything in between with '*'.
5. Verify that len(token) == len(masked_token).
"""

# --- Solution ---
token = "PROD_AUTH_9482710395"

prefix = token[:5]
postfix = token[-4:]
masked_count = len(token[5:-4])

masked_token = prefix + (masked_count * "*") + postfix

print(f"Masked Token: {masked_token}")
print(f"Length Check Valid: {len(token) == len(masked_token)}")

"""
Expected Output:
Masked Token: PROD_***********0395
Length Check Valid: True
"""
