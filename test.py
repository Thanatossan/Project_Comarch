bit16= "0001000000000000"
if int(bit16, 2) & (1 << 15):
    for n in range(0, 16):
        bit16 = "1" + bit16
else:
    for m in range(0, 16):
        bit16 = "0" + bit16

bit32 = bit16
    
print(bit32)