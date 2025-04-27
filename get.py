import socket

def get_ip_from_url(url):
    try:
        if url.startswith('http://'):
            url = url[7:]
        elif url.startswith('https://'):
            url = url[8:]
        
        domain = url.split('/')[0]
        
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Failed to obtain IP address."

url = input("URL")
ip = get_ip_from_url(url)
print(f"IP {url}: {ip}")
input()