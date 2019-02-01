My solution for the BBC Software Engineering Grad Scheme coding assignment.
=========================

*Run with "python game_of_life.py"*

Requires numpy and matplotlib

Implements an infinite universe with initially random cells that live or die depending on the rules of The Game of Life, within a set amount of time.

ASSUMPTIONS:
* "Infinite" means that the grid representing the universe wraps around on itself, such that the rightmost neighbour to a cell at the limit of X is simply the first cell on that row.
* The initial state is random (or random enough for this exercise).
* The game plays out for a specified time.
