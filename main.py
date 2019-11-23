import re  # RegEx
from assembler import Assembly
from simulator import simulator
from check_error import labelcheck
line_arr = []
filename = "testcase/test.txt"

#----------Check Error----------
labelcheck(filename)

#----------Stock line in list----------
with open(filename, 'r') as f:
    for line in f:
        line_arr.append(line)

#----------Set list of Memory----------
mem = []
for i in range(0, len(line_arr)):
    mem.append(0)
# print(mem)

#----------Set list of Memory of dec----------
mem_int = []
for i in range(0, len(line_arr)):
    mem_int.append(0)
# print(mem_int)

#----------Set list of Register----------
reg = []
for i in range(0, 8):
    reg.append(0)
# print(reg)

#----------Assambler----------
PC = 0
while PC < len(line_arr):
    field = re.split(r"\s+", line_arr[PC], 5)
    mem[PC] = Assembly(field, PC, filename)
    if(field[1] == ".fill"):
        print("memory[" + (str(PC)) + "]=" + str(int(mem[PC])))
        mem_int[PC] = int(mem[PC])
    else:
        print("memory[" + (str(PC)) + "]=" + str(int(mem[PC], 2)))
        mem_int[PC] = int(mem[PC], 2)
    # print(mem[PC])
    # print(field)
    # print(PC)
    PC += 1
# print(mem)
# print(mem_int)
# print(reg)
# print(PC)

#----------Simulator----------
PC = 0
simulator(mem, reg, PC, mem_int)