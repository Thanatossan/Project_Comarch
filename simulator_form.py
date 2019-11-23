def simulator_form(PC, reg, mem, mem_int):
    print('\n@@@')
    print('state:')
    print('\tpc ', PC)
    print('\tmemory:')
    for x in range(0, len(mem)):
        print("\t\tmem[", x, "] ", int(mem_int[x]))
    print('\tregister:')
    for i in range(0, 8):
        print('\t\treg[', i, '] ', reg[i])
        i = i+1
    print('end state')
