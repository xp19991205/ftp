from ftplib import FTP
import time
import os
def ftpClient(ip, port, user, passwd, ftpfolder, savefolder):
    ftp = FTP()                                     #设置变量
    timeout = 30  
    ftp.connect(ip,port,timeout)       # 连接FTP服务器
    ftp.login(user, passwd)                  # 登录

    # print(ftp.getwelcome())                          # 获得欢迎信息
    ftp.cwd(ftpfolder)                            # 设置FTP远程目录(路径)  
    list = ftp.nlst()                      #获取目录下的文件,获得目录列表  
    for name in list:  
        print(name)
        path = savefolder + name                        # 定义文件保存路径  
        f = open(path,'wb')                             # 打开要保存文件  
        filename = 'RETR ' + name                       # 保存FTP文件  
        ftp.retrbinary(filename,f.write)                # 保存FTP上的文件  
        ftp.delete(name)                                # 删除FTP文件  
        # ftp.storbinary('STOR '+filename, open(path, 'rb')) # 上传FTP文件  
    ftp.quit()

if __name__ == '__main__':
    ftp_IP = "0.0.0.0"
    port = 2121
    user = 'user'
    passwd = '123456'
    imagefolder = 'wanyj/workspace/darknet/image/test'
    savefolder = time.strftime('%Y-%m-%d-%H-%M/', time.localtime(time.time()))
    savefolder = 'F:/SmartEyes/pics/' + savefolder
    if(not os.path.exists(savefolder)):
        os.mkdir(savefolder)
    ftpClient(ftp_IP, port, user, passwd, imagefolder, savefolder)