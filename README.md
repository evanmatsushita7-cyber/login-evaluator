Suspicious Login Detector

A Python CLI tool that parses authentication logs and flags brute-force and credential-stuffing activity.

What it does
Brute force — flags any IP with a high number of login attempts (based on --threshold)
Credential stuffing — flags any IP attempting logins against many distinct usernames

Outputs a plain-English summary of flagged IPs.

Usage
bash
python login-evaluator.py --file sample.txt --threshold 10
Flag	Description
--file	Path to the log file to analyze (required)
--threshold	Attempt count that triggers a brute-force flag (required)
Example output:
Excessive Login Attempts: Possible brute force from ip 192.168.1.5
Excessive Login Attempts: Possible brute force from ip 203.0.113.55
Many usernames entered: Possible credential stuffing from 203.0.113.55 


Sample data

sample.txt — fake log data for testing.

Evan, Computer Science student at Carleton University
