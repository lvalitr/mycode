#!/usr/bin/env python3
"""Jurassic Park Trivia | Solution"""

# Question 1
question1 = input("In Jurassic Park, what kind of dinosaur is the star attraction? ")

# Check if the answer is correct (case-insensitive)
if question1.lower() == "t-rex":
    print("Correct! The T-Rex is the star attraction!")
else:
    print("Sorry, that's not correct. The correct answer is T-Rex.")

# Question 2
question2 = input("What type of DNA was used to fill the gaps in the dinosaur genome? ")

# Check if the answer is correct (case-insensitive)
if question2.lower() == "frog":
    print("Correct! Frog DNA was used to fill the gaps in the genome!")
else:
    print("Sorry, that's not correct. The correct answer is Frog.")

