x = input("type your target (you can type IP or site name): ")
import sys
from datetime import datetime as time
import socket
your_target = socket.gethostbyname(x) # you can type site name , like to www.google.com
print('-'*50)
print("Time started: " + str(time.now()))
print("scanning your target: " + your_target )
print('-'*50)

try:
    for port in range(1,65535):
        msh = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        msh_result = msh.connect_ex((your_target , port))
        if msh_result == 0 :
            print (f"hey boy port {port} is open" + f" - found in {str(time.now())}")
        msh.close
except KeyboardInterrupt:
    print("\nBye...")
    sys.exit()
except socket.gaierror:
    print("Your hostname is incomprehensible")
    sys.exit()
except socket.error:
    print("I can't connect to server")
    sys.exit()