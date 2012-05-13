#!/usr/bin/python

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (False, True, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"First line",
	"Second one",
	"Third one",
	"Last, the fourth one"
)
print formatter % (
         "text with 'apostrophes'",        "text with 'apostrophes'",        "text with 'apostrophes'",       "text with 'apostrophes'",

)
