  x = bin(int(reg[A]))[2:]
      y = bin(int(reg[B]))[2:]
       if(len(x)) >= (len(y)):
            y = y.zfill(len(x))
        else:
            x = x.zfill(len(y))
        for i in range(0, len(y)):
            nand_bit = ""
            if(x[i:i+1] == "1" and y[i:i+1] == "1"):
                nand_bit = nand_bit + "0"
            else:
                nand_bit = nand_bit + "1"
        reg[dest] = nand_bit
