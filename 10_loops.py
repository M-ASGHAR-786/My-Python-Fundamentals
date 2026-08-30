"""
Challenge: Automated Inventory Restock & Audit Engine

Scenario & Business Problem:
You are developing a warehouse inventory audit system for an e-commerce fulfillment center. 
The system must process an in-memory catalog of warehouse inventory records (a list of dictionaries), 
identify items that have fallen below safe operating thresholds, compute required replenishment units, 
and generate a financial restock manifest.

Inventory Dataset:
Initialize your program with the following dataset of items:
- Item: "NVMe SSD 1TB", Category: "Storage", Current Stock: 14, Reorder Point: 25, Unit Cost: 85.0
- Item: "DDR4 RAM 16GB", Category: "Memory", Current Stock: 42, Reorder Point: 40, Unit Cost: 45.0
- Item: "Mechanical Keyboard", Category: "Peripherals", Current Stock: 8, Reorder Point: 20, Unit Cost: 70.0
- Item: "USB-C Hub Multiport", Category: "Accessories", Current Stock: 0, Reorder Point: 15, Unit Cost: 30.0
- Item: "4K Monitor 27in", Category: "Displays", Current Stock: 12, Reorder Point: 10, Unit Cost: 280.0

Requirements & System Logic:

1. Input Validation:
- Interactively prompt the user for an audit budget cap (float).
- Use an indefinite loop to continuously re-prompt the user if they enter a number less than or equal to 0. 
  The loop only terminates once a strictly positive budget is provided.

2. Inventory Processing:
- Iterate through the inventory records.
- For each item, determine if the item is depleted (Current Stock < Reorder Point).
- For depleted items:
  - Calculate Deficit Units: (Reorder Point - Current Stock).
  - Calculate Restock Cost: (Deficit Units * Unit Cost).
- Skip all items that meet or exceed their reorder point.

3. Budget & Manifest Evaluation:
- Accumulate the total procurement cost for all depleted items.
- If total procurement cost exceeds the user's audit budget cap:
  - Mark budget status as "DEFICIT: Procurement exceeds budget cap".
- Otherwise:
  - Mark budget status as "APPROVED: Procurement within budget cap".

4. Output Display:
- Print a formatted Restock Manifest showing:
  - Each restocked item name, its deficit units, and its subtotal restock cost.
- Print a summary section showing:
  - Total restocked items count.
  - Total procurement cost (formatted to 2 decimal places with currency symbol).
  - Budget Status.
"""

data_set: list[dict] = [
    {
        "Item": "NVMe SSD 1TB",
        "Category": "Storage",
        "Current Stock": 14,
        "Reorder Point": 25,
        "Unit Cost": 85.0,
    },
    {
        "Item": "DDR4 RAM 16GB",
        "Category": "Memory",
        "Current Stock": 42,
        "Reorder Point": 40,
        "Unit Cost": 45.0,
    },
    {
        "Item": "Mechanical Keyboard",
        "Category": "Peripherals",
        "Current Stock": 8,
        "Reorder Point": 20,
        "Unit Cost": 70.0,
    },
    {
        "Item": "USB-C Hub Multiport",
        "Category": "Accessories",
        "Current Stock": 0,
        "Reorder Point": 15,
        "Unit Cost": 30.0,
    },
    {
        "Item": "4K Monitor 27in",
        "Category": "Displays",
        "Current Stock": 12,
        "Reorder Point": 10,
        "Unit Cost": 280.0,
    },
]


def input_validation() -> float:
    budget_cap: float = float(input("Enter total budget: "))
    while budget_cap <= 0:
        budget_cap = float(input("Enter valid total budget: "))
    return budget_cap


def item_data(item: dict) -> dict:
    sub_total: float = 0.0
    if item["Current Stock"] < item["Reorder Point"]:
        reorder_point: int = item["Reorder Point"]
        current_stock: int = item["Current Stock"]
        price: float = item["Unit Cost"]
        deficit_items: int = reorder_point - current_stock
        unit_cost: float = deficit_items * price
        sub_total = sub_total + unit_cost
        item_list: dict = {
            "Name": item["Item"],
            "Deficit Units": deficit_items,
            "Sub Total": sub_total,
        }
        return item_list
    return {}


def inventory_analysis() -> float:
    total: float = 0.0
    for item in data_set:
        if item["Current Stock"] >= item["Reorder Point"]:
            continue
        item_list: dict = item_data(item)
        total = total + item_list["Sub Total"]
    return total


def budget_status(current_budget: float, required_budget: float) -> str:
    if current_budget < required_budget:
        return "DEFICIT: Procurement exceeds budget cap"
    else:
        return "APPROVED: Procurement within budget cap"


def main() -> None:
    budget: float = input_validation()
    restock_cost: float = inventory_analysis()
    budget_state: str = budget_status(budget, restock_cost)
    total_deficit_units: int = 0

    for restock_detail in data_set:
        if restock_detail["Current Stock"] >= restock_detail["Reorder Point"]:
            continue
        item_list: dict = item_data(restock_detail)
        total_deficit_units = total_deficit_units + item_list["Deficit Units"]
        print(f"Item: {item_list['Name']}")
        print(f"Deficit Units: {item_list['Deficit Units']}")
        print(f"Sub Total: ${item_list['Sub Total']:,.2f}")
        print("-" * 50)

    print("=" * 80)
    print(f"Total Deficit Items: {total_deficit_units}")
    print(f"Total Cost: ${restock_cost:,.2f}")
    print(f"Budget Status: {budget_state}")
    print("=" * 80)


if __name__ == "__main__":
    main()

"""
EXPECTED TERMINAL OUTPUT:

Enter total budget: 3000
Item: NVMe SSD 1TB
Deficit Units: 11
Sub Total: $935.00
--------------------------------------------------
Item: Mechanical Keyboard
Deficit Units: 12
Sub Total: $840.00
--------------------------------------------------
Item: USB-C Hub Multiport
Deficit Units: 15
Sub Total: $450.00
--------------------------------------------------
================================================================================
Total Deficit Items: 38
Total Cost: $2,225.00
Budget Status: APPROVED: Procurement within budget cap
================================================================================
"""
