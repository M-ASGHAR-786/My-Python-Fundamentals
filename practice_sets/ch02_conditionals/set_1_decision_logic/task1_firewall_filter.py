"""
Task 1: Syntax & Method Drill — The Network Firewall Filter
Directory: practice_sets/ch02_conditionals/set_1_decision_logic/
File: task1_firewall_filter.py

Scenario:
Build an edge-routing firewall rule engine that inspects incoming network traffic 
packets and decides whether to ALLOW, THROTTLE, or DROP the connection based on 
port numbers, protocol types, and packet sizes.

Requirements:
1. Define is_trusted_port(port: int) -> bool returning True for ports 80, 443, 8080.
2. Define evaluate_packet(protocol: str, port: int, payload_size_kb: int) -> str:
   - "DROP: Invalid Payload Size" if payload <= 0 or > 10240.
   - "ALLOW: Secure Web Traffic" if trusted port and protocol == "HTTPS".
   - "ALLOW: Standard Web Traffic" if trusted port and protocol == "HTTP".
   - "THROTTLE: Non-Standard Web Traffic" if trusted port and protocol not in ("HTTP", "HTTPS").
   - "DROP: Blocked Port" for all other ports.
3. Define parse_firewall_action(decision: str) -> str using match-case on the decision prefix:
   - "ALLOW" -> "Status 200: Traffic Forwarded to Gateway"
   - "THROTTLE" -> "Status 429: Bandwidth Rate-Limited"
   - "DROP" -> "Status 403: Packet Discarded at Firewall"
   - _ -> "Status 500: Internal Rule Error"
4. Implement main() prompting user input, executing evaluation, and displaying formatted output.
"""


def is_trusted_port(port: int) -> bool:
    """Checks if incoming port belongs to standard web routing ports."""
    return port in (80, 443, 8080)


def evaluate_packet(protocol: str, port: int, payload_size_kb: int) -> str:
    """Evaluates packet attributes and returns a categorized routing decision."""
    if payload_size_kb <= 0 or payload_size_kb > 10240:
        return "DROP: Invalid Payload Size"
    elif is_trusted_port(port) and protocol == "HTTPS":
        return "ALLOW: Secure Web Traffic"
    elif is_trusted_port(port) and protocol == "HTTP":
        return "ALLOW: Standard Web Traffic"
    elif is_trusted_port(port) and protocol not in ("HTTP", "HTTPS"):
        return "THROTTLE: Non-Standard Web Traffic"
    else:
        return "DROP: Blocked Port"


def parse_firewall_action(action_key: str) -> str:
    """Maps decision status keys to standard HTTP gateway responses."""
    match action_key:
        case "ALLOW":
            return "Status 200: Traffic Forwarded to Gateway"
        case "THROTTLE":
            return "Status 429: Bandwidth Rate-Limited"
        case "DROP":
            return "Status 403: Packet Discarded at Firewall"
        case _:
            return "Status 500: Internal Rule Error"


def main() -> None:
    protocol: str = input("Enter Protocol: ").strip().upper()
    port: int = int(input("Enter Port: "))
    payload_size_kb: int = int(input("Enter Payload Size in kb: "))

    decision: str = evaluate_packet(protocol, port, payload_size_kb)
    action_key: str = decision.split(":")[0]
    status_message: str = parse_firewall_action(action_key)

    print("-" * 50)
    print(f"Decision : {decision}")
    print(f"Response : {status_message}")
    print("-" * 50)


if __name__ == "__main__":
    main()

"""
EXPECTED TERMINAL OUTPUT:

Test Case 1 (Valid HTTPS):
Enter Protocol: https
Enter Port: 443
Enter Payload Size in kb: 512
--------------------------------------------------
Decision : ALLOW: Secure Web Traffic
Response : Status 200: Traffic Forwarded to Gateway
--------------------------------------------------

Test Case 2 (Untrusted Port):
Enter Protocol: http
Enter Port: 22
Enter Payload Size in kb: 120
--------------------------------------------------
Decision : DROP: Blocked Port
Response : Status 403: Packet Discarded at Firewall
--------------------------------------------------

Test Case 3 (Throttled Protocol on Web Port):
Enter Protocol: websocket
Enter Port: 8080
Enter Payload Size in kb: 64
--------------------------------------------------
Decision : THROTTLE: Non-Standard Web Traffic
Response : Status 429: Bandwidth Rate-Limited
--------------------------------------------------
"""