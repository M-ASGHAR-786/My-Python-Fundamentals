"""
TASK 2: Server Path Sanitization & Escape Traps

Scenario:
You are building an AI data pipeline on Windows. You receive a local file path 
that contains characters that trigger escape sequences (\t for tab, \n for newline).

Given Data:
Local raw path: C:\temp\new_datasets\train_v1.csv

Goals:
1. Store path in 'raw_path' using raw string syntax (r"...").
2. Extract file extension (".csv") using negative slicing ([-4:]).
3. Extract file name with extension ("train_v1.csv") using negative slicing ([-12:]).
4. Construct a new cloud URL: "https://aws.s3.cloud/datasets/" + file_with_ext.
5. Explain the difference between out-of-range slicing and direct indexing.
"""

# --- Solution ---
raw_path = r"C:\temp\new_datasets\train_v1.csv"

file_ext = raw_path[-4:]
file_with_ext = raw_path[-12:]

cloud_url = "https://aws.s3.cloud/datasets/" + file_with_ext

print(f"File Extension: {file_ext}")
print(f"File Name: {file_with_ext}")
print(f"Cloud URL: {cloud_url}")

# Slice vs Index Comparison:
# 1. raw_path[0:150] safely returns the entire string without crashing.
# 2. raw_path[150] throws an IndexError because direct index access requires 
#    the exact element to exist in memory.

"""
Expected Output:
File Extension: .csv
File Name: train_v1.csv
Cloud URL: https://aws.s3.cloud/datasets/train_v1.csv
"""