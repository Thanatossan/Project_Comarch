#import text
import re  # RegEx
# -------------check label undefine --------


def labelcheck(filename):
    with open(filename, 'r') as f:
        for line1 in f:
            check = False
            label = re.split(r"\s+", line1, 5)
            if len(label) < 5:
                continue
            if not (label[4].lstrip('-').isdigit()):
                for line2 in f:
                    check = False
                    instruc = re.split(r"\s+", line2, 5)
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
                    raise ValueError('label Undifine')
            else:
                continue
