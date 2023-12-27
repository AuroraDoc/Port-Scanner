import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print("\n" + "[Scanning Target]" + str(target))
    for port in range(1,50): #try to make two variables and make that an input for the range
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip) #retrives the ip address of a domain name

def get_banner(sock):
    return sock.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) #the amount of time it takes to connect before it gives up and skips it and says its closed. The higher the time the higher the accuracy
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[+] Open Port" + str(port) + ":" + str(banner.decode().strip("\n")))
        except:
            print("[+] Open Port" + str(port))
    except:
        pass

targets = input("What ipaddress's do you want to connect to? (split each target with ,):")

if "," in targets:
    for ip_add in targets.split(","):
        scan(ip_add.strip(" "))
else:
    scan(targets)


# use the nslookup command in the terminal to look up a websites ip
