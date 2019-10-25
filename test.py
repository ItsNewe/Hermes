from ftplib import FTP

i = input()
ftp = FTP(i)
ftp.login()
ftp.retrlines("LIST")
ftp.quit()