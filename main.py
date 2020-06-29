from worldmanager import WorldManager
from world import World
from animal import Animal

print("\nWelcome to the WildLife Simulator!\n")

while(True):
    iterations = int(input("Please input the number of iterations (must be > 0): "))
    energy_gain = int(input("Please input the energy gain (must be >= 0): "))
    reproduction_threshold = int(input("Please input the reproduction_threshold (must be > 2): "))

    if iterations <= 0 or energy_gain < 0 or reproduction_threshold <= 2:
        print("Bad input, please try again\n")
    else:
        break    

while(True):
    file_name = input("Please input the full name of your configuration file (exemple.txt): ")
    try:
        file = open(file_name, "r")
        break
    except:
        print("Bad input, please try again")
                

print(file.read())
