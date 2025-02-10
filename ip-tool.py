import sys
import argparse
import subprocess
import ipaddress

def get_configured_ips():
    """Get the configured IP networks of the container."""
    try:
        # Use 'ip addr' command to get IP addresses
        result = subprocess.run(['ip', 'addr'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error getting IP addresses: {e}"

def check_collision(file_path):
    """Check for IP collisions in the concatenated list of IP networks."""
    try:
        with open(file_path, 'r') as file:
            ip_list = file.read().splitlines()
        
        # Parse IPs and check for collisions
        ip_networks = [ipaddress.ip_network(ip) for ip in ip_list]
        collisions = set()
        
        for i, ip1 in enumerate(ip_networks):
            for j, ip2 in enumerate(ip_networks[i+1:]):
                if ip1.overlaps(ip2):
                    collisions.add((str(ip1), str(ip2)))
        
        if len(collisions)>0:
            print("Collisions found:")
            for collision in collisions:
                print(f"{collision[0]} overlaps with {collision[1]}")
        else:
            print("No collisions found.")
    
    except Exception as e:
        print(f"Error checking collisions: {e}")

def main():
    parser = argparse.ArgumentParser(description="IP Tool for Kubernetes Cluster")
    parser.add_argument('-checkcollision', type=str, help="Check for IP collisions in the given file")
    
    args = parser.parse_args()
    
    if args.checkcollision:
        check_collision(args.checkcollision)
    else:
        print(get_configured_ips())

if __name__ == "__main__":
    main()