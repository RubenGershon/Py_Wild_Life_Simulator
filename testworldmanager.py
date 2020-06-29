import unittest
from animal import Animal
from world import World
from worldmanager import WorldManager

class TestWorldManager(unittest.TestCase):

    def test_1(self):
        a1 = Animal(0,0,0,5,[1,2,3,4,5,6,7,8])
        a2 = Animal(0,0,0,5,[1,2,3,4,5,6,7,8])
        animal_list = [a1, a2]
        newWorld = World(10,10,2,2,1,1)
        wmanager = WorldManager(newWorld, animal_list, 2, 0, 10)
        wmanager.Start()

if __name__ == '__main__':
    unittest.main()        

#if height > 0 and width > 0 and height >= beauce_height and \
        #width >= beauce_width and height >= beauce_first_cell_height and \
        #width >= beauce_first_cell_width: