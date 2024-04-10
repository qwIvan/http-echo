#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket

def http_response(request):
    """构建HTTP响应报文，包含接收到的请求报文"""
    return f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n{request}".encode()

def start_server(host='localhost', port=8001):
    """启动TCP服务器"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"服务器启动，监听 {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"来自 {addr} 的连接")
                request = conn.recv(1024).decode()
                print(f"接收到的请求:\n{request}")
                response = http_response(request)
                conn.sendall(response)

if __name__ == '__main__':
    start_server()
