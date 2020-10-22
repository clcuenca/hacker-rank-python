# Hacker Rank - Warmup
# Time Conversion
# Author: Carlos L. Cuenca
# Date: 10/21/2020

# -------
# Imports

import sys

# ------------------------
# Function Implementations

def timeConversion(time):

	hours   = int(time[0] + time[1])
	minutes = int(time[3] + time[4])
	seconds = int(time[6] + time[7])

	timePeriod = time[8] + time[9]

	newTime = ""

	hours = hours % 12

	if timePeriod == "PM": hours += 12

	if hours < 10: newTime += ("0" + str(hours))

	else: newTime += str(hours)

	newTime += ":"

	if minutes < 10: newTime += ("0" + str(minutes))

	else: newTime += str(minutes)

	newTime += ":"

	if seconds < 10: newTime += ("0" + str(seconds))

	else: newTime += str(seconds)

	return newTime

# -------
# Program

for line in sys.stdin:

	stripped = line.strip()

	print(str(timeConversion(stripped)))