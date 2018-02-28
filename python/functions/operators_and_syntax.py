# a line comment
"""
a block comment
"""

# -------------------------------------------------------

# / true division, always returns a float
5 / 2 == 2.5

# // floor division, returns type of input
5 / 2 == 2
5.0 / 2 == 2.0

# -------------------------------------------------------

# bit shift operators
1 << 1 # left shift - multiplies by a power of two
2 >> 1 # right shift - divides by a power of two

# -------------------------------------------------------

# string operators
"abc" == "abc" # True
"abc" <  "bc"  # True - lexographical order
"bc"  >  "abc"

strcmp("", "") == 0
strcmp("abc", "ab") > 0
strcmp("ab", "abc") < 0

# string - immutable
s = "abc"
s[1] == "a"    # True
# s[1] = "d"   # **does not** work

# -------------------------------------------------------

#default constructors and values
b = bool()
b == False

i = int()
i == 0

f = float()
f == 0.0

c = complex()
c = 0 + 0j

# -------------------------------------------------------

# len(...)
# len(<sequence or mapping>)

len("abc")                    # 3 (string)
len([2, 3, 4])                # 3 (list)
len((2, ))                    # 1 (tuple)
len({2, 3, 4})                # 3 (set)
len({2: "a", 3: "b", 4: "c"}) # 3 (dictionary)

# -------------------------------------------------------

# ** exponentiation

2 ** 3 == 8

# -------------------------------------------------------

# parallel assignment
i, j = 2, 3
i == 2
j == 3

i, j = j, i
i == 3
j == 2

# -------------------------------------------------------

# multiple comparison and assignment
a = b = c = 3
a == 3
b == 3
c == 3

a == b == c == 3    # True

a = 1
b = 2
c = 3
a < b < c           # True
