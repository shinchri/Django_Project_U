from struct import *

# Store as bytes data
# 'iif' = format (2 integers and 1 float)
packed_data = pack('iif', 6, 19, 4.73)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# to get the data back to normal
original_data = unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@')
print(original_data)