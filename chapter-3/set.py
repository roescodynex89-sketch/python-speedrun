# Set operations
a = {1,2,3}
b = {3,4,5}
a - b            # difference → {1,2}
a.add(10)
a.discard(2)      #It doesn't throw an error when using `remove`, even if the key doesn't exist.