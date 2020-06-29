class Animal:

    """Class representing an animal, characterized by:
    -x coordinate on the world map
    -y coordinate on the world map
    -direction
	-energy level
	-distance from the beauce
	-chromosome set """

    number_of_animals = 0
    
    def __init__(self, x, y, direction, energy, chromosome):
        self._x_coordinate = x
        self._y_coordinate = y
        self._direction = direction
        self._energy = energy
        self._chromosome = chromosome

    def _get_x(self):
        return self._x_coordinate
    def _set_x(self, new_x):
        self._x_coordinate = new_x
    def _get_y(self):
        return self._y_coordinate
    def _set_y(self, new_y):
        self._y_coordinate = new_y
    def _get_direction(self):
        return self._direction
    def _set_direction(self, new_direction):
        self._direction = new_direction
    def _get_energy(self):
        return self._energy
    def _set_energy(self, new_energy):
        self._energy = new_energy
    def _get_chromosome(self):
        return self._chromosome

    x_coordinate = property(_get_x, _set_x)
    y_coordinate = property(_get_y, _set_y)
    direction = property(_get_direction, _set_direction)
    energy = property(_get_energy, _set_energy)
    chromosome = property(_get_chromosome)

    def __repr__(self):
        return "[ ANIMAL STATUS ] \n x: {} |  y: {} \
| Direction: {} | Energy: {} \n Chromosome: {}\n" .format(
self._x_coordinate, self._y_coordinate, self._direction, self._energy, self._chromosome)