import numpy as np
from itertools import product

def get_vis(puz):
    """
    Determine which numbers are visible 
    """
    vis = puz[-1,:,:]
    for i in range(1,puz.shape[0]):
        mask = vis==0
        vis[mask] = puz[-1-i,mask]
    return vis

def evaluate(puz):
    """
    Compute the column sums for a puzzle in it's current configuration
    """
    vis = get_vis(puz)
    return np.sum(vis,axis=0)

def rotate_puzzle(puz, state):
    """
    Create and return a copy of the puzzle given the rotation state
    """
    assert len(state) == puz.shape[0]-1

    stated_puz = puz.copy()
    for layer,offset in enumerate(state):
        stated_puz[layer,:,:] = np.roll(stated_puz[layer,:,:], offset, axis=1)
    return stated_puz
    

# Define Puzzle
puzzle = [[[7,8,8,3,4,12,2,5,10,7,16,8],
           [9,9,4,4,6,6,3,3,14,14,21,21],
           [14,15,4,5,6,7,8,9,10,11,12,13],
           [11,14,11,11,14,11,14,11,14,14,11,14]],
          [[1,0,9,0,12,0,6,0,10,0,10,0],
           [3,26,6,0,2,13,9,0,17,19,3,12],
           [9,20,12,3,6,0,14,12,3,8,9,0],
           [7,0,9,0,7,14,11,0,8,0,16,2]],
          [[0,0,0,0,0,0,0,0,0,0,0,0],
           [22,0,16,0,9,0,5,0,10,0,8,0],
           [11,26,14,1,12,0,21,6,15,4,9,18],
           [17,4,5,0,7,8,9,13,9,7,13,21]],
          [[0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0],
           [0,14,0,9,0,12,0,4,0,7,15,0],
           [11,11,6,11,0,6,17,7,3,0,6,0]],
          [[0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0],
           [3,0,6,0,10,0,7,0,15,0,8,0]]]
puzzle = np.array(puzzle)

# Solve puzzle by brute-force trying every possible state
num_layers,num_rows,num_columns = puzzle.shape
possible_states = product(range(num_columns), repeat=num_layers-1)
for s in possible_states:
    stated_puzzle = rotate_puzzle(puzzle, s)
    sums = evaluate(stated_puzzle)
    if np.all(sums==42):
        print(get_vis(stated_puzzle))
