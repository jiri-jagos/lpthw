#!/usr/bin/python
from sys import argv

script, filename = argv

sText = open(filename)

print "Filename: %s" % filename
print sText.read()
sText.close();

print "Type the filename again (%s):" % filename
filename = raw_input()

print "and again: "
sText = open(filename)

print sText.read()
sText.close()
