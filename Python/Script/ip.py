#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, re, sys, subprocess
from blessings import Terminal
os.system('clear')
print("Checking connection...\n\n")
arq = open(sys.argv[1])
t = Terminal()
for line in arq: 
 line = line.replace('\n', '').replace('\r', '')
 terminal = "ping -c4 %s" %line
 #terminal = "shutdown /p %s" %line
 os.system("{} > /tmp/{}.txt".format(terminal, line))
 busca = open("/tmp/{}.txt".format(line))
 for item in range(2):
  r = busca.readline()  
 if re.search ("64 bytes from", r):
  print(line, t.green("Connection OK!"))
  #os.system('shutdown /p')
  print(r)
 else:
  print(line, t.red("Connection OFF!"))
  for item in range(2):
   r = busca.readline()
  print(r)
 os.system("rm /tmp/{}.txt".format(line))
