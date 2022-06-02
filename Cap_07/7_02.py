s = "AAACTBF"
s2 = "CBT"
s3 = ""
p = 0
q = -1
while p < len(s2):
    q = s.find(s2[p])
    if q >= 0:
        s3 += s[q]
    p += 1
print(s3)