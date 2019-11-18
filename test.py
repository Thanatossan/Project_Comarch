
intNumber = -10
if intNumber < 0:
    if intNumber >= -32768:
        negNum = intNumber*-1
        top = bin(32767)[2:].zfill(15)
        bi = bin(negNum)[2:].zfill(15)
        negate = int(top, 2) - int(bi, 2) + int('1', 2)
        result = '1'+bin(negate)[2:].zfill(15)
        print(result)
    else:
        raise ValueError("Overflow Number OffsetField")
else:
    result = bin(intNumber)[2:].zfill(16)
    if intNumber < 32768:
        print(result)
    else:
        raise ValueError("Overflow Number OffsetField")


# print(0b01)
# import re
# label_addr = {}  # storeLabel as dictionary
# temp = 0
# with open('test.txt', 'r') as f2:

#     for line in f2:
#         key = re.split(r"\s+", line, 5)
#         print(key[0])
#         if key[0] != '':
#             if key[0] not in label_addr:
#                 label_addr[key[0]] = temp
#             else:
#                 raise ValueError('label duplicated : ' + key[0])
#         temp += 1
#     print(label_addr)
# print('five' in label_addr)  # check statement
num = -10
if num < 0:
    if num >= -32768:
        negative_num = -1 * num
        compliment = (bin((32767 - negative_num + 1)))[2:].zfill(15)
        two_compliment = '1'+compliment
        print(two_compliment)
    else:
        raise ValueError("underflow")
else:
    two_compliment = bin(num)[2:].zfill(16)
    if num < 32768:
        print(two_compliment)
    else:
        raise ValueError("overflow")
