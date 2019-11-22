import re  # RegEx
from assembler import Assembly
from simulator import simulator
line_arr = []
filename = "testcase/combination.txt"
with open(filename, 'r') as f:
    for line in f:
        line_arr.append(line)

mem = []
for i in range(0, len(line_arr)):
    mem.append(0)
    # print(mem)

mem_int = []
for i in range(0, len(line_arr)):
    mem_int.append(0)
    # print(mem)


reg = []
for i in range(0, 8):
    reg.append(0)
   # print(reg)


PC = 0
while PC < len(line_arr):
    parameter = re.split(r"\s+", line_arr[PC], 5)
    # print(parameter)
    # check_offset(parameter, PC)
    # # checkoffset(parameter, PC)
    mem[PC] = Assembly(parameter, mem, PC, filename)

    # print(mem[PC])
    #  print(parameter)
    # print(PC)
    if(parameter[1] == ".fill"):
        print("memory[" + (str(PC)) + "]=" + str(int(mem[PC])))
        mem_int[PC] = int(mem[PC])

    else:
        print("memory[" + (str(PC)) + "]=" + str(int(mem[PC], 2)))
        mem_int[PC] = int(mem[PC], 2)

    PC += 1

PC = 0
simulator(mem, reg, PC, mem_int)
