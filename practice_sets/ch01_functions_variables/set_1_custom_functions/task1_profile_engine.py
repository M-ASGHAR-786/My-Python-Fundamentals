"""
TASK 1: User Profile Normalizer & Unit Cost Engine

Scenario:
You are building an onboarding helper for an application. Users provide unformatted 
input (extra whitespace, inconsistent casing), and you need modular, reusable functions 
to sanitize user data and calculate per-unit costs.

Goals:
1. Define a function named format_name(full_name: str = "anonymous user") -> str:
   - It must strip all leading and trailing whitespace.
   - It must convert the name to Title Case (e.g., "  aLi kHaN  " -> "Ali Khan").
   - It must return the cleaned string (do NOT use print() inside the function).
2. Define a function named calculate_unit_price(total_cost: float, quantity: int = 1) -> float:
   - It must calculate the price per single item (total_cost / quantity).
   - It must return the calculated value rounded to 2 decimal places.
   - If quantity is not passed by the caller, it must default to 1.
3. Create a main() function that:
   - Normalizes the name "   dAvId mALaN   " using format_name.
   - Calculates the unit cost for a total cost of $1450.75 with quantity = 5 using calculate_unit_price.
   - Prints the final receipt using an F-string formatted with thousands separators and 2 decimal places (e.g., {unit_price:,.2f}).
4. Call main() to execute your program.
"""

# --- Solution ---

# Function for normalizing and capitalizing each word of name
def format_name(full_name: str = "anonymous user") -> str:
    cleaned_name: str = full_name.strip().title()
    return cleaned_name


# Function for finding price of single item
def calculate_unit_price(total_cost: float, quantity: int = 1) -> float:
    price_per_item: float = total_cost / quantity
    return round(price_per_item, 2)


# Main function for orchestrating the program flow
def main() -> None:
    raw_name: str = "   dAvId mALaN   "
    customer_name: str = format_name(raw_name)
    
    total_cost: float = 1450.75
    quantity: int = 5
    
    unit_price: float = calculate_unit_price(total_cost, quantity)
    
    print(f"Dear {customer_name}! You purchased {quantity} items, each worth ${unit_price:,.2f}")


main()

"""
Expected Output:
Dear David Malan! You purchased 5 items, each worth $290.15
"""