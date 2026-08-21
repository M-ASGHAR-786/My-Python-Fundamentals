"""
TASK 3: AI Model Benchmark & Log Evaluation Engine

Scenario:
You are building an automated quality-control module for an AI model evaluation pipeline. 
The system receives raw, uncleaned text logs from an evaluation server, extracts the performance 
metrics, and calculates a composite benchmark score.

Given Raw Log String:
raw_log = "   MODEL:llama-3-8b | ACCURACY:0.8925 | LOSS:0.0450   "

Goals:
1. Define a function sanitize_log(log_str: str) -> str:
   - Strips whitespace and converts to lowercase.
2. Define a function extract_metric(clean_log: str, metric_prefix: str, value_length: int = 6) -> float:
   - Finds the starting position of metric_prefix.
   - Slices the numerical text immediately following that prefix.
   - Returns the value as a float.
3. Define a function calculate_composite_score(accuracy: float, loss: float, acc_weight: float = 0.75) -> float:
   - Calculates: (accuracy * acc_weight) - (loss * (1.0 - acc_weight)).
   - Defaults acc_weight to 0.75 if omitted.
   - Returns the score rounded to 4 decimal places.
4. In main():
   - Sanitize raw_log.
   - Extract accuracy and loss.
   - Compute composite score.
   - Print formatted evaluation report showing percentages and decimals.
5. Call main().
"""

# --- Solution ---

raw_log: str = "   MODEL:llama-3-8b | ACCURACY:0.8925 | LOSS:0.0450   "


def sanitize_log(log_str: str) -> str:
    return log_str.strip().lower()


def extract_metric(clean_log: str, metric_prefix: str, value_length: int = 6) -> float:
    start_index: int = clean_log.find(metric_prefix) + len(metric_prefix)
    end_index: int = start_index + value_length
    numeric_data: float = float(clean_log[start_index:end_index])
    return numeric_data


def calculate_composite_score(accuracy: float, loss: float, acc_weight: float = 0.75) -> float:
    score: float = (accuracy * acc_weight) - (loss * (1.0 - acc_weight))
    return round(score, 4)


def main() -> None:
    sanitized_log: str = sanitize_log(raw_log)

    accuracy: float = extract_metric(sanitized_log, "accuracy:")
    loss: float = extract_metric(sanitized_log, "loss:")

    evaluated_score: float = calculate_composite_score(accuracy, loss, 0.80)

    print(f"""\
Model Evaluation Report:
------------------------
Accuracy of Model : {accuracy:.2%}
Loss of Model     : {loss:.4f}
Composite Score   : {evaluated_score:.4f} (Benchmark: {evaluated_score:.2%})""")


main()

"""
Expected Output:
Model Evaluation Report:
------------------------
Accuracy of Model : 89.25%
Loss of Model     : 0.0450
Composite Score   : 0.7050 (Benchmark: 70.50%)
"""
