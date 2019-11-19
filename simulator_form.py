def simulator_form(PC, reg, mem):
    print('@@@')
    print('state:')
    print('\tpc ', PC)
    print('\tmemory:')
    for x in range(0, len(mem)):
        print("\t\tmem[", x, "] ", int(mem[PC+x], 2))
    print('\tregister:')
    for i in range(0, 8):
        print('\t\treg[', i, '] ', reg[i])
        i = i+1
    print('end state')
