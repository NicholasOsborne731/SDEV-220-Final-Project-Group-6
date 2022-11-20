#Program to read log files based on uuid
#TESTFILE Currently also creates its own UUID for debug purposes. 

import logging
import uuid 
import re
import random as r

Random = str(r.randrange(0, 99999999))
IDD = re.sub('\D', '', str(uuid.uuid4())[0:5])
print("Your ID : " + IDD)
logging.basicConfig(filename=IDD+'.log', filemode='w',level = logging.DEBUG, format='%(message)s')
logging.info("ID : "+ IDD + "\n" + Random)
balls = input("Type your uniqe ID : ")
with open(balls + ".log") as f:
    for line in f:
        print(line)