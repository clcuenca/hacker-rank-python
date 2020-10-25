# Hacker Rank - Algorithms - Dynamic Programming
# Coin Change
# Author: Carlos L. Cuenca
# Date: 10/25/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def getWays(n, coins):

	coins.append(0)
	coins.sort()

	matrix = []

	for index in range(0, len(coins)):

		row = [0]*(n + 1)

		matrix.append(row)

	for row in range(0, len(matrix)):
		for column in range(0, len(matrix[row])):

			if column == 0: matrix[row][column] = 1

			elif row - 1 >= 0:

				matrix[row][column] = matrix[row - 1][column]

				if column - coins[row] >= 0:

					matrix[row][column] += matrix[row][column - coins[row]]

	return matrix[len(coins) - 1][n]

# -------
# Program

linesRead = 0
number = 0
coins = 0

for line in sys.stdin:

	if linesRead == 0:

		stripped = line.strip().split(" ")

		stripped = [int(number) for number in stripped]

		number = stripped[0]
		coins  = stripped[1]

		linesRead += 1

	elif linesRead == 1:

		coins = line.strip().split(" ")
		coins = [int(number) for number in coins]

		print(getWays(number, coins))

		linesRead = 0