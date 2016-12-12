code = [i.strip() for i in open("input.txt").readlines()]

pos = 0;
reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
while pos < len(code):
    ops = code[pos].split(' ')
    ops1 = reg[ops[1]] if ops[1].isalpha() else int(ops[1])
    if ops[0] == "cpy":
            reg[ops[2]] = ops1
    elif ops[0] == "inc":
        reg[ops[1]] += 1
    elif ops[0] == "dec":
        reg[ops[1]] -= 1
    if ops[0] == "jnz" and ops1 != 0:
        pos += int(ops[2])
    else:
        pos += 1
print(reg)
