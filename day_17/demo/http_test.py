"""
http 请求响应演示
"""
from socket import *

#创建tcp套接字
s=socket()
s.bind(("0.0.0.0",8881))
s.listen(5)
connfd,addr=s.accept()
data=connfd.recv(4096)
print(data.decode())

# http响应格式
html="""HTTP/1.1 200 OK
Content-Type:text/html

hello world
"""
connfd.send(html.encode())
connfd.close()
s.close()