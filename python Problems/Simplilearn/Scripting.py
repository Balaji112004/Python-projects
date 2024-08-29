import time;
epc=time.time()
localtime=time.localtime(epc)
print(localtime)
print(localtime.tm_year)
print(time.ctime(epc))
import os;
print("_________________________________________")
print(os.getcwd())
print(os.path.abspath("looop.py"))