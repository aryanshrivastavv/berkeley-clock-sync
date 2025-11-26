# Berkeley Clock Synchronization – Distributed Systems Project

## Description
This project implements the Berkeley Clock Synchronization Algorithm using Python sockets.
A master node synchronizes the clocks of multiple worker nodes without using a global clock.

## Files
- worker.py → Worker nodes with different clock drift
- master.py → Master node to synchronize clocks

## How to Run

### Step 1: Start Workers (in separate terminals)
python worker.py --port 5001 --id W1 --drift 4
python worker.py --port 5002 --id W2 --drift -3
python worker.py --port 5003 --id W3 --drift 2

### Step 2: Start Master
python master.py --workers 5001 5002 5003

## Result
All worker clocks synchronize to a common average time.

## Subject
Distributed Systems (M.Tech)
