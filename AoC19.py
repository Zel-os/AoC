import math

num = 3004953
elves = [i for i in range(1, num+1)]
while len(elves) > 1:
    nextround = [elves[i] for i in range(0, len(elves), 2)]
    if len(elves) % 2 == 1:
        del nextround[0]
    elves = nextround
print(elves)

x = pow(3, int(math.log(num, 3)))
y = num - x
if y > x:
    y = ((y - x) * 2) + x
print(y)

