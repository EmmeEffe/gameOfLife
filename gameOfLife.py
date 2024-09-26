'''
Game of Life
Rules:
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
Author: Martino Falorni
'''

import numpy as np
import time
import cv2
import argparse

class GameOfLife:
    def __init__(self, size, seed, mutation_rate):
        self.size = size
        self.square_size = 5
        self.grid = np.zeros((size, size), dtype=int)
        self.random_initialize(seed)
        self.mutation_rate = mutation_rate

        # Conditions
        self.DEAD = 0 # DO NOT CHANGE, dead is 0, other is >0
        self.ALIVE = 1

    def random_initialize(self, seed=None):
        if seed is not None:
            np.random.seed(seed)
        self.grid = np.random.randint(2, size=(self.size, self.size))

    def render(self):
        img = np.zeros((self.size*self.square_size, self.size*self.square_size, 3), dtype=np.uint8)
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i, j] == self.ALIVE:
                    img[i*self.square_size:(i+1)*self.square_size, j*self.square_size:(j+1)*self.square_size] = (255, 255, 255)
        cv2.imshow('frame', img)

    def count_live_neighbours(self, x, y):
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < self.size and j >= 0 and j < self.size:
                    if i != x or j != y:
                        count += self.grid[i, j]
        return count

    def mutate(self):
        for i in range(self.size):
            for j in range(self.size):
                if np.random.rand() < self.mutation_rate:
                    self.grid[i, j] = 1 - self.grid[i, j] # Toggle the value

    def update_pixel(self, x, y):
        '''
            Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            Any live cell with two or three live neighbours lives on to the next generation.
            Any live cell with more than three live neighbours dies, as if by overpopulation.
            Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        '''
        neighbours = self.count_live_neighbours(x, y)
        if self.grid[x, y] == self.DEAD:
            if neighbours == 3:
                return self.ALIVE   # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        else:
            if neighbours < 2 or neighbours > 3:
                return self.DEAD    # Any live cell with fewer than two or more than three live neighbours dies.
            else:
                return self.ALIVE   # Any live cell with two or three live neighbours lives on to the next generation.
        return self.grid[x, y]

    def update(self):
        new_matrix = np.zeros((self.size, self.size), dtype=int)
        for i in range(self.size):
            for j in range(self.size):
                new_matrix[i, j] = self.update_pixel(i, j)
        self.grid = new_matrix
        self.render()

# Parse command line arguments
parser = argparse.ArgumentParser(description='Game of Life')
parser.add_argument('--size', type=int, default=100, help='Size of the grid')
parser.add_argument('--seed', type=int, default=10, help='Seed for random initialization')
parser.add_argument('--mutation_rate', type=float, default=0.001, help='Mutation rate')
parser.add_argument('--fps', type=float, default=100, help='Epochs per second')
args = parser.parse_args()

refresh_period_ms = int(round(1000/args.fps))

# Initialize the game with the provided parameters
gameOfLife = GameOfLife(args.size, args.seed, args.mutation_rate)
gameOfLife.render()
while True:
    gameOfLife.update()
    char = cv2.waitKey(refresh_period_ms)
    if char == ord('q'):
        break
    if char == ord('m'):
        gameOfLife.mutate()

cv2.destroyAllWindows()
