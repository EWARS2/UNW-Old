# Title: Hot Dog Cookout Calculator
# Chapter 3, Exercise 8
# Starting Out With Python, 5th Edition
# Date: 2/7/2024
# Author: Ethan Reed
# Class: Python Programming I
# Professor James Smith

# Declare constants
DOG_PACK_CONTAINS = 10
BUN_PACK_CONTAINS = 8

# Get input and convert it accordingly
headcount = int(round(float(input("How many people? :"))))
perPerson = int(round(float(input("How many hot dogs per person? :"))))

# Calculate diggity-dogs needed
needed = headcount * perPerson

# Calculate # of packages needed
# & remainders
dogPacks   = needed // DOG_PACK_CONTAINS
dogsRemain = needed %  DOG_PACK_CONTAINS
bunPacks   = needed // BUN_PACK_CONTAINS
bunsRemain = needed %  BUN_PACK_CONTAINS

# Round up Hot Dog Packets
if ( dogsRemain <= ( DOG_PACK_CONTAINS / 2 )) and not dogsRemain==0:
    dogPacks = dogPacks + 1

# Round up Hot Dog Bun Packs
if ( bunsRemain <= ( BUN_PACK_CONTAINS / 2 ) ) and not bunsRemain==0:
    bunPacks = bunPacks + 1

# Display results
print (f"You will need {needed} total Hot Dogs.")
print (f"This is {dogPacks} packs of {DOG_PACK_CONTAINS} hot dogs,")
print (f"and {bunPacks} packs of {BUN_PACK_CONTAINS} hot dog buns.")
print (f"\nYou will have {dogsRemain} hot dogs and {bunsRemain} buns spare.")

