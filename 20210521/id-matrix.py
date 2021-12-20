# Created 21.5.2021
# Challenge from https://edabit.com/challenge/QN4RMpAnktNvMCWwg
# Identity Matrix

# Explanation:
# Create a function that takes an integer n and returns the identity matrix of n x n dimensions.
# For this challenge, if the integer is negative, 
# return the mirror image of the identity matrix of n x n dimensions.. 
# It does not matter if the mirror image is left-right or top-bottom.
# Incompatible types passed as n should return the string "Error".



def id_mtrx(n: int) -> int:
    matrix = []

    if (type(n) == int):
        for i in range(abs(n)):
            row = []

            for j in range (abs(n)):
                if (j == i):
                    row.append(1)
                else:
                    row.append(0)

            matrix.append(row)

        if (n < 0):
            return matrix [::-1]  # mirroring
        
        return matrix

    else:
        return False



# Testing
print(id_mtrx(0)) # -> []
print(id_mtrx(2)) # -> [[1, 0], [0, 1]]
print(id_mtrx(-2)) # -> [[0, 1], [1, 0]]
print(id_mtrx(4)) # -> [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
print(id_mtrx("invalid input")) # -> False
print(id_mtrx(True)) # -> False