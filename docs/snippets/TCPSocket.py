import socket

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
server_address = ('localhost', 12345)
sock.connect(server_address)

# Send data
message = 'Hello, server!'
sock.sendall(message.encode())

# Receive data
data = sock.recv(1024)
received_message = data.decode()
print('Received:', received_message)

# Close the socket
sock.close()
