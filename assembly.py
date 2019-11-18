

# def check_offset(parameter, PC):
#     print(parameter)
#     for i in range(0, len(parameter)):
#         print(i)
#         print(parameter[i])
#         check_arr.append(parameter[i])
#         # if not (parameter[i].isdigit()):
#         #     fill_arr.append(parameter[4])
#         print(check_arr)
#         if(parameter[1] == ".fill"):
#             fill_arr.append(parameter[0] + ' ' + parameter[2])

#         print(fill_arr)

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


def Assembly(parameter, reg, PC):

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

        if not (parameter[4].isdigit()):
            sym = offset
            addr_label = storelabel()[sym]
            print(addr_label)
            bin_addr_label = bin((addr_label))[2:].zfill(16)
            print(bin((addr_label))[2:].zfill(16))

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
