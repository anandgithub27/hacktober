# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time
import sys

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)    
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user.lower() == stopper.lower():
            mixer.music.stop()
            break
        elif input_of_user.lower() == 'exit':            
            sys.exit()
        else:
            print("Invalid Input..please enter valid input to stop the alarm and Enter 'Exit' to stop the program.")

def log_now(msg):
    with open("HealthDetails.txt", "a") as f:            
        f.write(f"{msg} {datetime.now()}\n------------------------------------------------------ \n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    # watersecs = 40*60
    # exsecs = 30*60
    # eyessecs = 45*60 
    watersecs = 5
    exsecs = 30
    eyessecs = 50

    print(" \n\t***********************************\n\t  Take Care of Programmer Health\n\t***********************************")
    print("\n Welcome")

    while True:
        if time() - init_water > watersecs:
            print("\n*********************************************************************************************")
            print("Water Drinking time. Enter 'Done' to stop the alarm and Enter 'Exit' to stop the program.\n")
            print("*********************************************************************************************")
            musiconloop('water.mp3', 'Done')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("\n*********************************************************************************************")
            print("Eye exercise time. Enter 'Done' to stop the alarm and Enter 'Exit' to stop the program.\n")
            print("*********************************************************************************************")
            musiconloop('water.mp3', 'Done')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("\n*********************************************************************************************")
            print("Physical Activity Time. Enter 'Done' to stop the alarm and Enter 'Exit' to stop the program.\n")
            print("*********************************************************************************************")
            musiconloop('water.mp3', 'Done')
            init_exercise = time()
            log_now("Physical Activity done at")

