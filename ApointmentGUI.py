import tkinter as tk
import logging 
import uuid
import re
import time
Field1 = "First Name"


Field2 = "Last Name"


Field3 = "Appointment Date"


Field4 = "Appointment Time"

UID = re.sub('\D', '', str(uuid.uuid4())[0:5])
logging.basicConfig(filename=UID+'.log', filemode='w',level = logging.DEBUG, format='%(message)s')
fields = Field1, Field2, Field3, Field4

def fetch(entries):
    global t
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 
        logging.info('%s: "%s"' % (field, text))

def makeform(root, fields):
    entries = []
    TestEnt = tk.Label(root, text= "Unique ID : " + UID)
    TestEnt.pack()
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=25, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Show',
                  command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

    print ("UID:" + (UID))
