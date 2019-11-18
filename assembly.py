
import re
check_arr = []
fill_arr = []
Mech = ''


def storelabel():

    label_addr = {}  # storeLabel as dictionary
    temp = 0
    with open('test.txt', 'r') as f2:

        for line in f2:
            key = re.split(r"\s+", line, 5)
            if key[0] != '':
                if key[0] not in label_addr:
                    label_addr[key[0]] = temp
                else:
                    raise ValueError('label duplicated : ' + key[0])
            temp += 1
    # print(label_addr)
    # print('five' in label_addr)  # check statement

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


def Assembly(parameter, mem, PC):

    # R type
    if parameter[1] == "add" or parameter[1] == "nand":
        instru = parameter[1]
        regA = parameter[2]
        regB = parameter[3]
        offset = parameter[4]
        opcode = ''
        if(parameter[1] == "add"):
            opcode = "000"
        elif(parameter[1] == "nand"):
            opcode = "001"
        Mech = (opcode+bin(int(parameter[2]))[2:].zfill(3) +
                bin(int(parameter[3]))[2:].zfill(3) + "0000000000000"+bin(int(parameter[4]))[2:].zfill(3))

        return Mech
    # I type
    elif parameter[1] == "lw" or parameter[1] == "sw" or parameter[1] == "beq":
        instru = parameter[1]
        regA = parameter[2]
        regB = parameter[3]
        offset = parameter[4]
        if(parameter[1] == "lw"):
            opcode = "010"
        elif(parameter[1] == "sw"):
            opcode = "011"
        elif(parameter[1] == "beq"):
            opcode = "100"

        if not (parameter[4].lstrip('-').isdigit()):
            addr_label = storelabel()[offset]
            bin_addr_label = bin((addr_label))[2:].zfill(16)
            if(parameter[1] == "lw" or parameter[1] == "sw"):
                Mech = (
                    opcode + bin(int(parameter[2]))[2:].zfill(3) +
                    bin(int(parameter[3]))[2:].zfill(3)+bin_addr_label)
                return Mech
            elif(parameter[1] == "beq"):
                if(addr_label < PC):
                    # in case of addr_label is above current
                    addr_label = (addr_label * (-1)) - 1
                Mech = (
                    opcode + bin(int(parameter[2]))[2:].zfill(3) +
                    bin(int(parameter[3]))[2:].zfill(3)+twocompliment_16bit(addr_label))
                return Mech
        elif(parameter[4].isdigit()):

            if(parameter[1] == "beq"):
                Mech = (
                    opcode + bin(int(parameter[2]))[2:].zfill(3) +
                    bin(int(parameter[3]))[2:].zfill(3)+twocompliment_16bit(int(parameter[4])))
                return Mech
            elif(parameter[1] == "lw" or parameter[1] == "sw"):
                Mech = (
                    opcode + bin(int(parameter[2]))[2:].zfill(3) +
                    bin(int(parameter[3]))[2:].zfill(3)+twocompliment_16bit(int(parameter[4])))
                return Mech

    # J type
    elif parameter[1] == "jalr":
        instru = parameter[1]
        regA = parameter[2]
        regB = parameter[3]
        opcode = "101"

        Mech = (opcode+bin(int(parameter[2]))[2:].zfill(3) +
                bin(int(parameter[3]))[2:].zfill(3) + "0000000000000000")
        return Mech

    # O type
    elif parameter[1] == "halt" or parameter[1] == "noop":
        if(parameter[1] == "halt"):
            opcode = "110"
        elif(parameter[1] == "noop"):
            opcode = "111"

        Mech = (opcode + "0000000000000000000000")
        return Mech

    elif parameter[1] == ".fill":
        fill_addr = parameter[2]
        if not(fill_addr.lstrip('-').isdigit()):
            addr_label = storelabel()[fill_addr]
            return addr_label
        else:
            return fill_addr
