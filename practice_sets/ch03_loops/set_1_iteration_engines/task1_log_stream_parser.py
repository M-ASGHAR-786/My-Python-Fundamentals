"""
Task 1: Syntax & Method Drill — Telemetry Log Stream Parser
Directory: practice_sets/ch03_loops/set_1_iteration_engines/
File: task1_log_stream_parser.py

Scenario & Business Problem:
You are developing an automated log ingestion parser for a backend cloud cluster. 
The microservice cluster continuously outputs telemetry events. Your script must ingest 
a batch of log records, filter out routine informational noise, flag high-latency 
operational anomalies, track critical failures, and immediately shut down log stream 
processing if a fatal panic signal is detected.

Raw Input Data:
Dataset of 8 event records (Service, Level, Latency, Message).

Business Rules & Processing Constraints:
1. Interactive Threshold Validation:
   - Indefinite loop prompting for an Alert Latency Threshold in ms (> 0).
2. Stream Filtering & Panic Triggers:
   - Discard "INFO" level records.
   - Tag actionable records ("WARNING", "ERROR", "CRITICAL") as [HIGH LATENCY] or [NORMAL LATENCY].
   - If message contains "FATAL_PANIC", include it in alerts and terminate further parsing immediately.
3. Telemetry Metrics Aggregation:
   - Track total logs inspected, total flagged alerts, latency breaches, and ingestion exit status.
4. Output Display:
   - Numbered list of flagged anomalies followed by a Telemetry Summary report.
"""

log_stream: list[dict[str, str | int]] = [
    {"Service": "auth-api", "Level": "INFO", "Latency": 45, "Message": "User token verified"},
    {"Service": "payment-gateway", "Level": "WARNING", "Latency": 320, "Message": "Gateway timeout retry 1"},
    {"Service": "database-proxy", "Level": "INFO", "Latency": 15, "Message": "Read query executed"},
    {"Service": "order-processor", "Level": "ERROR", "Latency": 850, "Message": "Deadlock detected on checkout"},
    {"Service": "cache-redis", "Level": "CRITICAL", "Latency": 1200, "Message": "Out of memory error"},
    {"Service": "notification-hub", "Level": "INFO", "Latency": 25, "Message": "Email queued"},
    {"Service": "payment-gateway", "Level": "CRITICAL", "Latency": 1500, "Message": "FATAL_PANIC: Core banking link down"},
    {"Service": "analytics-worker", "Level": "ERROR", "Latency": 400, "Message": "Queue ingestion failed"},
]


def get_latency_threshold() -> int:
    """Prompts for a positive latency alert threshold using indefinite validation."""
    while True:
        threshold: int = int(float(input("Enter latency alert threshold (ms): ")))
        if threshold > 0:
            return threshold
        print("Threshold must be a positive integer greater than 0.")


def parse_telemetry_stream(
    events: list[dict[str, str | int]], threshold: int
) -> tuple[list[dict[str, str | int]], int, int, str]:
    """
    Processes log records in a single pass.
    Returns: (flagged_anomalies, inspected_count, latency_breach_count, exit_status)
    """
    flagged_anomalies: list[dict[str, str | int]] = []
    inspected_count: int = 0
    latency_breach_count: int = 0
    exit_status: str = "COMPLETED: Clean Batch Run"

    for event in events:
        inspected_count += 1
        latency: int = int(event["Latency"])

        if event["Level"] == "INFO":
            continue

        is_breach: bool = latency > threshold
        if is_breach:
            latency_breach_count += 1

        tag: str = "[HIGH LATENCY]" if is_breach else "[NORMAL LATENCY]"

        flagged_anomalies.append({
            "Service": event["Service"],
            "Level": event["Level"],
            "Latency": latency,
            "Tag": tag,
            "Message": event["Message"],
        })

        if "FATAL_PANIC" in str(event["Message"]):
            exit_status = "HALTED: Fatal Panic Encountered"
            break

    return flagged_anomalies, inspected_count, latency_breach_count, exit_status


def main() -> None:
    threshold: int = get_latency_threshold()
    anomalies, inspected_logs, breaches, status = parse_telemetry_stream(
        log_stream, threshold
    )

    print("\n" + "=" * 80)
    print("FLAGGED TELEMETRY ANOMALIES")
    print("=" * 80)

    for index, alert in enumerate(anomalies, start=1):
        print(
            f"{index}. [{alert['Level']}] Service: {alert['Service']} | "
            f"Latency: {alert['Latency']}ms {alert['Tag']}\n"
            f"   Message: {alert['Message']}"
        )
        print("-" * 80)

    print("\n" + "=" * 80)
    print("TELEMETRY INGESTION SUMMARY")
    print("=" * 80)
    print(f"Total Logs Inspected   : {inspected_logs}")
    print(f"Total Flagged Alerts   : {len(anomalies)}")
    print(f"Latency Breaches Count : {breaches}")
    print(f"Ingestion Exit Status  : {status}")
    print("=" * 80)


if __name__ == "__main__":
    main()

"""
EXPECTED TERMINAL OUTPUT:

Enter latency alert threshold (ms): 500

================================================================================
FLAGGED TELEMETRY ANOMALIES
================================================================================
1. [WARNING] Service: payment-gateway | Latency: 320ms [NORMAL LATENCY]
   Message: Gateway timeout retry 1
--------------------------------------------------------------------------------
2. [ERROR] Service: order-processor | Latency: 850ms [HIGH LATENCY]
   Message: Deadlock detected on checkout
--------------------------------------------------------------------------------
3. [CRITICAL] Service: cache-redis | Latency: 1200ms [HIGH LATENCY]
   Message: Out of memory error
--------------------------------------------------------------------------------
4. [CRITICAL] Service: payment-gateway | Latency: 1500ms [HIGH LATENCY]
   Message: FATAL_PANIC: Core banking link down
--------------------------------------------------------------------------------

================================================================================
TELEMETRY INGESTION SUMMARY
================================================================================
Total Logs Inspected   : 7
Total Flagged Alerts   : 4
Latency Breaches Count : 3
Ingestion Exit Status  : HALTED: Fatal Panic Encountered
================================================================================
"""