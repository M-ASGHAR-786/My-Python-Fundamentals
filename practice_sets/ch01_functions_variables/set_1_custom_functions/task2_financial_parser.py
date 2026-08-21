"""
TASK 2: Financial String Sanitizer & Tax Engine

Scenario:
In backend financial pipelines, raw API payloads deliver currency and percentage data 
as unparsed formatted strings (e.g., "$1,250.80" and "15%"). You must write modular 
helper functions to sanitize, parse, and calculate the total bill without crashing.

Goals:
1. Define a function parse_currency(currency_str: str) -> float:
   - Strips whitespace, removes '$' and ',', and returns a clean float.
2. Define a function parse_percentage(percent_str: str) -> float:
   - Strips whitespace, removes '%', divides by 100, and returns the decimal rate.
3. Define a function calculate_total_with_tax(base_amount: float, tax_rate: float = 0.05) -> float:
   - Calculates base_amount + (base_amount * tax_rate), rounded to 2 decimal places.
   - If tax_rate is omitted, defaults to 0.05 (5%).
4. In main():
   - Parse raw_price = " $2,450.75 " and raw_tax = " 8.5% ".
   - Calculate the total bill with tax.
   - Print a formatted receipt with base price, tax percentage, and total.
5. Call main().
"""

# --- Solution ---

def parse_currency(currency_str: str) -> float:
    cleaned: str = currency_str.strip().replace("$", "").replace(",", "")
    return float(cleaned)


def parse_percentage(percent_str: str) -> float:
    cleaned: str = percent_str.strip().replace("%", "").replace(",", "")
    return float(cleaned) / 100.0


def calculate_total_with_tax(base_amount: float, tax_rate: float = 0.05) -> float:
    total_amount: float = base_amount + (base_amount * tax_rate)
    return round(total_amount, 2)


def main() -> None:
    raw_price: float = parse_currency(" $2,450.75 ")
    raw_tax: float = parse_percentage(" 8.5% ")
    total_bill: float = calculate_total_with_tax(raw_price, raw_tax)

    print(f"""\
Dear Sir! Your Base price: ${raw_price:,.2f}
--------- Your Tax in   %: {raw_tax:.2%}
--------- Total bill     : ${total_bill:,.2f}""")


main()

"""
Expected Output:
Dear Sir! Your Base price: $2,450.75
--------- Your Tax in   %: 8.50%
--------- Total bill     : $2,659.06
"""