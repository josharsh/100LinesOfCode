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
        if c.isalpha() or c.isspace():
            c=c.upper()
            if c in symbol_codes:
                compressed += symbol_codes[c]
    with open(ofile, 'w') as f:
        f.write(compressed)
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

ifile = input("Enter your input filename: ")
codes = input("Enter the filename where you want to save your codes: ")
ofile = input("Enter the filename where you want your compressed document saved: ")
compress(ifile, codes, ofile)
print("Compressed code has been written to:", ofile)