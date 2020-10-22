# Hacker Rank - Warmup
# Diagonal Difference
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def diagonalDifference(matrix):
	
	leftDiagonal  = 0
	rightDiagonal = 0

	for index in range(len(matrix)):
		leftDiagonal += matrix[index][index]

	for index in range(len(matrix)):
		rightDiagonal += matrix[index][len(matrix) - index - 1]

	return abs(leftDiagonal - rightDiagonal)

# -------
# Program

linesRead = 0
number = 0
matrix = None

for line in sys.stdin:

	if linesRead == 0:

		number = int(line.strip())

		linesRead += 1
		matrix = []
	
	elif linesRead > 0 and linesRead <= number:

		stripped = line.strip().split(" ")
		matrix.append([int(item) for item in stripped])

		linesRead += 1

	if linesRead == number + 1:

		print(str(diagonalDifference(matrix)))

		linesRead = 0



