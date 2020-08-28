def replace_bits(bits, replace, i, j):
    all_ones = ~0
    left = all_ones << (i+1)
    right = (1 << j) - 1
    mask = left | right
    bits = mask & bits
    return bits | (replace << i)


bits = 0b10000000000000
replace = 0b1010101
print(bin(replace_bits(bits, replace, 3, 7)))
