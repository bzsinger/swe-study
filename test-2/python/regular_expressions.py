# regular expressions

import re

# split
s = 'b ab\naab 123'

a = re.split('ab', s)   # ['b ', '\na', ' 123']
                        # treats 'ab' as a delimiter, removes it, gives list of
                        #   text left over

b = re.split('ba', s)   # ['b ab\naab 123']
                        # if text does not appear in string, returned full,
                        #   untouched string

# ^ - start of string character
c = re.split('^b', s)   # ['', ' ab\naab 123']
                        # looking for beginning of string followed by b

r = re.compile('^a', re.M)  # interested in recognizing delineate letter on
                            #   multiple lines
                            # creates pattern object

r.split(s)              # ['b ab\n', 'ab 123']
                        # pattern object's method
                        # uses delineator, settings from compile

# $ - end of string character
re.split('3$', s)       # ['b ab\naab 12', '']
                        # split on '3' followed by end of string

# . - stand-in for any character (not newline)
re.split('.', s)       # ['', '', '', '', '\n', '', '', '', '', '', '', '']

# \d - captures digits
re.split(r'\d', s)     # ['b ab\naab ', '', '', '']

# \D - captures non-digits
re.split(r'\D', s)     # ['', '', '', '', '', '', '', '', '', '123']

# \w - captures any letter or digit
re.split(r'\w', s)     # ['', ' ', '', '\n', '', '', ' ', '', '', '']

# \W - captures any non-alphanumeric character
re.split(r'\W', s)     # ['b', 'ab', 'aab', '123']
