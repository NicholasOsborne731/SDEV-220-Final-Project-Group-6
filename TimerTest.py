from datetime import datetime
from datetime import date
from playsound import playsound
################################################################################################

appointmentDate = input('Enter Appointment Date:(format = yyyy/mm/dd, EX: dec 13 2022 = 2022-12-13: ')

appointmentTime = input('Enter Appointment Time:(format = military time, EX: 4:21pm = 16:21:00: ')


################################################################################################
untrimmed_time = datetime.now().time()

current_time = untrimmed_time.replace(second=0,microsecond=0)
print("current time", current_time)

current_date = date.today()
print("current date",  current_date)
################################################################################################

brk = 0
while brk != 1:
    if (appointmentDate == current_date) and (appointmentTime == current_time):
        print("playsound")
    else:
        brk = input('Would you like to exit? y/n ')
        if(brk != "n"):
            exit(99)
        else:
            continue
