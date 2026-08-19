"""
TASK 1: The Server Rack Math

Scenario:
You are setting up servers for a data center.
- You have a total of 147 servers.
- Each server rack can hold exactly 8 servers.

Goals:
1. Create variables: total_servers = 147 and rack_capacity = 8.
2. Use floor division (//) to calculate how many full racks you have.
3. Use the modulo operator (%) to calculate how many leftover servers remain in the last, partially filled rack.
4. Print both results clearly using f-strings.
"""

# --- Solution ---
total_servers = 147
rack_capacity = 8

# Calculate full racks (floored quotient) and remaining servers (remainder)
total_full_racks = total_servers // rack_capacity
remaining_servers = total_servers % rack_capacity

# Display results
print(f"Total Racks Holding 8 Servers Each: {total_full_racks}")
print(f"Leftover Servers in the Last Rack: {remaining_servers}")

"""
Expected Output:
Total Racks Holding 8 Servers Each: 18
Leftover Servers in the Last Rack: 3
"""
