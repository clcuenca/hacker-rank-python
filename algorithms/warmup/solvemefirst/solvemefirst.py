# Hacker Rank - Warmup
# Solve Me First
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def solveMeFirst(a, b):

	return a + b

# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")

	print(str(solveMeFirst(int(stripped[0]), int(stripped[1]))))