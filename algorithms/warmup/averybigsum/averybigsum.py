# Hacker Rank - Warmup
# A Very Big Sum
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def aVeryBigSum(array):

	returnSum = 0

	for number in array:

		returnSum += number

	return returnSum

# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")

	array = [int(number) for number in stripped]

	print(str(aVeryBigSum(array)))