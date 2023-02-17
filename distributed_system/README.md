# Distributed System

## Description

a TCP server that can accept and hold a maximum of N clients (where N is configurable).
These clients are assigned ranks based on first-come-first-serve, i.e whoever connects first receives the next available
high rank. Ranks are from 0–N, 0 being the highest rank.

Clients can send to the server commands that the server distributes among the clients. Only a client with a lower rank
can execute a command of a higher rank client. Higher rank clients cannot execute commands by lower rank clients, so 
these commands are rejected. The command execution can be as simple as the client printing to console that command has been executed.

If a client disconnects the server should re-adjust the ranks and promote any client that needs to be promoted not to leave any gaps in the ranks.

## How to run

### In linux
in terminal run "chmod u+x distributed_system.py" to make the scripts executable
./distributed_system

### In windows/MacOS
python distributed_system.py

## To run the tests:
python -m doctest -v ./tests/distributed_system.test.py | tail -2
