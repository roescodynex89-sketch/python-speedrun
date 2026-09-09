range(5)          # 0, 1, 2, 3, 4
range(2, 10)       # 2 to 9
range(0, 10, 2)      # 0, 2, 4, 6, 8 (step)
range(10, 0, -1)      # reverse

# loop control
for i in range(10):
    if i == 3:
        continue    # skips to the next iteration
    if i == 6:
        break        # terminates the loop
    print(i)

# else with loop (a special Python feature, not in JS)
for i in range(5):
    print(i)
else:
    print("Loop finished normally")   # executes if no break occurred

# nested loop
for i in range(3):
    for j in range(3):
        print(i, j)

# enumerate — index + value together
