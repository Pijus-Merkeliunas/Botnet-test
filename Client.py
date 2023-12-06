import sshtunnel
import paramiko
import socket
from pexpect import pxssh
import sys
#import wmi
import getpass
import time
import re

"""try:
    print("Establishing connection to %s" %ip)
    c = wmi.WMI()#ip, user=username, password=password)
    print("Connection established")

except wmi.x_wmi:
    print("Your Username and Password of "+getfqdn(ip)+" are wrong.")

if c is not None:

    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        print(interface.Description, interface.MACAddress)
        for ip_address in interface.IPAddress:
            print(ip_address)

startup = c.Win32_ProcessStartup.new ()
pid, result = c.Win32_Process.Create (CommandLine="", ProcessStartupInformation=startup)"""

"""try:

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,username=username,password=password,port=port)
    print("Connected to %s" % ip)

except paramiko.AuthenticationException:
    print("Failed to connect to %s due to wrong username/password" %ip)
    exit(1)

except:
    print("Error")
    exit(2)"""

class Client:

    def __init__(self, host, port, user):

        self.host = host
        self.port = port
        self.user = user
        self.session = self.connect()

    def connect(self):
        try:

            s = pxssh.pxssh()
            s.login(self.host, self.user, self.port)
            print("Connection succesfull to: " + self.host)
            return s

        except:
            print("Error Connecting to " + self.host)



    def send_command(self, cmd):

        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before



def botnetCommand(command):

    print("\n" + "Command: " + command + "\n")
    for client in botNet:

        output = client.send_command(command)
        print("Output from " + client.host)
        clean_output = output.decode('utf-8')
        print(clean_output, "\n")

def addClient(host, port, user):

    client = Client(host, port, user)
    botNet.append(client)


botNet = []
f = open("Clients.txt", "r+")

for client in f:

    tmp = re.split(":|\s", client)
    addClient(tmp[0],tmp[1],tmp[2])

f.close()

for each in botNet:

    if each.session is None:
        botNet.remove(each)

if len(botNet) == 0:
    print("Unable to connect to any machines")

try:
    f = open("Script.txt", "r")
    for each in f:
        botnetCommand(each)

except:

    active = True
    print("Write command: ")
    while active:
        botnetCommand(input())