# ‭0001000000010000000000000010‬
# 0001000000010000000000000110


def twocompliment_16bit(num):
    if num < 0:
        if num >= -32768:
            negative_num = -1 * num
            print(negative_num)
            compliment = (bin((32767 - negative_num + 1)))[2:].zfill(15)
            print(compliment)
            two_compliment = '1'+compliment
            return two_compliment
        else:
            raise ValueError("underflow")
    else:
        two_compliment = bin(num)[2:].zfill(16)
        if num < 32768:
            return two_compliment
        else:
            raise ValueError("overflow")


print(twocompliment_16bit(-3))
