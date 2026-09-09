# Tuple — immutable, faster than list
point = (10, 20, 30)
point.count(10)     # কতবার আছে
point.index(20)     # position

# nested tuple/list
matrix = [(1,2), (3,4), (5,6)]
for a, b in matrix:
    print(a, b)