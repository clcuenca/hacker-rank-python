# Hacker Rank - Warmup
# Simple Array Sum
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def simpleArraySum(array):

	sum = 0

	for item in array:

		sum += item

	return sum

# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")

	intArray = [int(number) for number in stripped]

	print(str(simpleArraySum(intArray)))