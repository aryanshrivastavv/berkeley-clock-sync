import socket
import threading
import argparse
import time
import random

def worker_server(port, wid, offset):
    clock_offset = offset

    def handle_client(conn):
        nonlocal clock_offset
        data = conn.recv(1024).decode()

        if data == "GET_TIME":
            current_time = time.time() + clock_offset
            conn.send(str(current_time).encode())

        elif data.startswith("ADJUST"):
            value = float(data.split()[1])
            clock_offset += value
            conn.send(b"OK")
            print(f"[{wid}] Clock adjusted by {value:.2f} seconds")

        conn.close()

    s = socket.socket()
    s.bind(("localhost", port))
    s.listen(5)

    print(f"[{wid}] Worker running on port {port} with offset {offset}")

    while True:
        conn, _ = s.accept()
        threading.Thread(target=handle_client, args=(conn,)).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--id", type=str, required=True)
    parser.add_argument("--drift", type=float, default=random.uniform(-5, 5))
    args = parser.parse_args()

    worker_server(args.port, args.id, args.drift)
