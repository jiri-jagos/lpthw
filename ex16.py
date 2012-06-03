#!/usr/bin/python
from sys import argv

script, sFilename = argv

print "We're gonna erase %r" % sFilename
print "Press <Enter> to confirm, <Ctrl> + C to abort"

raw_input("?")

print "Opening the file %r." % sFilename
oFile = open(sFilename, 'w')

print "Truncating the file. Say bye to its content."
oFile.truncate()

print "Now you can insert 3 lines of text:"
sLine1 = raw_input("line 1:\n")
sLine2 = raw_input("line 2:\n")
sLine3 = raw_input("line 3:\n")

print "Now i'll write these lines into the file"

# lines have to be converted to string before writing into the file
sContent = "%s\n%s\n%s\n" % (sLine1, sLine2, sLine3)

oFile.write(sContent)
oFile.close

oFile = open(sFilename)

print "File content is now:\n %s" % oFile.read()

print "Now we can close the file"
oFile.close()
