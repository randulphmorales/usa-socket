#!/usr/bin/env python
# coding=utf-8

import socket
import sys

from datetime import datetime
from matplotlib.animation import FuncAnimation
host = "192.168.76"
port = 23


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

#     try:
#         remote_ip = socket.gethostbyname(host)
#     except socket.gaierror:
#         print("Hostname could not be resolved")
#         sys.exit()
    print("socket created")
    print("IP Address: " + host)

    s.connect((host, port))

    print("Socket connected to " + host)

    while True:
        try:
            msg = s.recv(43)
            if len(msg) == 43:
                dtm = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(str(dtm) + "  " + msg.decode(), end="")
            else:
                break
        except socket.timeout:
            sys.exit()
