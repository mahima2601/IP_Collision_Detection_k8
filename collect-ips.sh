#!/bin/bash

# Output file
output_file="ip-list.txt"

# Clear the output file
> "$output_file"

# Get IP addresses of all pods
echo "Collecting pod IPs..."
kubectl get pods -o wide --all-namespaces | awk '{print $7}' | grep -v IP >> "$output_file"

# Get IP addresses of all services
echo "Collecting service IPs..."
kubectl get services -o wide --all-namespaces | awk '{print $4}' | grep -v CLUSTER-IP >> "$output_file"

# Get IP addresses of all nodes
echo "Collecting node IPs..."
kubectl get nodes -o wide | awk '{print $6}' | grep -v INTERNAL-IP >> "$output_file"

echo "IP addresses saved to $output_file"