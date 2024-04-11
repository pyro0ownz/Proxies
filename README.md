# Proxies
Proxy Range Scanner
The way this one works is you have two ways to do this, You google socks 5 proxies and generate a list with proxy:port 
Then you run the script and it will ask you where the location is
Then it will ask you if you want to use a custom port. 
so you can scan those ranges on either a custom port or you can scan them on the port the proxy was found.

Explaination: 
This was made to scan class b ranges in order to find more proxies based on a list that already has good ones. the way this scanner works is different than 
other range scanners because if the proxy exists on the range chances are there are others. It will take the proxy and port and the use the port and strip out 
the last two octets change them to zeros and scan them to .255.255 on the port the proxy belongs too. It will also go through the whole list but you may end up 
with a giant list of proxies as i found thousands in a couple days. I will be including the tester with the scanner. 

For the updated proxy testing script, you need the following Python libraries:

requests: For sending HTTP/HTTPS requests, and with SOCKS support if you install requests[socks].
concurrent.futures: This is part of the standard Python library (no separate installation needed) and is used for concurrent execution. You also need tqdm for the scanner.
Here’s how you can install the necessary libraries:

requests with SOCKS support:

Open your terminal (Command Prompt or PowerShell on Windows, Terminal on macOS or Linux).

Install requests and SOCKS support via pip by running:

pip install requests[socks]
This command installs both requests and PySocks (for SOCKS proxy support).

Assuming you are using a recent version of Python (3.3 or later), you also need to install tqdm. Here’s how to do it step by step:

Open your terminal or command prompt.

Run the installation command for tqdm:

pip install tqdm
Verifying the Installation
To verify that tqdm is installed correctly, you can run the following command in your terminal or command prompt:

python -c "import tqdm; print(tqdm.__version__)"

concurrent.futures:

This is included with Python, so there's no need to install it separately if you are using Python 3.2 or later. For older versions of Python (2.x or <= 3.1), you need to upgrade to a newer Python version to use concurrent.futures.
Installation Instructions
If you haven’t installed Python, download it from python.org and follow the installation process. Make sure to check the option to 'Add Python to PATH' during the installation on Windows.
Open a terminal or command prompt.
Use pip to install the requests[socks] package as shown above.
Verifying the Installation
To check if the libraries are installed correctly, you can run the following command in your terminal or command prompt:

python -c "import requests, concurrent.futures; print('requests:', requests.__version__)"
This command should display the version of the requests library, confirming that it is installed. Since concurrent.futures is part of the standard library, if this command runs without error, it's installed correctly. If you're using a version of Python that includes concurrent.futures (Python 3.2 and above), there should be no issues with this library.
