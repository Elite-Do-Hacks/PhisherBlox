#!/bin/bash

# 1. Ask the user for the port
PORT=""
while [ -z "$PORT" ]; do
    read -p "Enter the port you want to tunnel (e.g., 5000): " PORT
    if [ -z "$PORT" ]; then
        echo "Error: You must enter a port number to continue."
    fi
done

echo "Starting tunnel on port $PORT..."
echo "Press CTRL+C to stop."

# 2. The execution loop
while true; do
  cloudflared tunnel --url http://127.0.0.1:"$PORT"
  echo "Tunnel disconnected. Retrying in 5 seconds..."
  sleep 5
done
