# Hacker Rank - Warmup
# 
# Author: Carlos L. Cuenca
# Date:

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def plusMinus(array):

	positive = 0
	negative = 0
	zero     = 0

	for number in array:

		if number < 0:

			negative += 1

		elif number > 0:

			positive += 1

		else:

			zero += 1

	print(str('%.6f'%(positive / len(array))))
	print(str('%.6f'%(negative / len(array))))
	print(str('%.6f'%(zero     / len(array))))


# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")

	array = [int(number) for number in stripped]

	plusMinus(array)