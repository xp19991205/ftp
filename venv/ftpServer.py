from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import tkinter as tk
from tkinter import filedialog
import tkinter
from tkinter import*
import socket
import threading
def thread_it(func, *args):
  '''将函数打包进线程'''
  # 创建
  t = threading.Thread(target=func, args=args)
  # 守护 !!!
  t.setDaemon(True)
  # 启动
  t.start()
  # 阻塞--卡死界面！
  # t.join()
def run():
    user=entry1.get()
    password=entry2.get()
    IP=entry3.get()
    #print(entry1.get())  # 获取文本框的内容

    root = tk.Tk()
    root.withdraw()
    Fpath = filedialog.askdirectory()
    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, Fpath, perm='elradfmw')

    # authorizer.add_anonymous('/home/nobody')

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((IP, 21), handler)

    server.serve_forever()

#获取本机电脑名
myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
myaddr = socket.gethostbyname(myname)
win = tkinter.Tk()
win.title("徐棚制作的ftp软件")
button = tkinter.Button(win, text="点击建立ftp服务器",  command=lambda :thread_it(run()).pack())  # 收到消息执行这个函数
button.pack()  # 加载到窗体，
text=tkinter.Text(win)
entry1 = tkinter.Entry(win, width=50, bg="white", fg="black")

entry2 = tkinter.Entry(win, width=50, bg="white", fg="black")
entry3 = tkinter.Entry(win, width=50, bg="white", fg="black")
# entry1=tkinter.Entry(win,show="*",width=50,bg="red",fg="black")
label1 = Label(win, text="用户名")
label2 = Label(win, text="密码")
label3 = Label(win, text="你的内网地址是(请输入到IP地址栏)")
label4 = Label(win, text=ip)
label5 = Label(win, text="端口21,点击运行后选择文件夹即可")
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
label4.pack()
entry3.pack()
label4.pack()
win.mainloop()

