def fract_to_bin(fract):
    fract_len = len(str(fract)) - 1
    return_str = ""
    for _ in range(32):
        if fract <= 0:
            return return_str
        fract = round(fract * 2, fract_len)
        if fract >= 1:
            return_str += "1"
            fract -= 1
        else:
            return_str += "0"
    return "ERROR"

print(fract_to_bin(.21))