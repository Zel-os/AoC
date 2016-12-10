def decompress(data, ver):
    outlength = 0
    while True:
        dcs = data.find('(')
        if dcs == -1:
            outlength += len(data)
            break
        outlength += len(data[:dcs])
        work, data = data[dcs+1:].split(')', 1)
        num, rpt = work.split('x')
        block = data[:int(num)]
        data = data[int(num):]
        if ver == 2:
            expanded = decompress(block, 2)
        else:
            expanded = len(block)
        outlength += expanded * int(rpt)
    return outlength


inputdata = open("input.txt").readline().strip()
print("v1:", decompress(inputdata, 1))
print("v2:", decompress(inputdata, 2))

