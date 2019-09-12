#!/usr/bin/env python
# coding=utf-8

import socket
import sys


# host = "www.google.com"
# port = 1234

# HEADERSIZE = 10
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("192.168.0.76", 23))
#
# full_msg = ""
#
# while True:
#     full_msg = ""
#     new_msg = True
#
#     while True:
#         msg = s.recv(1024)
#         if new_msg:
#             print(f'new message length: {msg[:HEADERSIZE]}')
#             msglen = int(msg[:HEADERSIZE])
#             new_msg = False
#
#         full_msg += msg.decode("utf-8")
#
#         if len(full_msg)-HEADERSIZE == msglen:
#             print("Full message received!")
#             print(full_msg[HEADERSIZE:])
#
#     print(full_msg)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     print("Socket created")
#
#     try:
#         remote_ip = socket.gethostname()
#     except socket.gaierror:
#         print("Hostname could not be resolved")
#         sys.exit()
#
#     print("IP Address: " + remote_ip)
#
#     s.connect((remote_ip, port))
#     print("Socket Connected to using IP " + remote_ip)
#
#     while True:
#         msg = s.recv(1024)
#         print(msg.decode())



# message = "GET / HTTP/1.1\r\n\r\n"
#
# try:
#     s.sendall(message.encode())
# except socket.error:
#     print("Did not send successfully")
#     sys.exit()
#
# print("Message sent successfully!")
#
# reply = s.recv(4096)
#
# print(reply.decode())
#
# s.close()
