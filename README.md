Suspicious Login Detector

A Python command-line tool that analyzes SSH authentication logs for signs of common attack patterns: brute-force login attempts, credential stuffing, and logins occurring during unusual hours.

What It Does

This tool reads a log file containing SSH login attempts and looks for three specific attack signatures:

Brute Force Detection — Flags any IP address that has made an excessive number of failed login attempts, suggesting repeated password guessing against a single account.
Credential Stuffing Detection — Flags any IP address that has attempted logins using an unusually high number of distinct usernames, suggesting an attacker cycling through a list of known/leaked credentials rather than targeting one account.
Odd-Hour Login Detection — Flags any login activity (successful or failed) occurring during typical "off hours" (before 5 AM), which can indicate compromised credentials being used outside of normal activity patterns.

The tool is resilient to malformed log lines — entries that don't match the expected format are safely skipped rather than crashing the program.

How to Run It
py login-evaluator.py --file sample.txt --threshold 4 --timestamp yes
Arguments
Argument	Description
--file	The log file to analyze (required)
--threshold	The number of attempts/usernames that triggers a warning (required)
--timestamp	If provided, also checks and reports odd-hour login activity
Sample Output

Running the tool against a sample log file produces output like this:

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
