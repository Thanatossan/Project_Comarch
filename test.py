"10101010101010101010101010101010"
"00000000000000000000000000000000"
a = "10101010101010101010101010101010"
ass = list(a)
rd = [ass[0],ass[1],ass[2]]
rs = [ass[19],ass[20],ass[21]]
rt = [ass[16],ass[17],ass[18]]
print(rs)
print(rt)
print
i = 0
while i < len(rd):
    if rs[i] == "0" or rt[i] == "0":
        rd[i] = "1"
    else:
        rd[i] = "0"
    i = i+1
i = 0
ans = ""
while i < len(rd):
    ans = ans+rd[i]
    i = i+1
print(ans)