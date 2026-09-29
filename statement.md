# Problem Statement: Cybersecurity Log Analyzer

## Background

Every system that has a login page records each attempt as a log entry. When the same IP address fails to log in again and again, it is often a sign of a brute-force attack, where someone tries many passwords to break into an account. Checking such logs by hand is slow and easy to get wrong.

## Problem

Write a Python program that reads login records, counts the successful and failed attempts for every IP address, and points out the IP addresses that look suspicious.

## Input

1. The total number of logs (an integer).
2. For each log:
   - **IP address**: a non-empty string, for example `192.168.1.10`
   - **Status**: either `SUCCESS` or `FAILED` (not case sensitive)

## Rules

- If the IP address is blank, show an error message and skip that record.
- If the status is not `SUCCESS` or `FAILED`, show an error message and skip that record.
- An IP address is **suspicious** if it has **3 or more failed** login attempts.
- If the total failed logins are **more than** the total successful logins, show a warning. Otherwise, show that the activity looks normal.

## Output

The program should print three sections:

1. **Login Report**: successful and failed login counts for each IP address.
2. **Suspicious IPs**: every IP address with 3 or more failed attempts, or a message that none were found.
3. **Final Analysis**: total successful logins, total failed logins, and the warning or normal message.

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

## Approach

- Use two dictionaries, `success` and `failed`, where the key is the IP address and the value is the number of attempts.
- Split the work into four functions:

| Function | Job |
|----------|-----|
| `get_log_data()` | Take input, validate it, and build the two dictionaries |
| `print_report()` | Print the per-IP login report |
| `check_suspicious_ips()` | Find IPs with 3 or more failed attempts |
| `calculate_totals()` | Add up all logins and print the final analysis |

## Concepts Used

Functions, dictionaries, loops, conditional statements, input validation, and data aggregation.
