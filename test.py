import re

label_addr = {}
f2 = open("test.txt", "r")
c = 0
for line in f2:
    test1 = re.split(r"\s+", line, 5)
    if test1[0] != '':
        if test1[0] not in label_addr:
            label_addr[test1[0]] = c
        else:
            raise ValueError('Duplicate label >> ' + test1[0])
    print(c)
    print(label_addr)
    c += 1
