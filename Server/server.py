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

while True:  # Loop to re-accept after disconnects
    conn, addr = server.accept()
    print(f"Connected by {addr} (EV3)")
    
    try:
        while True:
            message = input("Enter message (or 'quit' to disconnect): ")
            if message.lower() == 'quit':
                conn.send(b'quit')
                break
            conn.send(message.encode())
    except (ConnectionResetError, BrokenPipeError):
        print("Client (EV3) disconnected—waiting for reconnect...")
    except KeyboardInterrupt:
        raise
    finally:
        conn.close()
        print("Connection closed—ready for next...")

