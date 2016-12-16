data = "10111100110001111"
#dsize = 272
dsize = 35651584

while len(data) <= dsize:
    buf = ""
    for n in data[::-1]:
        buf += "0" if n == "1" else "1"
    data = data + "0" + buf
data = data[:dsize]

while len(data) % 2 == 0:
    chk = ""
    for i in range(0, len(data), 2):
        chk += "1" if data[i] == data[i+1] else "0"
    data = chk
print(len(data), data)
