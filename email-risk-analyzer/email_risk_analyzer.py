import re

def analyze_email(email):
    score = 0
    warnings = []

    # Urgent or threatening language
    urgent_words = [
        "urgent",
        "immediately",
        "act now",
        "account suspended",
        "verify now",
        "limited time",
        "final warning"
    ]

    # Sensitive information requests
    sensitive_words = [
        "password",
        "otp",
        "one-time password",
        "credit card",
        "bank account",
        "cvv",
        "social security",
        "pin"
    ]

    # Check for urgent language
    for word in urgent_words:
        if word in email.lower():
            score += 1
            warnings.append(f"Urgent language detected: '{word}'")

    # Check for sensitive information requests
    for word in sensitive_words:
        if word in email.lower():
            score += 2
            warnings.append(f"Sensitive information request detected: '{word}'")

    # Check for links
    links = re.findall(r"https?://\S+|www\.\S+", email)

    if links:
        score += 1
        warnings.append("Email contains a link. Verify the destination before opening it.")

    # Check for suspicious link patterns
    for link in links:
        if "http://" in link.lower():
            score += 1
            warnings.append("Unencrypted HTTP link detected.")

        if re.search(r"\d+\.\d+\.\d+\.\d+", link):
            score += 2
            warnings.append("Link uses an IP address instead of a normal domain.")

    # Classify risk
    if score >= 6:
        risk = "HIGH RISK"
    elif score >= 3:
        risk = "MEDIUM RISK"
    else:
        risk = "LOW RISK"

    print("\nEmail Risk Level:", risk)
    print("Risk Score:", score)

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print("-", warning)
    else:
        print("\nNo obvious suspicious patterns detected.")


# Get email content
print("=== Email Risk Analyzer ===")
print("Paste the email content below.")
print("Type END on a new line when finished.\n")

lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    lines.append(line)

email_content = "\n".join(lines)

analyze_email(email_content)