#import text
import re  # RegEx

def labelcheck(filename):
    with open(filename, 'r') as f:
        for line1 in f:
            check = False
            label = re.split(r"\s+", line1, 5)
            # print(label)
            if len(label) < 5:
                # print('low')
                continue
            if not (label[4].lstrip('-').isdigit()):
                for line2 in f:
                    check = False
                    instruc = re.split(r"\s+", line2, 5)
                    # print(instruc)
                    if label[4] == instruc[0]:
                        if instruc[1] == 'halt' or instruc[1] == 'noop':
                            check = True
                            break
                        elif instruc[1] != '':
                            if instruc[2] != '':
                                check = True
                                break
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue        
                if check == False:
                    raise ValueError('label undifine')
                # else:
                #     print('pass')
            else:
                # print('number')
                continue