import time

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3
LOCKOUT_TIME = 10

failed_attempts = 0

print("=== Login Attempt Control System ===")

while True:
    password = input("Enter password: ")

    if password == CORRECT_PASSWORD:
        print("Login successful!")
        break

    failed_attempts += 1
    remaining_attempts = MAX_ATTEMPTS - failed_attempts

    print("Incorrect password.")

    if remaining_attempts > 0:
        print(f"Attempts remaining: {remaining_attempts}")

    if failed_attempts >= MAX_ATTEMPTS:
        print(f"\nToo many failed attempts.")
        print(f"Access restricted for {LOCKOUT_TIME} seconds.")

        time.sleep(LOCKOUT_TIME)

        print("\nLockout period ended. You can try again.")
        failed_attempts = 0