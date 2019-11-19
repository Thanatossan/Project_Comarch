import re
from assembler import twocompliment_16bit


def twocompliment_to_int(twocomp):
    if(twocomp[:1] == "1"):  # check first bit
        twocomp = twocomp[-15:]  # if first bit is 1 delete first bit
        # fill firstbit with 0
        twocomp = -1*(32767 - (int(twocomp.zfill(16), 2)) + 1)
        return twocomp  # twocomp = 32767 - negativeNumber +1
    else:
        twocomp = int(twocomp, 2)
        return twocomp


def simulator(mem, reg, PC):
    for i in range(0, 8):  # initail register
        reg[i] = 0

    while PC < len(mem):
        opcode = str(mem[PC])[:3]
        if(opcode == "000" or opcode == "001"):  # R type
            dest = int(str(mem[PC])[-3:], 2)
            A = int(str(mem[PC])[4:6], 2)
            B = int(str(mem[PC])[7:9], 2)
            if(opcode == "000"):  # add
                reg[dest] = int(reg[A]) + int(reg[B])
            elif(opcode == "001"):  # nand
                print("nand")
        elif(opcode == "010" or opcode == "011" or opcode == "100"):  # I type
            A = int(str(mem[PC])[4:6], 2)
            B = int(str(mem[PC])[7:9], 2)
            offset = int(twocompliment_to_int((mem[PC])[-15:]))
            if(opcode == "010"):
                reg[B] = mem[int(reg[A]) + offset]  # lw
            elif(opcode == "011"):
                mem[int(reg[A]) + offset] = reg[B]  # sw
            elif(opcode == "100"):  # beq
                if reg[A] == reg[B]:
                    PC = PC + offset
        elif(opcode == "101"):  # J type
            A = int(str(mem[PC])[4:6], 2)
            B = int(str(mem[PC])[7:9], 2)
            if A == B:
                reg[B] = PC + 1
            else:
                reg[B] = PC + 1
                PC = reg[A]
        elif(opcode == "111"):  # noop
            print("noop")
        elif(opcode == "110"):  # halt
            print("halt")
            break

        PC = PC + 1
