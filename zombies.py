"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
#import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None,
                 zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list is not None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list is not None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def __str__(self):
        ans = poc_grid.Grid.__str__(self)
        ans += "\nHumans:" + str(self._human_list)
        ans += "\nZombies:" + str(self._zombie_list)
        return ans

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        if (row, col) not in self._zombie_list:
            self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        if (row, col) not in self._human_list:
            self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        hgt = self.get_grid_height()
        wdt = self.get_grid_width()
        # visited -grid of the same size, full = visited
        visited = poc_grid.Grid(hgt, wdt)
        # distance field = nested list of the same size, default value = max
        distance_field = [[hgt * wdt for _ in range(wdt)] for _ in range(hgt)]
        # boundary - queue with starting cells
        boundary = poc_queue.Queue()

        if entity_type == ZOMBIE:
            entities = self.zombies
        else:
            entities = self.humans
        # setting up initial boundary, visited and distance field
        for enitity in entities():
            boundary.enqueue(enitity)
        for item in boundary:
            visited.set_full(item[0], item[1])
            distance_field[item[0]][item[1]] = 0

        # for ecah cell in boundary:
        # deque in form boundary, take the dourn neighbours
        # if neighbour os not visited and is not full - add to visited
        # add it to boundary, set the vaule in distance field
        # to +1 from value of curent cell in distance field
        while len(boundary) > 0:
            current_cell = boundary.dequeue()
            for neighbour in self.four_neighbors(current_cell[0],
                                                 current_cell[1]):
                if (visited.is_empty(neighbour[0], neighbour[1]) and
                        self.is_empty(neighbour[0], neighbour[1])):

                    visited.set_full(neighbour[0], neighbour[1])
                    boundary.enqueue(neighbour)
                    c_value = distance_field[current_cell[0]][current_cell[1]]
                    distance_field[neighbour[0]][neighbour[1]] = c_value + 1
        return distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        # finiding the max of 8 neighbours and itself
        for idx in range(self.num_humans()):
            hooman = self._human_list[idx]
            neighbours = self.eight_neighbors(hooman[0], hooman[1])
            max_nei = [[zombie_distance_field[nei[0]][nei[1]], nei]
                       for nei in neighbours
                       if self.is_empty(nei[0], nei[1])]
            max_nei = max([[0, hooman]] + max_nei)
            max_nei = max_nei[1]
            self._human_list[idx] = max_nei

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        # finiding the min of 4 neighbours and itself
        for idx in range(self.num_zombies()):
            zombie = self._zombie_list[idx]
            if human_distance_field[zombie[0]][zombie[1]] != 0:
                neighbours = self.four_neighbors(zombie[0], zombie[1])
                min_nei = [[human_distance_field[nei[0]][nei[1]], nei]
                           for nei in neighbours
                           if self.is_empty(nei[0], nei[1])]

                min_nei = [[self.get_grid_height() * self.get_grid_width(),
                            zombie]] + min_nei
                print min_nei
                min_nei = min(min_nei)
                min_nei = min_nei[1]
                self._zombie_list[idx] = min_nei


# poc_zombie_gui.run_gui(Apocalypse(30, 40))
