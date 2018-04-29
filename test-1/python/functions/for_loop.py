# for loop

for v in range(2, 5):   # internally has a try, except
    print(v)            # see ./iterator.py

# -------------------------------------------------------

for v in a:             # a must be iterable
    ...

a = [[1, 2], (1, 2), {1, 2}, {1: "a", 2: "b"}, "12"]
for x, y in a:          # a must be an iterable full of two element items
    ...                 #   ex. (1 , 2) or [1, 2]

for v, _ in a:          # a must be an iterable full of two element items
    ...                 #   ignore the second half of each element

# -------------------------------------------------------

for v in {1, 2}:            # (hash) set - order not guaranteed
    ...                     #   see structures/set.py

for v in {1: "a", 2: "b"}:  # (hash table/) dictionary - order not guaranteed
    ...                     #   iterates through the keys
                            #   see structures/dict.py

# -------------------------------------------------------

for n in range(10):
    if n == 5:
        break
else:                       # only runs if **loop ends normally**
    ...                     #   if break out of loop, **does not** run

                            # use case: only want to run code if you
                            #   **don't** find what you're looking for

# -------------------------------------------------------

# get reference to elements

# for mutables
a = [[2], [3], [4]]
for v in a:
    v += [5]
a == [[2, 5], [3, 5], [4, 5]]

# for immutables
a = [2, 3, 4]
for v in a:
    v += 1
a == [2, 3, 4]
