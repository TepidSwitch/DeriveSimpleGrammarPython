#! /usr/bin/python3

# Written by Stanislav Schaller, 2/20/2016
import sys
import argparse
import string
import copy

# Input
strLength = input('Enter maximum string length: ')
if (strLength.isdigit()==False):
	strLength = 3
else:
	strLength = int(strLength)
filename = input('Enter the grammar filename: ')

# Process
data = []
productions = {}

for line in open(filename, "r"):
	data.append(line.split())

# Dictionary 
for entry in data:
	key = entry[0]
	value = ''

	# Check to see if I need to mash together more than one character
	if (len(entry) > 3):
		almost = len(entry) - 1
		for x in entry[2:almost]:
			value += str(x) + ' '
		value += str(entry[almost])
	else:
		value += str(entry[2])

	if key not in productions:
		productions[key] = []
		productions[key].append(value)
	else:
		productions[key].append(value)

# Worklist
wlist = [data[0][0]]
known = []

while (wlist):
	sentence = wlist.pop().split()
	terminals = 0
	if (len(sentence) <= strLength):
		# Check number of terminals in sentence
		for term in sentence:
			if term not in productions:
				terminals += 1
		# Check if the entire sentence is terminals or not
		if (terminals == len(sentence)):
			output = ' '.join(sentence)
			if (output not in known):
				print(output)
				known.append(output)
		# Otherwise it's chugging time!
		else:
			for index in range(0, len(sentence)):
				if sentence[index] in productions:
					tmp = copy.copy(sentence)
					for prod in productions[sentence[index]]:
						tmp[index] = prod
						wlist.append(' '.join(tmp))