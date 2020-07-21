import os
import base64
from math import log
from arguments import *

# function
def encrypt(s):
    temp = str(base64.b64encode(s.encode("utf-8")), "utf-8")
    return temp.replace("/","_") + ".html"

def decrypt(s):	
    temp = s[:-5]
    return str(base64.b64decode(temp.replace("_","/")), "utf-8")

def chkDir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

def tf(cnt):
    return 1 + log(cnt, 2)
    
def idf(cnt, n):
    return log(n / cnt, 2)

