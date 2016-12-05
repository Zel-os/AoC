from hashlib import *

doorid = "ojvtpuvg"
blank = {'0', '1', '2', '3', '4', '5', '6', '7'}
code1 = ""; code2 = list("........"); n = 0
while len(blank) != 0:
    dhash = md5(str(doorid+str(n)).encode('utf-8')).hexdigest()
    if dhash[0:5] == "00000":
        code1 += dhash[5]
        if dhash[5] in blank:
            blank.remove(dhash[5])
            code2[int(dhash[5])] = dhash[6]
    n += 1
print(code1[0:8], ''.join(code2))
