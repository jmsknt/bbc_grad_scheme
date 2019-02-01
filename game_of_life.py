import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def seed_universe(N):
    '''
    Seed N*N universe with random cells.
    A cell has 5% of being alive upon creation.

    params: the 'limit' to the universe grid (N)
    returns: a seeded universe as a 2D array
    '''
    return np.random.choice([1, 0], N*N, p=[0.20, 0.80]).reshape(N, N)

def check_neighbours(universe, N, i, j):
    '''
    Check over the 8 neighbours of a cell (i,j).
    To make the universe effectively infinite,
    we check for a "wraparound" when the cell is
    at the edge of the stored grid.

    params: the universe, its limit (N) and a cell position (i,j)
    returns: the total number of neighbours for cell (i,j)
    '''

    # number of neighbours
    total = 0

    # the neighbours from left to right
    for x in [i-1, i, i+1]:
        # the neighbours from top to bottom
        for y in [j-1, j, j+1]:
            # we don't want to check the cell itself
            if (x == i and y == j):
                continue
            # add a cell's value to the toal (it's either 0 or 1)
            if (x != N and y != N):
                total += universe[x,y]
            # account for if the cell is at the nth x value
            elif (x == N and y != N):
                total += universe[0,y]
            # account for if the cell is at the nth y value
            elif (x != N and y != N):
                total += universe[x,0]
            # account for if the cell is at (n,n) (lower right)
            elif (x == N and y == N):
                total += universe[0,0]
    return total

def life(universe,N):
    '''
    Apply the rules of the game such that
    a cell either propagates or dies.

    params: the universe, and its limit (N)
    returns: the updated universe
    '''
    new_universe = np.copy(universe)

    for i in range(N):
        for j in range(N):
            neighbours = check_neighbours(universe, N, i, j)
            # less than 2 or more than 3
            if universe[i,j] == 1:
                # this covers underpopulation and overcrowding
                if not 2 <= neighbours <= 3:
                    new_universe[i,j] = 0
                # this covers survival
                else:
                    new_universe[i,j] = 1
            # this covers creation of life when cells has exactly 3 neighbours
            elif universe[i,j] == 0 and neighbours == 3:
                new_universe[i,j] = 1
    return new_universe

def main(N,T):
    '''
    Play the rule of life for all cells,
    updating the universe on each iteration.

    params: boundary to the universe (N), time limit (T)
    '''
    t = 0 # initialise time step
    universe = seed_universe(N) # seed a random N*N universe

    fig = plt.figure()

    # each time step should be captured as a frame
    frames = []

    print("working...")
    while t <= T: # play the game of life for time T

        # capture plot of universe's current state as a frame
        frames.append((plt.imshow(universe),))

        # scenario 0
        if np.all(universe==0):
            pass
        # other scenarios
        else:
            universe = life(universe,N) # universe becomes the updated universe

        t += 1 # next time steps

        if t == T:
            print("...done!")

    # animate the resulting universe's evolution
    # matplotlib's ArtistAnimation function is the easiest way to do this
    anim = animation.ArtistAnimation(fig, frames, interval=100, repeat=False, blit = "True")
    plt.show()

if __name__ == '__main__':
    main(50,200)
