#!/usr/bin/env python
# coding=utf-8

import socket
import sys
import time
from datetime import datetime

host = "192.168.0.76"
port = 23

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created")

    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    print("IP Address: " + remote_ip)

    s.connect((remote_ip, port))
    s.settimeout(10)
    # s.setblocking(0)
    print("Socket Connected to using IP " + remote_ip)

    buff_size = 43
    while True:
        try:
            msg  = s.recv(buff_size)
            if len(msg) == buff_size:
                dtm = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(str(dtm) + "  " + msg.decode(), end="")
            else:
               pass
        except socket.timeout as e:
            print(e, " : No connection after 10 seconds")
            break
    s.close()
