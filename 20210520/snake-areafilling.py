# Created 20.5.2021
# Challenge from https://edabit.com/challenge/Y5Ji2HDnQTX7MxeHt
# The Snake — Area Filling

# Explanation:
# This challenge is based on the classic videogame "Snake".

# Assume the game screen is an n * n square, and the snake starts the game with length 1 positioned on the top left corner.
# In this version of the game, the length of the snake doubles each time it eats food 
# (e.g. if the length is 4, after eating it becomes 8).
# Create a function that takes the side n of the game screen 
# and returns the number of times the snake can eat before it runs out of space in the game screen.


def snakefill(rows: int):
    # square matrix ->  colums == rows
    grid = rows ** 2
    n = 0

    # doubling sequense 2^n = 1, 2, 4, 8, 16... represents the growing process
    while (pow(2,n) <= grid):
        if (pow(2, n) == grid):
            return n
        n += 1

    return n - 1


# Test the results
print(snakefill(3)) # -> 3
print(snakefill(6)) # -> 5
print(snakefill(24)) # -> 9
print(snakefill(37)) # -> 10
print(snakefill(70)) # -> 12