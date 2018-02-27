# dict

# Hash Table
# key-value pairs
# look-up, removal, and add - const. time
d = {2: "abc", 3: "def", 4: "ghi"}
d[2] = "def"        # keys cannot be duplicated or modified in place
d                   # {2: "def", 3: "def", 4: "ghi"}

# -------------------------------------------------------

d = {2: "abc", 3: "def", 4: "ghi"}
k1 = d.keys()               # not an iterator, but iterable
k2 = d.keys()
k1 is k2                    # False - different objects

set(k1) == {2, 3, 4}

d[5] = "jkl"
set(k1) == {2, 3, 4, 5}     # lazy operation, k1 does not store/copy keys
                            #   when created
                            # does not exhaust k1
set(k1) == {2, 3, 4, 5}

# -------------------------------------------------------

d = {2: "abc", 3: "def", 4: "ghi"}
a = d.items()                                   # tuple of key, value pairs
list(a) == [(2, "abc"), (3, "def"), (4, "ghi")]
list(a) == [(2, "abc"), (3, "def"), (4, "ghi")] # does not get exhausted
