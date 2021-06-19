"""
基于epoll方法实现IO并发
重点代码 !
"""

from socket import *
from select import *

# 全局变量
HOST = "0.0.0.0"
PORT = 8889
ADDR = (HOST,PORT)

# 创建tcp套接字
tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)

# 设置为非阻塞
tcp_socket.setblocking(False)

p = epoll() # 建立epoll对象
p.register(tcp_socket,EPOLLIN) # 初始监听对象

# 准备工作，建立文件描述符 和 IO对象对应的字典  时刻与register的IO一致
map = {tcp_socket.fileno():tcp_socket}

# 循环监听
while True:
    # 对关注的IO进行监控
    events = p.poll()
    print("你有新的IO需要处理哦:",events)
    # events--> [(fileno,event),()....]
    for fd,event in events:
        # 分情况讨论
        if fd == tcp_socket.fileno():
            # 处理客户端连接
            connfd, addr = map[fd].accept()
            print("Connect from", addr)
            connfd.setblocking(False) # 设置非阻塞

            p.register(connfd,EPOLLIN|EPOLLET) # 当没有处理，不用边缘触发时，会一直提醒 。边缘触发，当没有处理时只提醒一次，在下一次又有IO发生时，会再次提醒
            map[connfd.fileno()] = connfd # 同时维护字典