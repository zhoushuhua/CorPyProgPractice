# user python download ftp file
import ftplib
import os
import socket

# const var
HOST = "ftp.iap.ac.cn"
DIR="/geog/hlens"
FILE = "00001-02161.00001-01081"

# defined function to download
def main():
    try:
        # connect ftp
        # print "> input ftp Host:"
        # data = raw_input()
        # if data != "" : HOST = data
        ftp = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print "ERROR : cannot reach %s" % HOST
        # terminal function
        return

    try:
        # login to ftp
        ftp.login()
    except ftplib.error_perm:
        print "ERROR : cannot login by anonymous"
        # terminal function
        return

    try:
        # print "> input ftp DIR:"
        # data = raw_input()
        # if data != "" : DIR = data
        ftp.cwd(DIR)
    except ftplib.error_perm:
        print "ERROR : cannot change to %s" % DIR
        # terminal function
        return

    try:
        # close file
        # with open(FILE, "wb") as f:
        #     ftp.retrbinary("RETR %s" % FILE, f.write)
        # print "> input ftp download file Name:"
        # data = raw_input()
        # if data != "" : FILE = data
        f = open(FILE, "wb")
        ftp.retrbinary("RETR %s" % FILE, f.write)
    except ftplib.error_perm:
        print "ERROR : cannot read file %s " % FILE
        return
    finally:
        # close file
        if f in locals():
            f.close()

    # return
    ftp.quit()

if __name__ == "__main__":
    main()