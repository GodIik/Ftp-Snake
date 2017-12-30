import socket, requests, os, sys, time
import ftplib



url = "ftp.bungie.org"
with ftplib.FTP(url) as ftp:
    #ftp = ftp(url)
    username = "anonymous"
    password = "anonymous@"
    ftplogin = ftp.login(user=username, passwd=password)
    ftplogin
    _time_ = time.strftime("%H:%M:%S")
    print("[%s] [+] Login Riuscito!: Username = %s Password = %s" %(_time_, username, password))
    _ftp_ = True
        #_ftpsurf_(url, username, password, ftplogin)
    file_ = input(" File > ")
    file = open(file_, 'rb')
    ftp.storbinary('STOR ' + file_, file)
    print("file inviato")     # send the file
    file.close()
