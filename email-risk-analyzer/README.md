# Email Risk Analyzer

A Python-based tool that analyzes email content and identifies potentially unsafe messages by detecting suspicious patterns such as urgent requests, sensitive information prompts, and potentially unsafe links.

## Features

* Detects urgent or threatening language
* Identifies requests for sensitive information such as passwords and OTPs
* Detects links included in email content
* Flags unencrypted HTTP links
* Detects links using IP addresses instead of normal domain names
* Calculates a risk score
* Classifies emails as:

  * LOW RISK
  * MEDIUM RISK
  * HIGH RISK
* Provides warnings explaining why an email was flagged

## Technologies Used

* Python
* Regular Expressions (`re`)
* Socket-free pattern-based analysis

## How It Works

The program scans the provided email content for predefined suspicious patterns.

Each detected pattern contributes to a risk score:

* Urgent language → increases risk
* Sensitive information requests → increases risk significantly
* Links → increase risk
* HTTP links → additional risk
* IP-address links → additional risk

The final score determines the email's risk level.

## How to Run

Open the terminal inside the project folder and run:

```bash
python email_risk_analyzer.py
```

Paste the email content into the terminal.

Type:

```text
END
```

on a new line when you have finished entering the email.

## Example

### Input

```text
URGENT! Your account has been suspended.

Verify now or your account will be permanently closed.
Click here: http://192.168.1.50/login

Enter your password and OTP immediately.

END
```

### Output

```text
Email Risk Level: HIGH RISK
Risk Score: 11

Warnings:
- Urgent language detected
- Sensitive information request detected
- Email contains a link
- Unencrypted HTTP link detected
- Link uses an IP address instead of a normal domain
```

## Project Structure

```text
email-risk-analyzer/
│
├── email_risk_analyzer.py
└── README.md
```

## Note

This project uses rule-based pattern detection for educational purposes. It identifies potentially suspicious patterns but does not guarantee that an email is malicious or safe.
