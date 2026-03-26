import socket
import signal
import sys

def signal_handler(sig, frame):
    print('\nShutting down...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('::', 12345))
server.listen(1)
print("Server listening on port 12345 (handles restarts)...")

conn, addr = server.accept()
print(f"Connected by {addr} (EV3)")


