#while 
x = 0
i = 0
print('@@@')
print('state:')
print('\tpc ',0)
print('\tmemory:')
while x < 3:
    print("\t\tmem[",x,"] ",x+1)
    x = x+1
print('\tregister:')
while i < 3:
    print('\t\treg[',i,'] ',i+2) 
    i = i+1
print('end state')
