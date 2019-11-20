a = "21"
b = "1"
dest = ""
x = bin(int(a))[2:]
y = bin(int(b))[2:]
if(len(x)) >= (len(y)):
    y = y.zfill(len(x))
else:
    x = x.zfill(len(y))
for i in range(0, len(y)):
    if(x[i:i+1] == "1" and y[i:i+1] == "1"):
        dest = dest + "0"
    else:
        dest = dest + "1"
print(dest)
print(int(dest, 2))