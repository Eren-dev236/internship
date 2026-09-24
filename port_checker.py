import socket

# Get port number from the user
port = int(input("Enter port number: "))

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout
sock.settimeout(2)

# Check the port
result = sock.connect_ex(("localhost", port))

if result == 0:
    print(f"Port {port} is OPEN")
else:
    print(f"Port {port} is CLOSED")

# Close the socket
sock.close()