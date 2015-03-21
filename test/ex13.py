#!/usr/bin/python 
# Filename: ex13.py

from sys import argv

f = raw_input("first: ")
s = raw_input("second: ")
t = raw_input("third: ")


script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third