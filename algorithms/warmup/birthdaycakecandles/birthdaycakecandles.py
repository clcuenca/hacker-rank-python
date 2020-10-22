# Hacker Rank - Warmup
# Birthday Cake Candles
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def birthdayCakeCandles(candles):

	tallestCount  = 0
	tallestCandle = -999999999

	for candle in candles:

		if candle > tallestCandle:

			tallestCandle = candle

			tallestCount = 1

		elif candle == tallestCandle: tallestCount += 1

	return tallestCount


# -------
# Program

for line in sys.stdin:

	stripped = line.strip().split(" ")
	candles = [int(number) for number in stripped]

	print(str(birthdayCakeCandles(candles)))