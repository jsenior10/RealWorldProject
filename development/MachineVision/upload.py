import ftplib

ftpConnection = ftplib.FTP("ftp.jacobsenior.coventry.domains", "jacobsen", "WtYm76iy47")
ftpConnection.pwd()
remotePath = "/www/rpi/"
ftpConnection.cwd(remotePath)
fh = open('Output/cam.jpg', 'rb')
fj = open('Output/red2.jpg', 'rb')
fk = open('Output/green2.jpg', 'rb')
ftpConnection.storbinary('STOR cam.jpg', fh)
fh.close
print("normal image uploaded")
ftpConnection.storbinary('STOR red.jpg', fj)
fj.close
print("red image uploaded")
ftpConnection.storbinary('STOR green.jpg', fk)
fk.close
print("green image uploaded")
fl = open('Output/LargestArea.jpg', 'rb')
ftpConnection.storbinary('STOR redsquare.jpg', fl)
fl.close
print("red box image uploaded")