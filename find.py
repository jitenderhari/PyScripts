#!/usr/bin/env python
# This program provides same functionality as "find / -name " command on *nix systems
# This is  just a demo to showcase how we can manipulate and handle the 

# unix/ OS processes by 'subprocess' module and its Popen method.
# on Unix Systems Popen 'os.execvp()' like functionality , while on Windows this Popen class uses 'CreateProcess()'
# function.

import subprocess
import os
 
 def find():

    ''' this function defines the logic for our find program'''
    
    y = input("Enter a text you want to search on the system!")
    
    # strip off the whitespace characters like newline character from the provided string
    s = y.rstrip("\n")
    print("string", s)
    
    #Popen ensures that evey new child program is served by the new process and 
    # 'subprocess.PIPE' indicates that a pipe should be opened to the output stream
    find = subprocess.Popen([r"/usr/bin/find", "/", "-name", y, "-print"], stdout=subprocess.PIPE)
    
    #loop over the all the paths returned by find 
    for line in find.stdout.readlines():
        print("line", line)
        l = line.rstrip("\n")
        list = subprocess.Popen([r"ls", "-l", l], stdout=subprocess.PIPE)
        list_stdout = list.communicate()[0]
        print(list_stdout)
    file = subprocess.Popen([r"file", l], stdout=subprocess.PIPE)
    file_stdout = file.communicate()[0]
    print(file_stdout)
 
def main():
    find()
