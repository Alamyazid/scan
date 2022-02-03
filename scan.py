import socket
import theading
import concurrent.futures
import colorama
from colorama import Fore
colorama.init()

print_lock = threading.lock()

ip = input("masukan ip yang discan=")

def scan(ip, port):
scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scanner.settimeout(1)
try:
scanner.connect((ip, port))
scanner.close()
with print_lock:
print(Fore.WHITE + f"({port})" + Fore.GRENN + "Opened")
except:
pass

with concurrent.futures.TreadpoolExecutor(max_workers=100)as executor:
for port in range(10000)
executor.sumbit(scan, ip, port + 1)