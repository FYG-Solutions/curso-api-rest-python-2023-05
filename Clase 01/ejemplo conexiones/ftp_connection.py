from ftplib import FTP
  
ftp = FTP('test.rebex.net')
  
ftp.login('demo','password')
  
# changing directory
ftp.cwd('pub')
  
ftp.dir()

ftp.quit()