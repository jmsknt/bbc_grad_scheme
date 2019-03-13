GAME OF LIFE
=========================

*Run with "python game_of_life.py", if you want to run the test case, change "test" to True in the main arguments*

*Requires numpy and matplotlib - written in Python 3.7.0*

Implements an infinite universe with initially random cells that live or die depending on the rules of The Game of Life, within a set amount of time.

ASSUMPTIONS:
* "Infinite" means that the grid representing the universe wraps around on itself, such that the rightmost neighbour to a cell at the limit of X is simply the first cell on that row.
* The initial state is random (or random enough for this exercise).
* The game plays out for a specified time.

My solution:
* Seed the universe
* Iterate over every cell
    * Check the cell's number of neighbours
    * Apply the rules of life to the cell
* Update the universe's cells with the new values
* Repeat to time limit or until the universe dies


(Originally uploaded as my solution for the BBC Software Engineering Grad Scheme coding assignment).
