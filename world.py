import sys
import numpy as np
import random as rand
from pair import Pair
from termcolor import colored


class World:

    """Class representing a world, characterized by:
    - world - BiDimentional matrix of Pairs
	- height of the matrix
	- width of the matrix
	- height of the beauce
	- width of the beauce
	- beauce_first_cell_height
	- beauce_first_cell_width"""

    def __init__(self, height, width, beauce_height, beauce_width,
                            beauce_pos_height, beauce_pos_width):
              
        self._world = np.ndarray((height, width), dtype = Pair)
        self._height = height
        self._width = width
        self._beauce_height = 0
        self._beauce_width = 0
        self._is_beauce = False
        for h in range(self._height):
            for w in range(self._width):
                self._world[h,w] = Pair()
                
        if beauce_height > 0 and beauce_width > 0 and \
            beauce_pos_height > 0 and beauce_pos_width > 0:
            self._is_beauce = True
            self._beauce_height = beauce_height
            self._beauce_width = beauce_width
            self._beauce_pos_height = beauce_pos_height
            self._beauce_pos_width = beauce_pos_width
            self._b_height_max = beauce_pos_height + beauce_height - 1
            self._b_width_max = beauce_pos_width + beauce_width - 1

    def _get_height(self):
        return self._height
    def _get_width(self):
        return self._width
    def _get_beauce_height(self):
        return self._beauce_height
    def _get_beauce_width(self):
        return self._beauce_width
    def _get_beauce_first_cell_height(self):
        return self._beauce_pos_height
    def _get_beauce_first_cell_width(self):
        return self._beauce_pos_width

    height = property(_get_height)
    width = property(_get_width)
    beauce_height = property(_get_beauce_height)
    beauce_width = property(_get_beauce_width)
    beauce_pos_height = property(_get_beauce_first_cell_height)
    beauce_pos_width = property(_get_beauce_first_cell_width)

    #Function that randomly update the food on the map
    def WorldUpdateFood(self):
        randHeight = rand.randint(0,sys.maxsize) % self.height
        randWidth = rand.randint(0,sys.maxsize) % self.width
        #Add food randomly in the world
        (self._world[randHeight, randWidth])._value += 1
        (self._world[randHeight, randWidth])._type = "FOOD"

        #Check if Beauce Exist
        if (self._is_beauce):
            randHeight = (rand.randint(0,sys.maxsize) % (self._b_height_max - self.beauce_pos_height + 1)) + self.beauce_pos_height
            randWidth = (rand.randint(0,sys.maxsize) % (self._b_width_max - self.beauce_pos_width + 1)) + self.beauce_pos_width
		    #Add food randomly in the Beauce
            (self._world[randHeight % self.height, randWidth % self.width])._value += 1
            (self._world[randHeight, randWidth])._type = "FOOD"

    def WorldHaveFood(self, y, x):
	    return 0 != (self._world[y,x])._value and (self._world[y,x])._type == "FOOD" 

    def WorldReduceFood(self, y, x):
    	(self._world[y,x])._value -= 1

    def WorldUpdateAnimalOldPos(self, y, x):
        if (self._world[y,x])._value == 0:
            (self._world[y,x])._type = "EMPTY"
        else:
             (self._world[y,x])._type = "FOOD"   


    def WorldUpdateAnimalNewPos(self, y, x):
        	(self._world[y,x])._type = "ANIMAL"            

    def WorldIsInBeauce(self, x, y):
        return self._is_beauce and x >=  self.beauce_pos_width \
        and x <= self._b_width_max and  y >= self.beauce_pos_height \
        and y <= self._b_height_max    


    def PrintWorld(self):
        for h in range(self._height):
            for w in range(self._width):
                if not self.WorldIsInBeauce(h,w):
                    if (self._world[h,w])._type != "ANIMAL":
                        print(colored( (self._world[h,w])._value,'grey', 'on_yellow'), end = '')
                    else:
                        print(colored( (self._world[h,w])._value, 'red', 'on_yellow'), end = '')
                    print(colored(" ", 'yellow', 'on_yellow'), end = '') 
                else:
                    if (self._world[h,w])._type != "ANIMAL":
                        print(colored( (self._world[h,w])._value, 'grey', 'on_green'), end = '')
                    else:
                        print(colored( (self._world[h,w])._value, 'red', 'on_green'), end = '')
                    print(colored(" ", 'green', 'on_green'), end = '') 


            print()     