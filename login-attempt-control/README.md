# Login Attempt Control System

A Python-based login system that limits repeated incorrect password attempts and temporarily restricts access after the maximum number of failures is reached.

## Features

* Password-based login
* Tracks incorrect login attempts
* Allows a maximum of 3 failed attempts
* Temporarily restricts access after repeated failures
* Resets the failed-attempt counter after the lockout period
* Displays the number of remaining attempts
* Allows access after entering the correct password

## Technologies Used

* Python
* `time` module

## How It Works

The system uses a maximum failed-attempt limit.

```text
Maximum attempts: 3
Lockout period: 10 seconds
```

If the user enters an incorrect password:

```text
Wrong password
↓
Failed attempt counter increases
↓
Remaining attempts are displayed
```

After 3 consecutive incorrect attempts:

```text
Too many failed attempts
↓
Access restricted for 10 seconds
↓
Failed-attempt counter resets
↓
User can try again
```

## How to Run

Open the terminal inside the project folder and run:

```bash
python login_control.py
```

The program will ask for a password.

For testing, the correct password is:

```text
admin123
```

## Example

```text
=== Login Attempt Control System ===
Enter password: wrong
Incorrect password.
Attempts remaining: 2

Enter password: wrong
Incorrect password.
Attempts remaining: 1

Enter password: wrong
Incorrect password.

Too many failed attempts.
Access restricted for 10 seconds.

Lockout period ended. You can try again.

Enter password: admin123
Login successful!
```

## Project Structure

```text
login-attempt-control/
│
├── login_control.py
└── README.md
```

## Security Note

This project demonstrates the concept of limiting repeated login attempts. The password is stored directly in the Python source code for demonstration purposes and should not be used this way in a real authentication system. Production systems should use secure password hashing and appropriate authentication controls.
