import re  # RegEx
from assembly import Assembly
line_arr = []
with open('test.txt', 'r') as f:
    for line in f:
        line_arr.append(line)

mem = []
for i in range(0, len(line_arr)):
    mem.append(0)
    # print(mem)


reg = []
for i in range(0, len(line_arr)):
    reg.append(0)
   # print(reg)


PC = 0
while PC < len(line_arr):
    parameter = re.split(r"\s+", line_arr[PC], 5)
    # print(parameter)
    # convert whole inst to machineCode and store memory
    # check_offset(parameter, PC)
    # # checkoffset(parameter, PC)
    Assembly(parameter, reg, PC)
  #  print(parameter)
    print(PC)

    PC += 1
