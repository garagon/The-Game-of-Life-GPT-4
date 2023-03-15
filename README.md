# The Game of Life GPT-4

This project is an implementation of the cellular automaton known as John Conway's "Game of Life" using Python and Pygame.

## Requirements
Python 3.x
Pygame

##Installation
To install the dependencies, run the following command in your terminal:

`pip install pygame`

## Execution
To run the program, simply execute the following command in your terminal:

`python game_of_life.py`

## Usage

The Game of Life starts with a random initial set of living and dead cells on a grid. Cells evolve over time following simple rules:

- A living cell with fewer than two living neighbors dies (underpopulation).
- A living cell with two or three living neighbors survives.
- A living cell with more than three living neighbors dies (overpopulation).
- A dead cell with exactly three living neighbors becomes a living cell (reproduction).


## Controls
- Click on the "Pause" button (top right corner) or press the "Space" key to pause or resume the simulation.
- Press the "Escape" key to exit the program.


Credits
Created by Gus Aragón with the help of OpenAI's AI.
