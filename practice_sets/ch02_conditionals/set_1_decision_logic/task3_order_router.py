"""
Task 3: The Subsystem Prototype — Quantitative Order Routing & Risk Engine
Directory: practice_sets/ch02_conditionals/set_1_decision_logic/
File: task3_order_router.py

Scenario:
Build an algorithmic trade validation, fee calculation, risk assessment, 
and venue routing engine for a high-frequency trading desk.

Requirements:
1. calculate_fee(order_type: str, total_value: float) -> float:
   - Returns -1.0 if total_value <= 0.0 or invalid order type.
   - "LIMIT" -> 0.1% (0.001 * total_value)
   - "MARKET" -> 0.25% (0.0025 * total_value)
   - "STOP_LOSS" -> 0.15% (0.0015 * total_value)
2. assess_risk(account_tier: str, leverage: int, margin_ratio: float) -> str:
   - Tier in ("STANDARD", "PRO", "INSTITUTIONAL")
   - 1 <= leverage <= 100
   - margin_ratio < 0.10 -> "REJECTED: Critical Margin Level"
   - leverage > 50 and tier == "STANDARD" -> "REJECTED: Excessive Leverage For Standard Tier"
   - (leverage > 20 and margin < 0.25) or (leverage > 75 and margin < 0.50) -> "FLAGGED: High Risk Exposure"
   - Else -> "APPROVED: Normal Risk"
3. route_order(order_type: str, total_value: float, risk_status: str) -> str:
   - Handles REJECTED, FLAGGED, and APPROVED order routing based on value thresholds.
4. main() -> None:
   - Validates inputs, executes the risk/fee/routing pipeline, and displays a formatted trade slip.
"""


def calculate_fee(order_type: str, total_value: float) -> float:
    """Calculates brokerage fee percentage based on order classification."""
    if total_value <= 0.0:
        return -1.0

    match order_type.strip().upper():
        case "LIMIT":
            return 0.001 * total_value
        case "MARKET":
            return 0.0025 * total_value
        case "STOP_LOSS":
            return 0.0015 * total_value
        case _:
            return -1.0


def assess_risk(account_tier: str, leverage: int, margin_ratio: float) -> str:
    """Evaluates account exposure, tier permissions, and margin requirements."""
    tier_normalized: str = account_tier.strip().upper()

    if tier_normalized not in ("STANDARD", "PRO", "INSTITUTIONAL"):
        return "REJECTED: Unknown Account Tier"
    elif not (1 <= leverage <= 100):
        return "REJECTED: Invalid Leverage Range"
    elif margin_ratio < 0.10:
        return "REJECTED: Critical Margin Level"
    elif leverage > 50 and tier_normalized == "STANDARD":
        return "REJECTED: Excessive Leverage For Standard Tier"
    elif (leverage > 20 and margin_ratio < 0.25) or (
        leverage > 75 and margin_ratio < 0.50
    ):
        return "FLAGGED: High Risk Exposure"
    else:
        return "APPROVED: Normal Risk"


def route_order(order_type: str, total_value: float, risk_status: str) -> str:
    """Determines the appropriate exchange venue based on risk and order attributes."""
    order_normalized: str = order_type.strip().upper()

    if risk_status.startswith("REJECTED"):
        return "CANCELLED: Blocked by Risk Gate"
    elif risk_status == "FLAGGED: High Risk Exposure":
        return "ROUTED: Secondary Dark Pool (Manual Review Required)"
    elif risk_status == "APPROVED: Normal Risk":
        if (
            order_normalized in ("LIMIT", "STOP_LOSS")
            and total_value >= 100000.0
        ):
            return "ROUTED: Institutional ECN"
        elif (
            order_normalized in ("LIMIT", "STOP_LOSS")
            and total_value < 100000.0
        ):
            return "ROUTED: Primary Retail Exchange"
        elif order_normalized == "MARKET":
            return "ROUTED: Direct Market Maker AMM"
        else:
            return "CANCELLED: Unrecognized Order Specification"

    return "CANCELLED: Unresolved Risk State"


def main() -> None:
    account_tier: str = input("Enter Account Tier: ").strip().upper()
    order_type: str = input("Enter Order Type: ").strip().upper()
    quantity: int = int(input("Enter Quantity: "))
    unit_price: float = float(input("Enter Unit Price: "))
    leverage: int = int(input("Enter Leverage: "))
    margin_ratio: float = float(input("Enter Margin Ratio: "))

    if quantity <= 0 or unit_price <= 0.0:
        print("Invalid trade parameters.")
        return

    total_value: float = quantity * unit_price
    risk_status: str = assess_risk(account_tier, leverage, margin_ratio)
    fee: float = calculate_fee(order_type, total_value)
    routing_destination: str = route_order(order_type, total_value, risk_status)

    fee_display: str = (
        f"${fee:,.2f}"
        if (fee > 0 and not risk_status.startswith("REJECTED"))
        else "N/A"
    )

    print("-" * 50)
    print("ORDER EXECUTION TICKET")
    print("-" * 50)
    print(f"Total Order Value   : ${total_value:,.2f}")
    print(f"Risk Status         : {risk_status}")
    print(f"Routing Destination : {routing_destination}")
    print(f"Estimated Fee       : {fee_display}")
    print("-" * 50)


if __name__ == "__main__":
    main()

"""
EXPECTED TERMINAL OUTPUT:

Test Case 1 (Approved Institutional Limit Order):
Enter Account Tier: institutional
Enter Order Type: limit
Enter Quantity: 500
Enter Unit Price: 250.0
Enter Leverage: 10
Enter Margin Ratio: 0.40
--------------------------------------------------
ORDER EXECUTION TICKET
--------------------------------------------------
Total Order Value   : $125,000.00
Risk Status         : APPROVED: Normal Risk
Routing Destination : ROUTED: Institutional ECN
Estimated Fee       : $125.00
--------------------------------------------------

Test Case 2 (Rejected Standard Tier Excessive Leverage):
Enter Account Tier: standard
Enter Order Type: market
Enter Quantity: 100
Enter Unit Price: 50.0
Enter Leverage: 60
Enter Margin Ratio: 0.30
--------------------------------------------------
ORDER EXECUTION TICKET
--------------------------------------------------
Total Order Value   : $5,000.00
Risk Status         : REJECTED: Excessive Leverage For Standard Tier
Routing Destination : CANCELLED: Blocked by Risk Gate
Estimated Fee       : N/A
--------------------------------------------------
"""