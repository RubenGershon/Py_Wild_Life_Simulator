from animal import Animal
from world import World
import random as rand
import sys


class WorldManager:

    """Class representing a world, characterized by:"""

    def __init__(self, world, animal_list, nIterations, energy_gain, reproduction_threshold):
        try:
            len(animal_list) != 0
            reproduction_threshold > 2
        except:
            print("WorldManager __init__ wrong Args.\n")
        else:
            self._world = world
            self._animal_list = animal_list
            self._nIterations = nIterations
            self._energy_gain = energy_gain
            self._reproduction_threshold = reproduction_threshold

    def InitWorldWithAnimals(self):
        for animal in self._animal_list:
            self._world.WorldUpdateAnimalNewPos(animal._y_coordinate, animal._x_coordinate)

    def GetActivatedGene(self, chromosome):
        sum = 0
        index = 0

        for i in range(8):
            sum += chromosome[i]

        newArr = [None] * sum

        for i in range(8):   
            for j in range(chromosome[i]):
                newArr[index] = chromosome[i]
                index += 1

        return newArr[rand.randint(0,sys.maxsize) % sum]


    def MoveAnimal(self, animal, gene):
        newDirection = (animal.direction + gene) % 8

        if newDirection == 0:
            animal.y_coordinate = (animal.y_coordinate + 1) % self._world.height

        elif newDirection == 1:
            animal.y_coordinate = (animal.y_coordinate + 1) % self._world.height
            animal.x_coordinate = (animal.x_coordinate + 1) % self._world.width
        
        elif newDirection == 2:
            animal.x_coordinate = (animal.x_coordinate + 1) % self._world.width

        elif newDirection == 3:
            if 0 == animal.y_coordinate:
                animal.y_coordinate = self._world.height - 1
            else:
                animal.y_coordinate = animal.y_coordinate - 1

            animal.x_coordinate = (animal.x_coordinate + 1) % self._world.width

        elif newDirection == 4:
            if 0 == animal.y_coordinate:
                animal.y_coordinate = self._world.height - 1
            else:
                animal.y_coordinate = animal.y_coordinate - 1

        elif newDirection == 5:
            if 0 == animal.y_coordinate:
                animal.y_coordinate = self._world.height - 1
            else:
                animal.y_coordinate = animal.y_coordinate - 1
        
            if 0 == animal.x_coordinate:
                animal.x_coordinate = self._world.width - 1
            else:
                animal.x_coordinate = animal.x_coordinate - 1

        elif newDirection == 6:
            if 0 == animal.x_coordinate:
                animal.x_coordinate = self._world.width - 1
            else:
                animal.x_coordinate = animal.x_coordinate - 1

        elif newDirection == 7:
            animal.y_coordinate = (animal.y_coordinate + 1) % self._world.height
            if 0 == animal.x_coordinate:
                animal.x_coordinate = self._world.width - 1
            else:
                animal.x_coordinate = animal.x_coordinate - 1

        #Update the direction and the energy of the animal after the move
        animal.direction = newDirection
        animal.energy -= 1


    def EnergyLevelAction(self, animal):
        if 0 >= animal.energy:
            self._animal_list.remove(animal)
        elif animal.energy >=  self._reproduction_threshold:
            newAnimal = Animal(animal.y_coordinate, animal.x_coordinate, animal.direction, animal.energy/2, animal.chromosome)
            self.RandomMutation(newAnimal.chromosome)
            self._animal_list.append(newAnimal)
            animal.energy /= 2
            self._world.WorldUpdateAnimalNewPos(newAnimal.y_coordinate, newAnimal.x_coordinate)
        else:
            self._world.WorldUpdateAnimalNewPos(animal.y_coordinate, animal.x_coordinate)    
    

    def RandomMutation(self, animal):
        random1 = rand.randint(0,sys.maxsize) % 8
        random2 = rand.randint(0,sys.maxsize) % 3

        if 0 == random2:
            random2 = -1
        elif 1 == random2:
            random2 = 0
        else:
            random2 = 1

        if animal.chromosome[random1] > 1:
            animal.chromosome[random1] += random2


    def Start(self):
    
        self.WorldManagerPrint()
        self.InitWorldWithAnimals()

        for i in range(self._nIterations):
            # Randomly Update food quantity on the world and beauce.
            self._world.WorldUpdateFood()

            print(f"\n*************************[ DAY - {i} - ]**********************\n")
            print("*************[ BEFORE MOVE ]****************\n")
            self._world.PrintWorld()
            print()
            print(self._animal_list)

            for animal in self._animal_list:
                self._world.WorldUpdateAnimalOldPos(animal.y_coordinate, animal.x_coordinate)
                #Choose a gene randomly from the animal.
                randGene = self.GetActivatedGene(animal.chromosome)

                #Move the animal according to the activated gene.
                self.MoveAnimal(animal, randGene)

                #Check if there is food at animal new position.
                if True == self._world.WorldHaveFood(animal.y_coordinate, animal.x_coordinate):
                    #if food, feed the animal and update the food on the world
                    animal.energy += self._energy_gain
                    self._world.WorldReduceFood(animal.y_coordinate, animal.x_coordinate)

                #Analyze energy level and decide if death/reproduce/nothing
                self.EnergyLevelAction(animal)
                

            print("\n***********[ AFTER MOVE ]**************\n")
            self._world.PrintWorld()
            print()
            print(self._animal_list)


    def WorldManagerPrint(self):
        print("\n***********[ SIMULATION PARAMETERS ]************\n");
        print("Iterations:", self._nIterations)
        print("Energy Gain:", self._energy_gain)
        print("Reproduction Threshold:", self._reproduction_threshold)