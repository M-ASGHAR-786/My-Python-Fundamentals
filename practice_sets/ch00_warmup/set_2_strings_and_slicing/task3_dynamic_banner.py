"""
TASK 3: Dynamic Terminal Banner & Immutability Trap

Scenario:
You are building an automated alerting system for training AI models. When a model crashes, 
the server must format a dynamic error box in the logs, and you must verify string immutability.

Given Data:
model_name = "LLAMA-3-8B"
status_code = "ERR_GPU_OOM_503"

Goals:
1. Construct a message line using an f-string.
2. Dynamically generate a border of '-' matching len(message).
3. Print the formatted alert box.
4. Demonstrate how to bypass string immutability using slicing.
"""

# --- Solution ---
model_name = "LLAMA-3-8B"
status_code = "ERR_GPU_OOM_503"

message = f"| CRITICAL ALERT: {model_name} -> {status_code} |"
border = len(message) * "-"

# Method A (Your Single-Line Approach):
print(f"{border}\n{message}\n{border}")

# Method B (The Multi-Line Triple Quote Approach with leading '\\' to strip first newline):
alert_box = f"""\
{border}
{message}
{border}"""

# Immutability Demonstration:
# Trying `model_name[0] = 'M'` throws TypeError: 'str' object does not support item assignment.
# Strings are immutable; you must slice and create a new string:
updated_model_name = "M" + model_name[1:]
print(f"Updated Model Name: {updated_model_name}")

"""
Expected Output:
-------------------------------------------------
| CRITICAL ALERT: LLAMA-3-8B -> ERR_GPU_OOM_503 |
-------------------------------------------------
Updated Model Name: MLAMA-3-8B
"""
