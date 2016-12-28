code = [i.strip() for i in open("input.txt").readlines()]

target = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
output = []
a = 0
while True:
    pos = 0
    reg = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    output.clear()
    while pos < len(code):
        ops = code[pos].split(' ')
        ops1 = reg[ops[1]] if ops[1].isalpha() else int(ops[1])
        if ops[0] == "cpy":
            if ops[2].isalpha(): reg[ops[2]] = ops1
        elif ops[0] == "inc":
            if ops[1].isalpha(): reg[ops[1]] += 1
        elif ops[0] == "dec":
            if ops[1].isalpha(): reg[ops[1]] -= 1
        elif ops[0] == "mul":
            reg[ops[3]] += reg[ops[2]] * reg[ops[1]]
            reg[ops[2]] = 0
            reg[ops[1]] = 0
        elif ops[0] == "out":
            output.append(ops1)
        elif ops[0] == "tgl":
            if pos+ops1 in range(0, len(code)):
                tglops = code[pos+ops1].split(' ')
                if tglops[0] in {"dec", "tgl"}:
                    code[pos+ops1] = "inc "+ ' '.join(tglops[1:])
                if tglops[0] == "inc":
                    code[pos+ops1] = "dec "+ ' '.join(tglops[1:])
                if tglops[0] == "jnz":
                    code[pos+ops1] = "cpy "+ ' '.join(tglops[1:])
                if tglops[0] == "cpy":
                    code[pos+ops1] = "jnz "+ ' '.join(tglops[1:])
        if ops[0] == "jnz" and ops1 != 0:
            pos += reg[ops[2]] if ops[2].isalpha() else int(ops[2])
        else:
            pos += 1
        if len(output) == 10:
            if output == target:
                print("Match:", a)
                exit()
            break
    if a % 10 == 0:
        print("...", a)
    a += 1
