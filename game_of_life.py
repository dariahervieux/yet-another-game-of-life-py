# arrays library - https://docs.scipy.org/doc/numpy/user/basics.creation.html
import numpy as np

#Cell class - a unit of a world. Rules implementation
class Cell(object):
    #returns a tuple (sequence of immutable objects): 0 element - neighbours start coord, 1 element - end coord
    @staticmethod
    def get_neighbours_start_end(n, elements_number):
        return (max (n-1, 0), min (n+2, elements_number))

    @staticmethod
    def get_alive_neighbours_number(x, y, world):
        x_start_end = Cell.get_neighbours_start_end(x,  world.shape[0])
        y_start_end =  Cell.get_neighbours_start_end(y,  world.shape[1])
        return np.sum(world[x_start_end[0]:x_start_end[1],
                            y_start_end[0]:y_start_end[1]]) - world[x, y]

    @staticmethod
    def get_next_state(x, y, world):
        alive_neighbours = Cell.get_alive_neighbours_number(x, y, world)
        #Any live cell with fewer than two live neighbours dies
        #Any live cell with more than three live neighbours dies
        if(world[x, y] and (2 > alive_neighbours or alive_neighbours > 3)) :
            return 0
          
        #Any dead cell with exactly three live neighbours becomes a live cell
        if (not world[x,y] and alive_neighbours == 3) :
            return 1

        #Any live cell with two or three live neighbours lives on to the next generation
        # If no rule applies - no change
        return world[x,y]

# World class to handle 2D space description of all cells
class World(object):    
    def __init__(self, dim_x, dim_y, seed = None, seed_pos_x = 0, seed_pos_y = 0):
        self.world = np.zeros((dim_x, dim_y), dtype=int)
        #integrate seed into the world matrix
        if seed is not None:
            array_seed = np.array(seed)
            seed_x_end = seed_pos_x + array_seed.shape[0]
            seed_y_end = seed_pos_y + array_seed.shape[1]            
            if seed_x_end > dim_x or seed_y_end > dim_y:
                print('seed_x_end %d, seed_y_end %d' %  (seed_x_end, seed_y_end))
                raise ValueError("Incompatible dimensions") 
            self.world[seed_pos_x:seed_x_end, seed_pos_y:seed_y_end] = array_seed

    def next(self):
        next_world = np.copy(self.world)
        for i in range(self.world.shape[0]):
            for j in range(self.world.shape[1]):
                next_world[i,j] = Cell.get_next_state(i,j, self.world)
        self.world = next_world
        return next_world

    def let_it_live(self, cycles_number):
        print('\n')
        for _ in range(cycles_number):            
            print(self.next())
            print('\n')
        return self.world


    

 


