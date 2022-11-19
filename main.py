from socket import *

ip = input("Enter Target IP to scan: ")
start = int(input("Enter starting port number: "))
end = int(input("Enter ending port number: "))

print("SCanning IP: ", ip)
print("Testing ports please wait...")
for port in range(start,end):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.005)##ESSENTIAL FOR THE TIME TAKES TO SCAN
    if(s.connect_ex((ip,port)) == 0):
        print("Port " + str(port) + " is open")
        s.close()
print("Scanning Completed")