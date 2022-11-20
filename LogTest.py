#*Creates a uuid and trims it down and stores that trimed value as IDD2

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