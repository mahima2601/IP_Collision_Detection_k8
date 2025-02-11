#!/bin/bash

# Step 1: Collect IP addresses
echo "Collecting IP addresses..."
./collect-ips.sh

# Step 2: Check for collisions
echo "Checking for IP collisions..."
docker run --rm -v $(pwd)/ip-list.txt:/app/ip.txt ip-tool -checkcollision ip.txt