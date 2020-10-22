# Hacker Rank - Warmup
# Compare Triplets
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def compareTriplets(alice, bob):

	aliceSum = 0
	bobSum = 0

	for index in range(3):

		if alice[index] > bob[index]:

			aliceSum += 1

		if alice[index] < bob[index]:

			bobSum += 1

	return [aliceSum, bobSum]

# -------
# Program

count = 0
alice = None
bob   = None

for line in sys.stdin:

	stripped = line.strip().split(" ")

	if count == 0:

		alice = [int(number) for number in stripped]
		count += 1

	elif count == 1:

		bob = [int(number) for number in stripped]

		count = 0

		print(str(compareTriplets(alice, bob)))

	
