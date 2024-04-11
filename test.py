import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Ask for the location of the proxy list and the proxy type
PROXY_LIST_FILE = input("Enter the location of the proxy list file: ")
PROXY_TYPE = input("Enter the proxy type (http, https, socks4, socks5): ")

# URL to test the proxy against, choosing a lightweight page for speed
TEST_URL = 'https://www.google.com'

# Maximum number of threads to use
MAX_THREADS = 5

def load_proxies(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def test_proxy(proxy):
    try:
        proxy_url = f"{PROXY_TYPE}://{proxy}"
        proxies = {'http': proxy_url, 'https': proxy_url}

        response = requests.get(TEST_URL, proxies=proxies, timeout=5)  # 5 seconds timeout
        if response.status_code == 200:
            return proxy
    except requests.RequestException as e:
        print(f"Error testing proxy {proxy}: {e}")
    return None

def test_proxies_concurrently(proxy_list):
    working_proxies = []
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        future_to_proxy = {executor.submit(test_proxy, proxy): proxy for proxy in proxy_list}
        for future in as_completed(future_to_proxy):
            proxy = future_to_proxy[future]
            try:
                result = future.result()
                if result:
                    print(f"Working proxy: {result}")
                    working_proxies.append(result)
            except Exception as exc:
                print(f"Proxy {proxy} generated an exception: {exc}")

    print(f"\nTotal working proxies: {len(working_proxies)}")
    # Optionally, save the working proxies to a new file
    with open('working_proxies.txt', 'w') as file:
        for proxy in working_proxies:
            file.write(proxy + '\n')

def main():
    proxies = load_proxies(PROXY_LIST_FILE)
    test_proxies_concurrently(proxies)

if __name__ == "__main__":
    main()
