"""
练习1：index.html 这个网页内容显示在浏览器上
要求，浏览器可以多次访问
"""
from socket import socket
ADDR=("0.0.0.0",8844)
tcp_sock=socket()
tcp_sock.bind(ADDR)
tcp_sock.listen(5)
html="""HTTP/1.1 200 OK
Content-Type:text/html

"""

while True:
    connfd,addr=tcp_sock.accept()
    data=connfd.recv(4096)
    print(data.decode().split("\r\n")[0])   #请求行
    connfd.send(html.encode())
    f=open("index.html")
    html+=f.read()
    connfd.send(html.encode())
    connfd.close()
    f.close()
tcp_sock.close()