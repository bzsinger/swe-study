# regex

# Write a regular expression that can match this following pattern:
# - Each line may start with a lower case letter
# - After which, there will be 1 or more numbers or upper case letters
# - After which, there will be 0 or more of the following pattern: lowercase number lowercase
# - After which, there will be any number of white space (or none at all) followed by a number, uppercase or lowercase letter
# - After which the line has to end with either a caret or a dollar sign

'^[a-z]?[A-Z]+([a-z]\d[a-z])*\s*[\dA-Za-z][\^\$]$'

# Write a regular expression such that all of the following is true:
# a) Abc123GHI has the following groups:
#   0: Abc123GHI
#   1: Abc
#   2: 123
#   3: GHI
# b) Hdf672LKN has the following groups:
#   0: Hdf672LKN
#   1: Hdf
#   2: 672
#   3: LKN
# c) pl743GUH has the following groups:
#   0: pl743GUH
#   1: pl
#   2: 743
#   3: GUH

'([A-Za-z]*)([\d]*)([A-Za-z]*)'
