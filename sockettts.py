import socket

hostname = raw_input("Insert IP: ")

hostIP = socket.getfqdn(hostname)

print hostIP