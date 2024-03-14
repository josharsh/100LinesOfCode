def decompress(ifile, codes,ofile):
    symbol_codes = {}
    with open(codes, 'r') as f:
        for line in f:
            last_space_index = line.rfind(' ')
            if last_space_index != -1:
                symbol = line[:last_space_index]
                code = line[last_space_index + 1:].strip()
                symbol_codes[code] = symbol
    with open(ifile, 'r') as f:
        compressed = f.readline()
    decompressed = ''
    current = ''
    for bit in compressed:
        current += bit
        if current in symbol_codes.keys():
            decompressed += symbol_codes[current]
            current = ''
    with open(ofile, 'w') as f:
        f.write(decompressed)

ifile = input("Enter your input (compressed) filename: ")
codes = input("Enter the filename where you have saved your codes: ")
ofile = input("Enter the filename where you want your decompressed document saved: ")
decompress(ifile, codes,ofile)
print("Decompressed code has been written to:", ofile)

