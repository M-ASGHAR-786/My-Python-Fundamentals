"""
Task 2: Algorithmic Logic Drill — High-Precision Calendar Engine
Directory: practice_sets/ch02_conditionals/set_1_decision_logic/
File: task2_calendar_engine.py

Scenario:
Build a zero-import settlement calendar engine to validate dates, determine 
leap years, and extract days-in-month across historical and future years 
using pure conditional and modulo logic.

Constraints:
Strictly zero imports (no datetime or calendar modules).

Requirements:
1. is_leap_year(year: int) -> bool:
   - Leap if divisible by 4, except centuries unless divisible by 400.
   - Return direct boolean expression.
2. get_days_in_month(month: int, year: int) -> int:
   - Returns -1 if month/year invalid.
   - Months 1, 3, 5, 7, 8, 10, 12 -> 31 days.
   - Months 4, 6, 9, 11 -> 30 days.
   - Month 2 -> 29 if leap year, else 28.
   - Uses match-case with pipe '|'.
3. validate_date(day: int, month: int, year: int) -> str:
   - Validates year > 0, 1 <= month <= 12, 1 <= day <= days_in_month.
4. main() -> None:
   - Prompts for Year, Month, Day.
   - Prints full diagnostic report if valid, or exact error string if invalid.
"""


def is_leap_year(year: int) -> bool:
    """Evaluates Gregorian leap year rules using modulo arithmetic."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_days_in_month(month: int, year: int) -> int:
    """Returns number of days in a given month accounting for leap years."""
    if year <= 0 or month < 1 or month > 12:
        return -1

    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 29 if is_leap_year(year) else 28
        case _:
            return -1


def validate_date(day: int, month: int, year: int) -> str:
    """Validates calendar date boundaries."""
    if year <= 0:
        return "INVALID: Year must be greater than 0"
    if month < 1 or month > 12:
        return "INVALID: Month must be between 1 and 12"

    max_days: int = get_days_in_month(month, year)
    if day < 1 or day > max_days:
        return "INVALID: Day exceeds valid range for month"

    return "VALID: Date confirmed"


def main() -> None:
    year: int = int(input("Enter Year: "))
    month: int = int(input("Enter Month: "))
    day: int = int(input("Enter Day: "))

    validation_result: str = validate_date(day, month, year)

    print("-" * 50)
    print(f"Validation Status : {validation_result}")

    if validation_result == "VALID: Date confirmed":
        print(f"Leap Year         : {is_leap_year(year)}")
        print(f"Days in Month     : {get_days_in_month(month, year)}")
    print("-" * 50)


if __name__ == "__main__":
    main()

"""
EXPECTED TERMINAL OUTPUT:

Test Case 1 (Valid Leap Day):
Enter Year: 2024
Enter Month: 2
Enter Day: 29
--------------------------------------------------
Validation Status : VALID: Date confirmed
Leap Year         : True
Days in Month     : 29
--------------------------------------------------

Test Case 2 (Invalid Century Leap Day):
Enter Year: 1900
Enter Month: 2
Enter Day: 29
--------------------------------------------------
Validation Status : INVALID: Day exceeds valid range for month
--------------------------------------------------

Test Case 3 (Valid 400-Year Century):
Enter Year: 2000
Enter Month: 2
Enter Day: 29
--------------------------------------------------
Validation Status : VALID: Date confirmed
Leap Year         : True
Days in Month     : 29
--------------------------------------------------
"""