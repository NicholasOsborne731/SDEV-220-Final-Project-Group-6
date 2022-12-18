import os as os
user_input = input("Enter patients name: ")
user = user_input.replace(" ", "_")+".log"
Name = user_input
x = 0
for i in os.listdir("logs/"):
    x = x + 1
    if(user == i):
        with open("logs/"+user) as f:
            for line in f:
                print("Patient Name: ",Name, " || UID: " + line)
        exit(99)
    if(x >= len(os.listdir("logs/"))):
        print("User not found")
        exit(99)