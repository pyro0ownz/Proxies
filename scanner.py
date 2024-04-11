from concurrent.futures import ThreadPoolExecutor, as_completed
from ipaddress import ip_network
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

def main():
    # Input file containing proxies
    proxy_file = input("Enter the proxy file path: ")
    use_custom_port = input("Use a custom port for all scans? (y/n): ").lower() == 'y'
    port = int(input("Enter port to scan: ")) if use_custom_port else None
    timeout = 1  # Socket timeout in seconds
    output_file = "open_proxies.txt"

    with open(proxy_file, 'r') as file:
        proxies = file.readlines()

    for proxy in proxies:
        ip, proxy_port = proxy.strip().split(":")
        if not use_custom_port:
            port = int(proxy_port)

        first_two = ip.split('.')[:2]
        start_ip = '.'.join(first_two + ['0', '0'])
        end_ip = '.'.join(first_two + ['255', '255'])
        network = ip_network(f"{start_ip}/{16}", strict=False)

        ips_to_scan = ip_range(network)
        proxy_count = 0

        with ThreadPoolExecutor(max_workers=50) as executor:
            with tqdm(total=len(ips_to_scan), desc="Scanning IPs", unit="ip") as progress:
                futures = {executor.submit(scan_ip, ip, port, timeout): ip for ip in ips_to_scan}
                
                for future in as_completed(futures):
                    ip_port = future.result()
                    if ip_port:
                        proxy_count += 1
                        with open(output_file, 'a') as f:
                            f.write(f"{ip_port}\n")
                    progress.set_postfix(found=proxy_count, refresh=True)
                    progress.update(1)

        print(f"Scanning complete for {ip}. {proxy_count} open proxies found.")

if __name__ == "__main__":
    main()
