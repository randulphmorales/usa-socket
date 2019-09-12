#!/usr/bin/env python
# coding=utf-8

import socket
import sys

from datetime import datetime

host = "192.168.0.76"
port = 23

output_file = "/home/ran-pc/Project/PYTHON/sockets/sample.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("socket created")

    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    print("IP Address: " + remote_ip)

    s.connect((remote_ip, port))
    s.settimeout(10)

    print("Socket connected to " + host + " using IP " + remote_ip)

    buff_size = 41
    with open(output_file, "w") as fw:
        while True:
            try:
                msg = s.recv(43)
                fw.write(msg.decode())
            except socket.timeout as e:
                print(e, "No connection after 10 seconds")
                s.close()
                break

            # new_msg = str(dtm) + " " + msg.decode()
            # if not msg:
            #     break
            # fw.write(new_msg)
