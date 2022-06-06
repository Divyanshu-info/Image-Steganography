def encode_pixel(value1, value2):
    if value1 == 255:
        if value2 == 1:
            return value1
        else:
            return value1-1
    bin_value1 = int(str(bin(value1))[-1])
    if bin_value1 == value2:
        return value1
    else:
        return value1+1
        

print(encode_pixel(0, 0))
print(encode_pixel(0, 1))

print(encode_pixel(1, 0))

print(encode_pixel(1, 1))

print(encode_pixel(254, 0))

print(encode_pixel(255, 0))

print(encode_pixel(254, 1))
print(encode_pixel(255, 1))

print(encode_pixel(128, 0))
print(encode_pixel(128, 1))
print(encode_pixel(129, 0))
print(encode_pixel(129, 1))
