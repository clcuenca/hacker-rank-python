# Hacker Rank - Warmup
# Mini Max Sum
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def miniMaxSum(array):

    choose = 4

    minSum = 9999999999
    maxSum = -9999999999

    combinations = [0]*(choose + 2)

    # Clear the combinations array
    for j in range(choose):
        combinations[j] = j

    # Assign the sentinels
    combinations[choose] = len(array)
    combinations[choose + 1] = 0

    j = 0

    while j < choose:

        currentSum = 0
        # Visit the combination
        for index in range(choose):
            currentSum += array[combinations[index]]

        if currentSum < minSum: minSum = currentSum
        if currentSum > maxSum: maxSum = currentSum
        
        # Find J
        j = 0

        while combinations[j] + 1 == combinations[j + 1]:
        
            combinations[j] = j

            j += 1

        combinations[j] += 1

    print(str(minSum) + " " + str(maxSum))

# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")
	array = [int(number) for number in stripped]

	miniMaxSum(array)