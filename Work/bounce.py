# bounce.py
#
# Exercise 1.5
"""
A rubber ball is dropped from a height of 100 meters and each time it hits the ground, 
it bounces back up to 3/5 the height it fell. 
Write a program bounce.py that prints a table showing the height of the first 10 bounces.
"""

bounces = 0 #Number of bounces 
height = 100 #Height of the ball in meters 
while bounces < 10: 
    height *= (3/5) 
    bounces += 1
    print(bounces, round(height, 4))
