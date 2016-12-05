inputdata = open("input.txt")

total = 0
for line in inputdata:
    split = line.rpartition("-")
    name = split[0]
    code = ''.join(sorted(split[0])).strip("-")
    split = split[2].partition("[")
    sid = int(split[0])
    chk = split[2].rstrip("]\n")

    counts = {}
    for letter in set(code):
        counts[letter] = code.count(letter)
    test = sorted(counts.items())
    test = sorted(test, key=lambda x:x[1], reverse=True)
    match = ''.join(str(a) for a,b in test)[0:5]
    if match == chk:
        total += sid
        decoded = ""
        for char in name:
            if char == "-":
                decoded += " "
            else:
                for i in range(sid%26):
                    char = chr(ord(char)+1)
                    if char == '{': char = 'a'
                decoded += char
        print(sid, decoded)
print(total)

