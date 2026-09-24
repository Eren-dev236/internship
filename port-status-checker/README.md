# Port Status Checker

A Python program that checks whether a specific port on the local system is open or closed.

## Features

* Takes a port number as input
* Checks whether the specified port is open or closed
* Uses a socket connection to test the port
* Displays the port status clearly

## Technologies Used

* Python
* Socket Programming
* `socket` module

## How It Works

The program attempts to establish a connection to the specified port on the local system (`localhost`).

* If the connection is successful, the port is reported as **OPEN**.
* If the connection fails, the port is reported as **CLOSED**.

## How to Run

Open a terminal inside the project folder and run:

```bash
python port_checker.py
```

Enter a port number when prompted.

## Example

```text
Enter port number: 5000
Port 5000 is CLOSED
```

If a service is running on the specified port:

```text
Enter port number: 5000
Port 5000 is OPEN
```

## Project Structure

```text
port-status-checker/
├── port_checker.py
└── README.md
```

## Note

This project checks ports on the local system using `localhost`.
