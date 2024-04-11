# Proxies
Proxy Range Scanner
The way this one works is you have two ways to do this, You google socks 5 proxies and generate a list with proxy:port 
Then you run the script and it will ask you where the location is
Then it will ask you if you want to use a custom port. 

Explaination: 
This was made to scan class b ranges in order to find more proxies based on a list that already has good ones. the way this scanner works is different that 
other range scanners because if the proxy exists on the range chances are there are others. It will take the proxy and port and the use the port and strip out 
the last two octets change them to zeros and scan them to .255.255 on the port the proxy belongs too. It will also go through the whole list but you may end up 
with a giant list of proxies as i found thousands in a couple days. I will be including the tester with the scanner. you have to modify the path inside the code 
for the location of the found proxies as some of these ips will contain websites so they need to be tested properly. 

