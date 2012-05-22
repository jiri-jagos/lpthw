#!/usr/bin/python

from sys import argv

import getpass

sScriptName = argv

sUserName = getpass.getuser()

print "I'm %s. Hello, %s" % (sScriptName, sUserName)

