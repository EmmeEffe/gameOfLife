# Game of Life

This project is an implementation of Conway's Game of Life.

## Description

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

## Rules

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Installation

To install the project, just clone the repository and navigate to the project directory:

## Usage

To run the Game of Life, execute the following command:

```bash
python gameOfLife.py
```
or

```bash
python gameOfLife.py --size 100 --seed 10 --mutation_rate 0.001 --fps 100
```

where:
- `size` is the size of the grid
- `seed` is the seed for random initialization
- `mutation_rate` is the mutation rate. Every pixel has a probability of `mutation_rate` to change its state
- `fps` is the number of epochs per second

To mutate the population just click 'm' on the keyboard.

To quit the game just click 'q' on the keyboard.