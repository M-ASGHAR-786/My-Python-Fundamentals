"""
Task 3: The Subsystem Prototype — Distributed API Gateway Traffic Governor & Token-Bucket Rate Limiter
Directory: practice_sets/ch03_loops/set_1_iteration_engines/
File: task3_traffic_governor.py

Scenario & Business Problem:
An API Gateway Traffic Governor for a microservice cluster. The gateway intercepts 
incoming HTTP requests, validates client credentials, mutates per-client token bucket 
quotas in real-time, calculates payload latency penalties, monitors for emergency kill-switch 
endpoints, and aggregates cluster telemetry reconciliation metrics.

Raw Input Data:
1. Client Registry Database:
   - "CLI-901": Tier "ENTERPRISE", Token Quota: 5, Base Penalty: 10ms
   - "CLI-302": Tier "PRO", Token Quota: 3, Base Penalty: 25ms
   - "CLI-105": Tier "FREE", Token Quota: 1, Base Penalty: 100ms
2. Incoming Request Stream (9 transaction requests).

Business Rules & System Logic:
1. Surcharge Input: Indefinite validation loop requiring positive multiplier (> 0.0).
2. Stream Processing:
   - 401_UNAUTHORIZED: Client missing from registry OR Authenticated is False (0.0ms latency, no quota change).
   - 429_RATE_LIMITED: Authenticated client with 0 tokens (0.0ms latency, request rejected).
   - 200_OK: Token deducted (-1). Latency = Base Penalty + ((Payload - 10) * Multiplier if Payload > 10 else 0).
   - Emergency Shutdown: If 200_OK targets "/api/v1/emergency_shutdown", record transaction and break loop immediately.
3. Telemetry Reconciliation:
   - Track requests evaluated, status breakdown (200, 429, 401), cumulative latency, final client quotas, and exit state.
"""

CLIENT_REGISTRY: dict[str, dict[str, str | int]] = {
    "CLI-901": {"Tier": "ENTERPRISE", "Token Quota": 5, "Base Penalty Ms": 10},
    "CLI-302": {"Tier": "PRO", "Token Quota": 3, "Base Penalty Ms": 25},
    "CLI-105": {"Tier": "FREE", "Token Quota": 1, "Base Penalty Ms": 100},
}

REQUESTS: list[dict[str, str | int | bool]] = [
    {"Client": "CLI-901", "Endpoint": "/api/v1/auth", "Payload KB": 4, "Authenticated": True},
    {"Client": "CLI-302", "Endpoint": "/api/v1/payments", "Payload KB": 12, "Authenticated": True},
    {"Client": "CLI-999", "Endpoint": "/api/v1/data", "Payload KB": 2, "Authenticated": False},
    {"Client": "CLI-302", "Endpoint": "/api/v1/export", "Payload KB": 35, "Authenticated": True},
    {"Client": "CLI-105", "Endpoint": "/api/v1/query", "Payload KB": 1, "Authenticated": True},
    {"Client": "CLI-302", "Endpoint": "/api/v1/payments", "Payload KB": 8, "Authenticated": True},
    {"Client": "CLI-105", "Endpoint": "/api/v1/query", "Payload KB": 2, "Authenticated": True},
    {"Client": "CLI-901", "Endpoint": "/api/v1/emergency_shutdown", "Payload KB": 1, "Authenticated": True},
    {"Client": "CLI-302", "Endpoint": "/api/v1/analytics", "Payload KB": 15, "Authenticated": True},
]


def get_surcharge_multiplier() -> float:
    """Prompts for a positive surcharge multiplier using indefinite validation."""
    while True:
        multiplier: float = float(input("Enter Over-Payload Surcharge Multiplier: "))
        if multiplier > 0.0:
            return multiplier
        print("Multiplier must be a positive number greater than 0.0.")


def process_traffic_stream(
    registry: dict[str, dict[str, str | int]],
    queue: list[dict[str, str | int | bool]],
    multiplier: float,
) -> tuple[list[dict[str, str | int | float]], dict[str, str | int | float]]:
    """
    Ingests transaction requests in a single pass, mutates token state, 
    and returns the transaction ledger along with aggregated telemetry summary.
    """
    ledger: list[dict[str, str | int | float]] = []
    total_evaluated: int = 0
    count_200: int = 0
    count_429: int = 0
    count_401: int = 0
    cumulative_latency: float = 0.0
    exit_state: str = "COMPLETED: Full Request Queue Drained"

    for req in queue:
        total_evaluated += 1
        client_id: str = str(req["Client"])
        endpoint: str = str(req["Endpoint"])
        payload_kb: int = int(req["Payload KB"])
        is_authenticated: bool = bool(req["Authenticated"])

        # 1. Authentication & Registry Verification
        if client_id not in registry or not is_authenticated:
            status: str = "401_UNAUTHORIZED"
            latency: float = 0.0
            count_401 += 1
            remaining_tokens: int = (
                int(registry[client_id]["Token Quota"]) if client_id in registry else 0
            )

        # 2. Token Bucket Quota Enforcement
        elif int(registry[client_id]["Token Quota"]) == 0:
            status = "429_RATE_LIMITED"
            latency = 0.0
            count_429 += 1
            remaining_tokens = 0

        # 3. Approved Execution & State Mutation
        else:
            status = "200_OK"
            count_200 += 1
            
            # Mutate state in registry
            registry[client_id]["Token Quota"] = int(registry[client_id]["Token Quota"]) - 1
            remaining_tokens = int(registry[client_id]["Token Quota"])

            # Compute latency
            base_penalty: int = int(registry[client_id]["Base Penalty Ms"])
            excess_kb: int = max(0, payload_kb - 10)
            latency = base_penalty + (excess_kb * multiplier)
            cumulative_latency += latency

        # 4. Record Transaction in Ledger
        ledger.append({
            "Client": client_id,
            "Endpoint": endpoint,
            "Status": status,
            "Latency": latency,
            "Tokens Remaining": remaining_tokens,
        })

        # 5. Circuit Breaker Emergency Kill Switch
        if status == "200_OK" and endpoint == "/api/v1/emergency_shutdown":
            exit_state = "HALTED: Emergency Circuit Breaker Activated"
            break

    summary: dict[str, str | int | float] = {
        "Exit State": exit_state,
        "Total Evaluated": total_evaluated,
        "Count 200": count_200,
        "Count 429": count_429,
        "Count 401": count_401,
        "Cumulative Latency": cumulative_latency,
    }

    return ledger, summary


def main() -> None:
    surcharge_multiplier: float = get_surcharge_multiplier()
    ledger, summary = process_traffic_stream(
        CLIENT_REGISTRY, REQUESTS, surcharge_multiplier
    )

    print("\n" + "=" * 95)
    print("API GATEWAY TRANSACTION LEDGER")
    print("=" * 95)

    for idx, tx in enumerate(ledger, start=1):
        print(
            f"TX #{idx:<2} | Client: {tx['Client']:<8} | "
            f"Status: {tx['Status']:<16} | "
            f"Latency: {float(tx['Latency']):>6.1f}ms | "
            f"Tokens Left: {tx['Tokens Remaining']:<2} | "
            f"Endpoint: {tx['Endpoint']}"
        )
        print("-" * 95)

    print("\n" + "=" * 95)
    print("GATEWAY RECONCILIATION SUMMARY")
    print("=" * 95)
    print(f"Gateway Exit State          : {summary['Exit State']}")
    print(f"Total Requests Evaluated    : {summary['Total Evaluated']}")
    print(f"Successful Transactions     : {summary['Count 200']} (200_OK)")
    print(f"Rate Limited Transactions   : {summary['Count 429']} (429_RATE_LIMITED)")
    print(f"Unauthorized Transactions   : {summary['Count 401']} (401_UNAUTHORIZED)")
    print(f"Cumulative Gateway Latency  : {float(summary['Cumulative Latency']):,.1f}ms")
    print("-" * 95)
    print("FINAL CLIENT TOKEN QUOTAS:")
    for client_id, meta in CLIENT_REGISTRY.items():
        print(f"  • {client_id} ({meta['Tier']}) : {meta['Token Quota']} tokens remaining")
    print("=" * 95)


if __name__ == "__main__":
    main()

"""
EXPECTED TERMINAL OUTPUT:

Enter Over-Payload Surcharge Multiplier: 1.5

===============================================================================================
API GATEWAY TRANSACTION LEDGER
===============================================================================================
TX #1  | Client: CLI-901  | Status: 200_OK           | Latency:   10.0ms | Tokens Left: 4  | Endpoint: /api/v1/auth
-----------------------------------------------------------------------------------------------
TX #2  | Client: CLI-302  | Status: 200_OK           | Latency:   28.0ms | Tokens Left: 2  | Endpoint: /api/v1/payments
-----------------------------------------------------------------------------------------------
TX #3  | Client: CLI-999  | Status: 401_UNAUTHORIZED | Latency:    0.0ms | Tokens Left: 0  | Endpoint: /api/v1/data
-----------------------------------------------------------------------------------------------
TX #4  | Client: CLI-302  | Status: 200_OK           | Latency:   62.5ms | Tokens Left: 1  | Endpoint: /api/v1/export
-----------------------------------------------------------------------------------------------
TX #5  | Client: CLI-105  | Status: 200_OK           | Latency:  100.0ms | Tokens Left: 0  | Endpoint: /api/v1/query
-----------------------------------------------------------------------------------------------
TX #6  | Client: CLI-302  | Status: 200_OK           | Latency:   25.0ms | Tokens Left: 0  | Endpoint: /api/v1/payments
-----------------------------------------------------------------------------------------------
TX #7  | Client: CLI-105  | Status: 429_RATE_LIMITED | Latency:    0.0ms | Tokens Left: 0  | Endpoint: /api/v1/query
-----------------------------------------------------------------------------------------------
TX #8  | Client: CLI-901  | Status: 200_OK           | Latency:   10.0ms | Tokens Left: 3  | Endpoint: /api/v1/emergency_shutdown
-----------------------------------------------------------------------------------------------

===============================================================================================
GATEWAY RECONCILIATION SUMMARY
===============================================================================================
Gateway Exit State          : HALTED: Emergency Circuit Breaker Activated
Total Requests Evaluated    : 8
Successful Transactions     : 6 (200_OK)
Rate Limited Transactions   : 1 (429_RATE_LIMITED)
Unauthorized Transactions   : 1 (401_UNAUTHORIZED)
Cumulative Gateway Latency  : 235.5ms
-----------------------------------------------------------------------------------------------
FINAL CLIENT TOKEN QUOTAS:
  • CLI-901 (ENTERPRISE) : 3 tokens remaining
  • CLI-302 (PRO) : 0 tokens remaining
  • CLI-105 (FREE) : 0 tokens remaining
===============================================================================================
"""