#!/usr/bin/python

import re
import sys
import subprocess

ip = sys.argv[1]
fileDir = sys.argv[2]

try:
    print("[+] Starting enum4linux on " + ip)
    enum4linuxOutput = subprocess.check_output(["enum4linux", "10.10.10.169"])
    enumFile = open(fileDir + "/enum4linux.txt", 'w')
    enumFile.write(enum4linuxOutput)
    enumFile.close()
    print("[+] Enum4linux is done, output saved in " + fileDir + "/enum4linux.txt")
except:
    print("suberror")

pattern = re.compile("(?<=user:\[)(.*?)(?=\])")

try:
    f = open(""  , 'r')
    text = f.read()
    f.close()

    matches = re.findall(pattern, text)

    fr = open("", 'w')
    i=0
    for line in matches:
        fr.write(str(matches[i]) + '\n')
        i = i+1

    fr.close()
except Exception as err:
    print("Oops something went wrong..." + str(err))