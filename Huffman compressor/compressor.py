import math
def compress(ifile, codes, ofile):
    symbol_codes = {}
    with open(codes, 'r') as f:
        for line in f:
            last_space_index = line.rfind(' ')
            if last_space_index != -1:
                symbol = line[:last_space_index]
                code = line[last_space_index + 1:].strip()
                symbol_codes[symbol] = code
    with open(ifile, 'r') as f:
        itext = f.read().strip()
    compressed = ''
    for c in itext:
        if c.isalpha() :
            c=c.upper()
            if c in symbol_codes:
                compressed += symbol_codes[c]
    compressed_bytes = compress_bits(compressed)
    with open(ofile, 'wb') as f:
        f.write(compressed_bytes)
    entropy(itext,compressed)
def entropy(a,b):
    D = {}
    E = {}
    for i in a:
        if i not in D:
            D[i]=1
        else:
            D[i]+=1
    for i in b:
        if i not in E:
            E[i]=1
        else:
            E[i]+=1
    entropya=0
    for i in D:
        entropya+=(D[i]/len(a))*math.log2((len(a)/D[i]))
    entropyb=0
    for i in E:
        entropyb+=(E[i]/len(b))*math.log2((len(b)/E[i]))
    print("The information gain from compression is: ",entropya-entropyb)
def compress_bits(compressed):
    compressed_bytes = bytearray()
    current_byte = 0
    bit_count = 0
    for bit in compressed:
        current_byte <<= 1
        current_byte |= int(bit)
        bit_count += 1
        if bit_count == 8:
            compressed_bytes.append(current_byte)
            current_byte = 0
            bit_count = 0
    if bit_count > 0:
        current_byte <<= (8 - bit_count)
        compressed_bytes.append(current_byte)
    return bytes(compressed_bytes)
ifile = input("Enter your input filename: ")
codes = input("Enter the filename where you have saved your codes: ")
ofile = input("Enter the filename where you want your compressed document saved: ")
compress(ifile, codes, ofile)
print("Compressed code has been written to:", ofile)