# Health Management System
# 3 clients - Ram, Sham and Jhon

import datetime

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

def gettime():
    return datetime.datetime.now()

def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if(c == 1):
            value = input("type here\n")
            with open("HealthSystem\Sham-ex.txt", "a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c == 2):
            value = input("type here\n")
            with open("HealthSystem\Sham-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

    elif(k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("HealthSystem\Ram-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("HealthSystem\Ram-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

    elif(k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("HealthSystem\Jhon-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("HealthSystem\Jhon-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Sham),2(Ram),3(Jhon)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if(c == 1):
            with open("HealthSystem\Sham-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c == 2):
            with open("HealthSystem\Sham-food.txt") as op:
                for i in op:
                    print(i, end="")

    elif(k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("HealthSystem\Ram-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("HealthSystem\Ram-food.txt") as op:
                for i in op:
                    print(i, end="")

    elif(k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("HealthSystem\Jhon-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("HealthSystem\Jhon-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Sham,Ram,Jhon)")


print("health management system")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for Sham 2 for Ram 3 for Jhon "))
    take(b)
else:
    b = int(input("Press 1 for Sham 2 for Ram 3 for Jhon "))
    retrieve(b)
