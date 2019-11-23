import re
check_arr = []
fill_arr = []
Mech = ''

def storelabel(filename):

    label_addr = {}  # storeLabel as dictionary
    temp = 0
    with open(filename, 'r') as f2:
        for line in f2:
            key = re.split(r"\s+", line, 5)
            if key[0] != '':
                if key[0] not in label_addr:
                    label_addr[key[0]] = temp
                else:
                    raise ValueError('label duplicated : ' + key[0])
            temp += 1
    return label_addr


def twocompliment_16bit(num): 
    if num < 0:
        if num >= -32768:
            negative_num = -1 * num
            compliment = (bin((32767 - negative_num + 1)))[2:].zfill(15)
            two_compliment = '1'+compliment
            return two_compliment
        else:
            raise ValueError("underflow")
    else:
        two_compliment = bin(num)[2:].zfill(16)
        if num < 32768:
            return two_compliment
        else:
            raise ValueError("overflow")


def twocompliment_32bit(num):
    if num < 0:
        if num >= -2147483648:
            negative_num = -1 * num
            compliment = (bin((2147483647 - negative_num + 1)))[2:].zfill(31)
            two_compliment = '1'+compliment
            return two_compliment
        else:
            raise ValueError("underflow")
    else:
        two_compliment = bin(num)[2:].zfill(32)
        if num < 2147483648:
            return two_compliment
        else:
            raise ValueError("overflow")


def Assembly(field, PC, filename):

    # R type
    if field[1] == "add" or field[1] == "nand":
        instru = field[1]
        regA = field[2]
        regB = field[3]
        offset = field[4]
        opcode = ''
        if(field[1] == "add"):
            opcode = "000"
        elif(field[1] == "nand"):
            opcode = "001"
        Mech = (opcode+bin(int(field[2]))[2:].zfill(3) +
                bin(int(field[3]))[2:].zfill(3) + "0000000000000"+bin(int(field[4]))[2:].zfill(3))

        return Mech
    # I type
    elif field[1] == "lw" or field[1] == "sw" or field[1] == "beq":
        instru = field[1]
        regA = field[2]
        regB = field[3]
        offset = field[4]
        if(field[1] == "lw"):
            opcode = "010"
        elif(field[1] == "sw"):
            opcode = "011"
        elif(field[1] == "beq"):
            opcode = "100"

        if not (field[4].lstrip('-').isdigit()):
            addr_label = storelabel(filename)[offset]
            bin_addr_label = bin((addr_label))[2:].zfill(16)
            if(field[1] == "lw" or field[1] == "sw"):
                Mech = (
                    opcode + bin(int(field[2]))[2:].zfill(3) +
                    bin(int(field[3]))[2:].zfill(3)+bin_addr_label)
                return Mech
            elif(field[1] == "beq"):
                # if(addr_label-1 < PC):
                #     # in case of addr_label is above current
                #     addr_above = (addr_label) - PC - 1
                #     Mech = (
                #         opcode + bin(int(field[2]))[2:].zfill(3) +
                #         bin(int(field[3]))[2:].zfill(3)+twocompliment_16bit(addr_above))
                # else:
                Mech = (
                    opcode + bin(int(field[2]))[2:].zfill(3) +
                    bin(int(field[3]))[2:].zfill(3)+twocompliment_16bit(addr_label-PC-1))

                return Mech
        elif(field[4].isdigit()):

            if(field[1] == "beq"):
                Mech = (
                    opcode + bin(int(field[2]))[2:].zfill(3) +
                    bin(int(field[3]))[2:].zfill(3)+twocompliment_16bit(int(field[4])))
                return Mech
            elif(field[1] == "lw" or field[1] == "sw"):
                Mech = (
                    opcode + bin(int(field[2]))[2:].zfill(3) +
                    bin(int(field[3]))[2:].zfill(3)+twocompliment_16bit(int(field[4])))
                return Mech

    # J type
    elif field[1] == "jalr":
        instru = field[1]
        regA = field[2]
        regB = field[3]
        opcode = "101"

        Mech = (opcode+bin(int(field[2]))[2:].zfill(3) +
                bin(int(field[3]))[2:].zfill(3) + "0000000000000000")
        return Mech

    # O type
    elif field[1] == "halt" or field[1] == "noop":
        if(field[1] == "halt"):
            opcode = "110"
        elif(field[1] == "noop"):
            opcode = "111"

        Mech = (opcode + "0000000000000000000000")
        return Mech

    elif field[1] == ".fill":
        fill_addr = field[2]
        if not(fill_addr.lstrip('-').isdigit()):
            addr_label = storelabel(filename)[fill_addr]
            #print(addr_label)
            return addr_label
        else:
            #print(fill_addr)
            return fill_addr
    else:
        raise ValueError("Invalid Error")
