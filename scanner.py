import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from ipaddress import IPv4Address, ip_network
from tqdm import tqdm

def ip_range(network):
    """Generate a list of IP addresses for the given network."""
    return [str(ip) for ip in network.hosts()]

def scan_ip(ip, port, timeout):
    """Attempt to connect to the given IP and port. Returns IP:Port if successful."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                return f"{ip}:{port}"
    except socket.error:
        pass
    return None

def scan_network(network, port, timeout, output_file):
    ips_to_scan = ip_range(network)
    proxy_count = 0

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_ip, ip, port, timeout): ip for ip in ips_to_scan}
        with tqdm(total=len(ips_to_scan), desc=f"Scanning {network}", unit="ip") as progress:
            for future in as_completed(futures):
                ip_port = future.result()
                if ip_port:
                    proxy_count += 1
                    with open(output_file, 'a') as f:
                        f.write(f"{ip_port}\n")
                progress.update(1)

    return proxy_count

def main():
    proxy_file = input("Enter the proxy file path: ")
    port = int(input("Enter port to scan: "))
    timeout = 1  # Socket timeout in seconds
    output_file = "open_proxies.txt"

    with open(proxy_file, 'r') as file:
        proxies = file.readlines()

    total_proxies_found = 0
    for proxy in proxies:
        ip, _ = proxy.strip().split(":")
        first_two = ip.split('.')[:2]
        network = ip_network('.'.join(first_two + ['0.0']) + '/16', strict=False)

        proxy_count = scan_network(network, port, timeout, output_file)
        print(f"Scanning complete for {network}. {proxy_count} open proxies found.")
        total_proxies_found += proxy_count

    print(f"Total scanning complete. {total_proxies_found} open proxies found.")

if __name__ == "__main__":
    main()
