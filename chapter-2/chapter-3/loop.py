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
