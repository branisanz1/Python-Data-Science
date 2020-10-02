# Startup scrip for school project 
# This script contains all needed configuration
import pandas as pd
import numpy as np
import os

print("Executing startup script")
pd.show_versions()
print("============================================")
pd.options.display.max_rows = 10
pd.options.display.max_columns = 10
pd.set_option('display.max_columns', None) 

if(not os.path.exists("data")):
    os.system('mkdir data')
    os.system('wget -O sante.txt https://lyaonq.am.files.1drv.com/y4mxH96WBKsE8JsACXScFsJ-dw4AFSi70uPnpleVaBYNnjbH_wFl1DRIwe1hjNcnvJZ8j459FYUFuGWYIOWI8VK0Ma_AzDrACvkJLNSM1NkwPaz3BMPlN-ArLZqiA5vOeEktZXwFEvw9HMPiVr2Kq3B1lG-04-votzdwOnq_BtZKYP7jcAZcH2oeLLSI6FVyL1b07WkQybBeMkdMm-uFdOjag')
    os.system('mv sante.txt data/sante.txt')
    os.system('cd data')
else: print("data directory already exists")
print("File Size: ",os.stat('data/sante.txt').st_size, "Bytes")
nb_lines = len(open('data/sante.txt').readlines())
print("Number of lines is: ", nb_lines)
with open("data/sante.txt",) as myfile:
    head = [next(myfile) for x in range(5)]
print(head)