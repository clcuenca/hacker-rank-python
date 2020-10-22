# Hacker Rank - Warmup
# Staircase
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def staircase(number):

    stairs = ""

    for index in range(number):

        for jindex in range(number - index - 1):
            stairs += " "

        for jindex in range(index + 1):
            stairs += "#"

        if index < number - 1: stairs += "\n"

    print(stairs)


# -------
# Program

for line in sys.stdin:

	stripped = int(line.strip())

	staircase(stripped)