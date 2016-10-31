def split_input(string, chunk_size):
    num_chunks = len(string)/chunk_size
    if (len(string) % chunk_size != 0):
        num_chunks += 1
    output = []
    for i in range(0, int(num_chunks)):
        output.append(string[chunk_size * i:chunk_size * (i+1)])
    return output

def printDna(dna1, dna2, tamanho):
    chunks1 = split_input(dna1, tamanho)
    chunks2 = split_input(dna2, tamanho)

    for i in range(0, len(chunks1)):
        print(chunks1[i])
        print('|'*len(chunks1[i]))
        print(chunks2[i])
        print()
e = 'ta'*200
f = 'at'*200
printDna(e, f, 80)
