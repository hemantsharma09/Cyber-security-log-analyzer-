# Cybersecurity Log Analyzer

A beginner-friendly Python command-line project that simulates how security teams monitor login activity. It takes login records as input, analyzes them, and flags suspicious behavior such as brute-force attempts.

## Features

- Accepts login records (IP address + SUCCESS/FAILED status)
- Validates input: rejects blank IPs and skips invalid statuses
- Counts successful and failed logins per IP address
- Flags IPs with 3 or more failed attempts as suspicious
- Prints a final summary and warns if failed logins outnumber successful ones

## Requirements

- Python 3.x
- No external libraries needed

## How to Run

```bash
python log_analyzer.py
```

## How It Works

| Function | Purpose |
|----------|---------|
| `get_log_data()` | Collects log entries and stores per-IP counts in two dictionaries (`success`, `failed`) |
| `print_report()` | Displays successful and failed login counts for each IP |
| `check_suspicious_ips()` | Flags any IP with 3 or more failed attempts |
| `calculate_totals()` | Totals all logins and warns if failures exceed successes |

## Sample Input

```
Enter total number of logs: 5

Log 1
Enter IP address: 192.168.1.10
Enter status (SUCCESS/FAILED): FAILED

Log 2
Enter IP address: 192.168.1.10
Enter status (SUCCESS/FAILED): FAILED

Log 3
Enter IP address: 192.168.1.10
Enter status (SUCCESS/FAILED): FAILED

Log 4
Enter IP address: 10.0.0.5
Enter status (SUCCESS/FAILED): SUCCESS

Log 5
Enter IP address: 10.0.0.5
Enter status (SUCCESS/FAILED): SUCCESS
```

## Sample Output

```
--- LOGIN REPORT ---

Successful Logins:
10.0.0.5 -> 2

Failed Logins:
192.168.1.10 -> 3

--- SUSPICIOUS IPS ---
192.168.1.10 -> 3 failed attempts

--- FINAL ANALYSIS ---
Total Successful Logins: 2
Total Failed Logins: 3
Warning: High number of failed login attempts!
```

## Concepts Used

- Functions
- Dictionaries
- Loops and conditionals
- Input validation
- Data aggregation

## Future Improvements

- Read logs from a file instead of manual input
- Add timestamps to log entries
- Export reports to CSV
- Automatically block flagged IPs
- Add IP address format validation

## Author

Hemant Sharma
 
