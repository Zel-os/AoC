inputdata = open("input.txt").readlines()

status = dict()
commands = dict()
for line in inputdata:
    parsed = line.strip().split(' ')
    if parsed[0] == "value":
        status.setdefault(parsed[5], []).append(int(parsed[1]))
    else:  #parsed[0] == "bot"
        a = 'o' + parsed[6] if parsed[5] == "output" else parsed[6]
        b = 'o' + parsed[11] if parsed[10] == "output" else parsed[11]
        commands[parsed[1]] = [a, b]

while len(commands) > 0:
    botlist = [i for i in status.items()]
    for bot in botlist:
        if len(bot[1]) == 2:
            values = status.pop(bot[0])
            target = commands.pop(bot[0])
            status.setdefault(target[0], []).append(min(values))
            status.setdefault(target[1], []).append(max(values))
            if min(values) == 17 and max(values) == 61:
                print("Values 61 and 17 are compared by bot:", bot[0])

ans = status.get('o0')[0] * status.get('o1')[0] * status.get('o2')[0]
print("Multiplied values in output bins 0, 1, 2:", ans)
