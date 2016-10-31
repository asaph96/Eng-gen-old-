def verifaug(seq):
    if 'aug' not in seq:
        print('A sequência não contem um "start códon"')
        return False
    else:
        return True


ccc
    try:

        b = []
        for i in range(len(a)):
            if i % 3 == 0:
                b.append(a[i] + a[i + 1] + a[i + 2])
                i -= i
            else:
                pass
    

    except NameError:

        b = []
        for i in range(len(a)):
            if i % 3 == 0:
                b.append(a[i] + a[i + 1] + a[i + 2])
                i -= i
            else:
                pass
    return b


##########################################################
def sepcodonsf2(a):
    try:

        b = []
        for i in range(len(a)):
            if i % 3 == 0:
                b.append(a[i + 1] + a[i + 2] + a[i + 3])
                i -= i
            else:
                pass

    except NameError:

        b = []
        for i in range(len(a)):
            if i % 3 == 0:
                b.append(a[i + 1] + a[i + 2] + a[i + 3])
                i -= i
            else:
                pass

    return b
############################################################
def sepcodonsf3(a):
    try:

        b = []
        for i in range(len(a)):
            if i % 3 == 0:
                b.append(a[i + 2] + a[i + 3] + a[i + 4])
                i -= i
            else:
                pass

    except NameError:

        b = []
        for i in range(len(a)):
            if i % 3 == 0:
                b.append(a[i + 2] + a[i + 3] + a[i + 4])
                i -= i
            else:
                pass
    return b

def retifica(s_tr):
    for i in range(len(s_tr)):
        s_tr[i] = s_tr[i].upper()
        i -= i

    for i in range(len(s_tr)):
        if s_tr[i] == 'T':
            s_tr[i] = 'U'
        else:
            pass
        i -= i


def traduzir_codons_3_letras(seq):
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

    for i in range(len(seq)):
        if seq[i] in ALA:
            z.append('ALA')
        elif seq[i] in ARG:
            z.append('ARG')
        elif seq[i] in ASN:
            z.append('ASN')
        elif seq[i] in ASP:
            z.append('ASP')
        elif seq[i] in CYS:
            z.append('CYS')
        elif seq[i] in GLN:
            z.append('GLN')
        elif seq[i] in GLU:
            z.append('GLU')
        elif seq[i] in GLY:
            z.append('GLY')
        elif seq[i] in HIS:
            z.append('HIS')
        elif seq[i] in ILE:
            z.append('ILE')
        elif seq[i] in LEU:
            z.append('LEU')
        elif seq[i] in LYS:
            z.append('LYS')
        elif seq[i] in MET:
            z.append('MET')
        elif seq[i] in PHE:
            z.append('PHE')
        elif seq[i] in PRO:
            z.append('PRO')
        elif seq[i] in SER:
            z.append('SER')
        elif seq[i] in THR:
            z.append('THR')
        elif seq[i] in TRP:
            z.append('TRP')
        elif seq[i] in TYR:
            z.append('TYR')
        elif seq[i] in VAL:
            z.append('VAL')
        elif seq[i] in PRD:
            z.append('STOP')
        i -= i
    return z
