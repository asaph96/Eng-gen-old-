def retifica(s_tr):
    a = []
    for i in range(len(s_tr)):
        a.append(s_tr[i].upper())
        i -= i

    for i in range(len(a)):
        if a[i] == 'T':
            a[i] = 'U'
        else:
            pass
        i -= i
    return a


def sepcodons(lista, frame):
    if frame == 1:
        if len(lista) % 3 == 1:
            c = lista.copy()
            c.append('-')
            c.append('-')
            b = []
            for i in range(len(c)):
                if i % 3 == 0:
                    b.append(lista[i] + lista[i + 1] + lista[i + 2])
                    i -= i
                else:
                    pass
        elif len(lista) % 3 == 2:
            c = lista.copy()
            c.append('-')
            b = []
            for i in range(len(c)):
                if i % 3 == 0:
                    b.append(lista[i] + lista[i + 1] + lista[i + 2])
                    i -= i
                else:
                    pass
        else:
            c = lista.copy()
            b = []
            for i in range(len(c)):
                if i % 3 == 0:
                    b.append(lista[i] + lista[i + 1] + lista[i + 2])
                    i -= i
                else:
                    pass

    elif frame == 2:
        if len(lista) % 3 == 1:
            c = lista.copy()
            c.append('-')
            c.append('-')
            b = []
            for i in range(len(c) - 3):
                if i % 3 == 0:
                    b.append(lista[i + 1] + lista[i + 2] + lista[i + 3])
                    i -= i
                else:
                    pass
        elif len(lista) % 3 == 2:
            c = lista.copy()
            c.append('-')
            b = []
            for i in range(len(c) - 3):
                if i % 3 == 0:
                    b.append(lista[i + 1] + lista[i + 2] + lista[i + 3])
                    i -= i
                else:
                    pass
        else:
            c = lista.copy()
            b = []
            for i in range(len(c)-3):
                if i % 3 == 0:
                    b.append(lista[i + 1] + lista[i + 2] + lista[i + 3])
                    i -= i
                else:
                    pass

    elif frame == 3:
        if len(lista) % 3 == 1:
            c = lista.copy()
            c.append('-')
            c.append('-')
            b = []
            for i in range(len(c) - 6):
                if i % 3 == 0:
                    b.append(lista[i + 2] + lista[i + 3] + lista[i + 4])
                    i -= i
                else:
                    pass
        elif len(lista) % 3 == 2:
            c = lista.copy()
            c.append('-')
            b = []
            for i in range(len(c) - 6):
                if i % 3 == 0:
                    b.append(lista[i + 2] + lista[i + 3] + lista[i + 4])
                    i -= i
                else:
                    pass
        else:
            c = lista.copy()
            b = []
            for i in range(len(c) - 6):
                if i % 3 == 0:
                    b.append(lista[i + 2] + lista[i + 3] + lista[i + 4])
                    i -= i
                else:
                    pass

    return b


def verifaug(lista):
    if 'aug' not in lista:
        print('A sequência não contem um "start códon"')
        return False
    else:
        return True


def traduzir_codons(lista, nletras):
    ALA = 'GCU', 'GCC', 'GCA', 'GCG'
    ARG = 'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'
    ASN = 'AAU', 'AAC'
    ASP = 'GAU', 'GAC'
    CYS = 'UGU', 'UGC'
    GLN = 'CAA', 'CAG'
    GLU = 'GAA', 'GAG'
    GLY = 'GGU', 'GGC', 'GGA', 'GGG'
    HIS = 'CAU', 'CAC'
    ILE = 'AUU', 'AUC', 'AUA'
    LEU = 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'
    LYS = 'AAA', 'AAG'
    MET = 'AUG'
    PHE = 'UUU', 'UUC'
    PRO = 'CCU', 'CCC', 'CCA', 'CCG'
    SER = "UCU", 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'
    THR = 'ACU', 'ACC', 'ACA', 'ACG'
    TRP = 'UGG'
    TYR = 'UAU', 'UAC'
    VAL = 'GUU', 'GUC', 'GUA', 'GUG'
    PRD = 'UAG', 'UGA', 'UAA'

    z = []
    if nletras == 3:
        for i in range(len(lista)):
            if lista[i] in ALA:
                z.append('ALA')
            elif lista[i] in ARG:
                z.append('ARG')
            elif lista[i] in ASN:
                z.append('ASN')
            elif lista[i] in ASP:
                z.append('ASP')
            elif lista[i] in CYS:
                z.append('CYS')
            elif lista[i] in GLN:
                z.append('GLN')
            elif lista[i] in GLU:
                z.append('GLU')
            elif lista[i] in GLY:
                z.append('GLY')
            elif lista[i] in HIS:
                z.append('HIS')
            elif lista[i] in ILE:
                z.append('ILE')
            elif lista[i] in LEU:
                z.append('LEU')
            elif lista[i] in LYS:
                z.append('LYS')
            elif lista[i] in MET:
                z.append('MET')
            elif lista[i] in PHE:
                z.append('PHE')
            elif lista[i] in PRO:
                z.append('PRO')
            elif lista[i] in SER:
                z.append('SER')
            elif lista[i] in THR:
                z.append('THR')
            elif lista[i] in TRP:
                z.append('TRP')
            elif lista[i] in TYR:
                z.append('TYR')
            elif lista[i] in VAL:
                z.append('VAL')
            elif lista[i] in PRD:
                z.append('STOP')
            i -= i
    elif nletras == 1:
        for i in range(len(lista)):
            if lista[i] in ALA:
                z.append('A')
            elif lista[i] in ARG:
                z.append('R')
            elif lista[i] in ASN:
                z.append('N')
            elif lista[i] in ASP:
                z.append('D')
            elif lista[i] in CYS:
                z.append('C')
            elif lista[i] in GLN:
                z.append('Q')
            elif lista[i] in GLU:
                z.append('E')
            elif lista[i] in GLY:
                z.append('G')
            elif lista[i] in HIS:
                z.append('H')
            elif lista[i] in ILE:
                z.append('I')
            elif lista[i] in LEU:
                z.append('L')
            elif lista[i] in LYS:
                z.append('K')
            elif lista[i] in MET:
                z.append('M')
            elif lista[i] in PHE:
                z.append('F')
            elif lista[i] in PRO:
                z.append('P')
            elif lista[i] in SER:
                z.append('S')
            elif lista[i] in THR:
                z.append('T')
            elif lista[i] in TRP:
                z.append('W')
            elif lista[i] in TYR:
                z.append('Y')
            elif lista[i] in VAL:
                z.append('V')
            elif lista[i] in PRD:
                z.append('STOP')
    return z


seq = list(input('Digite sua sequência\n=> '))
ret = retifica(seq)
# print(ret)
cdnsf1 = sepcodons(ret, 1)
cdnsf2 = sepcodons(ret, 2)
cdnsf3 = sepcodons(ret, 3)
a = traduzir_codons(cdnsf1, 1)
b = traduzir_codons(cdnsf2, 1)
c = traduzir_codons(cdnsf3, 1)
print(a)
print(b)
print(c)
