import socket # 导入 socket 模块    

class server:
    @staticmethod
    def send():
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);        # 创建 socket 对象
        host = socket.gethostname() # 获取本地主机名
        port = 12345                # 设置端口好
        s.bind((host,port))         # 绑定端口
        
        s.listen(5)                 # 等待客户端连接
        while True:
            print ("--server--")
            c, addr = s.accept()    # 建立客户端连接。
            print ('连接地址：', addr)
            c.send('欢迎访问菜鸟教程！')
            c.close()                # 关闭连接

class client:
    @staticmethod
    def receiver():
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);        # 创建 socket 对象
        host = socket.gethostname() # 获取本地主机名
        port = 12345                # 设置端口好
        s.connect((host,port))      # 连接
        
        print ("--client--: ",s.recv(1024))
        s.close()
        
server.send()
client.receiver()