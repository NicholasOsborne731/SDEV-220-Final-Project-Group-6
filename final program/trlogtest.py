#you are the docter 
import logging
import uuid 
import re
import random as r
import os as os

#patient id test
PatientTest1 = input("Make up a patient 1: ")
PatientTest2 = input("Make up a patient 2: ")
PatientTest3 = input("Make up a patient 3: ")

PatientArray = [PatientTest1, PatientTest2, PatientTest3]

#generate random uuid for patients 
Random = str(r.randrange(0, 99999999))
IDD1 = re.sub('\D', '', str(uuid.uuid4())[0:5])
IDD2 = re.sub('\D', '', str(uuid.uuid4())[0:5])
IDD3 = re.sub('\D', '', str(uuid.uuid4())[0:5])
IDArray = [IDD1, IDD2, IDD3]

#creates log file 
def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)  

setup_logger('log1', "logs/"+PatientTest1.replace(" ", "_")+'.log')
setup_logger('log2', "logs/"+PatientTest2.replace(" ", "_")+'.log')
setup_logger('log3', "logs/"+PatientTest3.replace(" ", "_")+'.log')

logger_1 = logging.getLogger('log1')
logger_2 = logging.getLogger('log2')
logger_3 = logging.getLogger('log3')

logger_1.info(IDD1)
logger_2.info(IDD2)
logger_3.info(IDD3)

#checking patients and showing the current patient index
def Main():
    Counter = -1
    balls = input("Choose Patient || press y for patient index Or enter patient name, First and Last:  ")
    if(balls == "y"):
        for i in PatientArray:
            Counter = Counter + 1
            print("Patient Name:",i, " || Patient ID : ", IDArray[Counter])
    if(balls != "y"):
        for i in PatientArray:
            if(balls != i):
                print("That patient doesnt exist")
                Main()
            else:
                with open(balls.replace(" ", "_") + ".log") as f:
                    for line in f:
                        print("Patient Name: ",balls, " || UID: " + line)
                Main()
Main()
