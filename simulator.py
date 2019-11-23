import re
from assembler import twocompliment_16bit, twocompliment_32bit
from simulator_form import simulator_form

def twocompliment_to_int(twocomp):
    if(len(twocomp) == 16):
        if(twocomp[:1] == "1"):  # check first bit
            twocomp = twocomp[-15:]  # if first bit is 1 delete first bit
            # fill firstbit with 0
            twocomp = -1*(32767 - (int(twocomp.zfill(16), 2)) + 1)
            return twocomp  # twocomp = 32767 - negativeNumber +1
        else:
            twocomp = int(twocomp, 2)
            return twocomp
    elif(len(twocomp) == 32):
        if(twocomp[:7] == "1111111"):  # check first bit
            twocomp = twocomp[-15:]  # if first 7 bit is 1 delete first 7 bit
            # fill firstbit with 0
            twocomp = -1*(32767 - (int(twocomp.zfill(16), 2)) + 1)
            return twocomp  # twocomp = 32767 - negativeNumber +1
        else:
            twocomp = int(twocomp, 2)
            return twocomp

def bit16_to_bit32(bit16):
    if int(bit16, 2) & (1 << 15):
        for n in range(0, 16):
            bit16 = "1" + bit16
    else:
        for m in range(0, 16):
            bit16 = "0" + bit16

    bit32 = bit16
    return bit32

def simulator(mem, reg, PC, mem_Int):
    count_instru = 0
    for i in range(0, 8):  # initail register
        reg[i] = 0
    while PC < len(mem):
        reg[0] = 0
        simulator_form(PC, reg, mem, mem_Int)
        count_instru = count_instru + 1
        bit = 0
        if(len(str(mem[PC])) == 32):
            bit = 7
        elif(len(str(mem[PC])) == 25):
            bit = 0
        opcode = str(mem[PC])[bit:3+bit]
        if(opcode == "000" or opcode == "001"):  # R type
            dest = int(str(mem[PC])[-3:], 2)
            A = int(str(mem[PC])[3+bit:6+bit], 2)
            B = int(str(mem[PC])[6+bit:9+bit], 2)
            if(opcode == "000"):  # add
                reg[dest] = int(reg[A]) + int(reg[B])
            elif(opcode == "001"):  # nand
                x = twocompliment_to_int(
                    twocompliment_32bit(int(reg[A])))
                y = twocompliment_to_int(
                    twocompliment_32bit(int(reg[B])))
                xnandy = twocompliment_32bit(~(x & y))
                reg[dest] = twocompliment_to_int(xnandy)
        elif(opcode == "010" or opcode == "011" or opcode == "100"):  # I type
            A = int(str(mem[PC])[3+bit:6+bit], 2)
            B = int(str(mem[PC])[6+bit:9+bit], 2)
            offset = int(twocompliment_to_int(bit16_to_bit32((mem[PC])[-16:])))
            if(opcode == "010"):  # lw
                reg[B] = mem[int(reg[A]) + offset]
            elif(opcode == "011"):     # sw
                while int(reg[A]) + offset > len(mem) - 1:
                    mem.append("0")
                    if (len(mem) > len(mem_Int)):
                        mem_Int.append("0")
                mem[int(reg[A]) + offset] = (reg[B])
                mem_Int[int(reg[A]) + offset] = (reg[B])
            elif(opcode == "100"):  # beq
                if int(reg[A]) == int(reg[B]):
                    PC = PC + offset
        elif(opcode == "101"):  # J type
            A = int(str(mem[PC])[3+bit:6+bit], 2)
            B = int(str(mem[PC])[6+bit:9+bit], 2)
            if A == B:
                reg[B] = PC + 1
            else:
                reg[B] = PC + 1
                PC = int(reg[A]) - 1
        elif(opcode == "111"):  # noop
            pass
        elif(opcode == "110"):  # halt
            break

        PC = PC + 1

    print("machine halted")
    print("total of " + str(count_instru) + " instructions executed")
    print("final state of machine:")
    simulator_form(PC, reg, mem, mem_Int)
