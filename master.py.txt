import socket
import argparse
import statistics

def get_time(port):
    s = socket.socket()
    s.connect(("localhost", port))
    s.send(b"GET_TIME")
    time_val = float(s.recv(1024).decode())
    s.close()
    return time_val

def adjust_time(port, offset):
    s = socket.socket()
    s.connect(("localhost", port))
    s.send(f"ADJUST {offset}".encode())
    s.recv(1024)
    s.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", nargs="+", type=int, required=True)
    args = parser.parse_args()

    times = {}
    print("\n[MASTER] Collecting times...")
    for p in args.workers:
        t = get_time(p)
        times[p] = t
        print(f"Worker {p} time: {t}")

    avg_time = statistics.mean(times.values())
    print(f"\n[MASTER] Average time: {avg_time}")

    print("\n[MASTER] Sending adjustments...")
    for p, t in times.items():
        offset = avg_time - t
        adjust_time(p, offset)
        print(f"Worker {p} adjusted by {offset:.2f} seconds")

    print("\n[MASTER] Synchronization complete")
