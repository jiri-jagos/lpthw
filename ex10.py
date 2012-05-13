#!/usr/bin/python
sTab = "\tThere's a tab on the beginning of the line.\n"

sSplit = "There's a newline escape sequence \n before this one."

sBackslash = " Here're \\ some backslashes here \\."

sFat = """This is pretty list: \n
\t* item 1
\t* item 2
\t* item 3
"""

sEscapedQuote = "this is string with \" escaped quote."

sEscapedApostrophe = 'this is string with \' escaped apostrophe.'

sOne = '''
This\'s
triple
apostrophe
""
'''

print sTab
print sSplit
print sBackslash
print sFat
print sOne

print "Formated quote escaped: %r" % sEscapedQuote
print "Formated apostrophe escaped: %r" % sEscapedApostrophe
