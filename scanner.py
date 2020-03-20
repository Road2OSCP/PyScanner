#!/busr/bin/python

import pyfiglet
from termcolor import colored

import os
import sys

import argparse
import subprocess
import re

result = pyfiglet.figlet_format("PyScanner", font = "slant") 
print(colored(result, "red"))

path = "/root/Documents/ldap/"

def argsParser():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--ip', dest='ip', required=True, help="IP or CIDR to scan")
        parser.add_argument('-m', '--mode', dest='mode', required=True, help="Scan mode: nmap, enum, smb, all")
        parser.add_argument('-p', '--path', dest='path', required=False, help="Path to folder to store the files in")
        args = parser.parse_args()
        return args
    except:
        sys.exit()

def nmap(ip):
    print(colored("[+] Starting nmap port scan on " + ip, "blue"))
    subprocess.call(["nmap", "-p-", "-T4", ip, "-oG", path + "ports.nmap"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    portPattern = re.compile("(?<=, )(.*?)(?=/)")
    portFile = open(path + "ports.nmap",'r')
    portList = re.findall(portPattern, portFile.read())

    portString = ""
    for port in portList:
        portString += str(port) + ","
    
    print(colored("[+] Portscan done, the following ports are open: " + portString, "green"))
    print(colored("[+] Starting full scan on ports in background", "blue"))
    #subprocess.Popen(["nmap", "-p", portString , "-T4", ip, "-oN", path + "fullportscan.nmap", "-A"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return portList

    
options = argsParser()

portList = []

if "nmap" in options.mode:
    portList = nmap(options.ip)

if options.mode == "all":
    portList = nmap(options.ip)
    if "445" in portList and "139" in portList:
        print(colored("[+] Starting enum4linux", "blue"))
        subprocess.Popen(["ls", path])
