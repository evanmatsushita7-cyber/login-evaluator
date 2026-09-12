# Suspicious Login Detector

A Python command-line tool that analyzes SSH authentication logs for signs of brute-force attacks, credential stuffing, and odd-hour login activity.

## What It Does

- **Brute Force Detection** — Flags any IP address with an excessive number of failed login attempts.
- **Credential Stuffing Detection** — Flags any IP address that has tried an unusually high number of distinct usernames.
- **Odd-Hour Login Detection** — Flags login activity (successful or failed) occurring before 5 AM.

Malformed log lines are safely skipped rather than crashing the program.

## How to Run It

```
py login-evaluator.py --file sample.txt --threshold 4 --timestamp yes
```

**Arguments:**

- `--file` — the log file to analyze (required)
- `--threshold` — number of attempts/usernames that triggers a warning (required)
- `--timestamp` — if provided, also checks for odd-hour login activity

## Sample Output

```
192.168.1.5 6
45.33.12.9 1
203.0.113.55 7
66.42.11.3 2
192.168.1.5 {'root', 'admin', 'test'}
45.33.12.9 {'guest'}
203.0.113.55 {'admin', 'user', 'postgres', 'test', 'administrator', 'guest', 'root'}
66.42.11.3 {'oracle'}
Excessive Login Attempts: Possible brute force from ip 192.168.1.5
Excessive Login Attempts: Possible brute force from ip 203.0.113.55
Many usernames entered: Possible credential stuffing from 203.0.113.55
Odd hour detected from 203.0.113.7
```
