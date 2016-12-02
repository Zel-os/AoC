inputdata = open("input.txt")
print("Part 1:")
for line in inputdata:
    button = 5
    for cmd in line.strip():
        if cmd == "U" and button > 3:
            button -= 3
        elif cmd == "D" and button < 7:
            button += 3
        elif cmd == "L" and button % 3 != 1:
            button -= 1
        elif cmd == "R" and button % 3 != 0:
            button += 1
    print(button, end="")

print("\nPart 2:")
inputdata.seek(0)
dirmap = {'U':0, 'D':1, 'L':2, 'R':3}
keymap = {'1':['1','3','1','1'], '2':['2','6','2','3'], '3':['1','7','2','4'], '4':['4','C','3','4'],
          '5':['5','5','5','6'], '6':['2','A','5','7'], '7':['3','B','6','8'], '8':['4','C','7','9'], '9':['9','9','8','9'],
          'A':['6','A','A','B'], 'B':['7','D','A','C'], 'C':['8','C','B','C'], 'D':['B','D','D','D']}
for line in inputdata:
    button = '5'
    for cmd in line.strip():
        nextbutton = keymap[button]
        button = nextbutton[dirmap[cmd]]
    print(button, end="")
