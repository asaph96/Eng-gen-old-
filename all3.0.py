class Enggen(object):
    def __init__(self, seq, frame, nletras):
        self.CYS = 'UGU', 'UGC'
        self.GLN = 'CAA', 'CAG'
        self.GLU = 'GAA', 'GAG'
        self.GLY = 'GGU', 'GGC', 'GGA', 'GGG'
        self.HIS = 'CAU', 'CAC'
        self.ILE = 'AUU', 'AUC', 'AUA'
        self.LEU = 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'
        self.LYS = 'AAA', 'AAG'
        self.MET = 'AUG',
        self.PHE = 'UUU', 'UUC'
        self.PRO = 'CCU', 'CCC', 'CCA', 'CCG'
        self.SER = "UCU", 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'
        self.THR = 'ACU', 'ACC', 'ACA', 'ACG'
        self.TRP = 'UGG',
        self.TYR = 'UAU', 'UAC'
        self.VAL = 'GUU', 'GUC', 'GUA', 'GUG'
        self.PRD = 'UAG', 'UGA', 'UAA'
        self.ASP = 'GAU', 'GAC'
        self.ASN = 'AAU', 'AAC'
        self.ARG = 'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'
        self.ALA = 'GCU', 'GCC', 'GCA', 'GCG'
        self.__seq = seq
        self.__sequp = []
        self.__frame = frame
        self.__nletras = nletras
        self.__a = []
        self.__z = list(zip(*self.__a))
        self.__dpl1 = []
        self.__dpl2 = []

    def transcricao(self):
        self.__a = []
        for i in range(len(self.__seq)):
            self.__a.append(self.__seq[i].upper())
            i -= i

        for i in range(len(self.__a)):
            if self.__a[i] == 'T':
                self.__a[i] = 'U'
            else:
                pass
            i -= i
        return self.__a

    def sequencia(self):
        for i in range(len(self.__seq)):
            self.__sequp.append(self.__seq[i])
            i-=i
        return self.__sequp

    def sepcodons(self):
        if self.__frame == 1:
            a1 = self.__a[0:(len(self.__a) - 1):3]
            b1 = self.__a[1:(len(self.__a) - 1):3]
            c1 = self.__a[2:(len(self.__a)):3]
            self.__a = [a1, b1, c1]
            self.__z = list(zip(*self.__a))
            for i in range(len(self.__z)):
                self.__z[i] = str(self.__z[i][0] + self.__z[i][1] + self.__z[i][2])
                i -= i

        if self.__frame == 2:
            a1 = self.__a[1:(len(self.__a) - 1):3]
            b1 = self.__a[2:(len(self.__a) - 1):3]
            c1 = self.__a[3:(len(self.__a)):3]
            self.__a = [a1, b1, c1]
            self.__z = list(zip(*self.__a))
            for i in range(len(self.__z)):
                self.__z[i] = str(self.__z[i][0] + self.__z[i][1] + self.__z[i][2])
                i -= i

        if self.__frame == 3:
            a1 = self.__a[2:(len(self.__a) - 1):3]
            b1 = self.__a[3:(len(self.__a) - 1):3]
            c1 = self.__a[4:(len(self.__a)):3]
            self.__a = [a1, b1, c1]
            self.__z = list(zip(*self.__a))
            for i in range(len(self.__z)):
                self.__z[i] = str(self.__z[i][0] + self.__z[i][1] + self.__z[i][2])
                i -= i

        return self.__z


    def traduzir_codons(self):

        self.p = []
        if self.__nletras == 3:
            for i in range(len(self.__z)):
                if self.__z[i] in self.ALA:
                    self.p.append('ALA')
                elif self.__z[i] in self.ARG:
                    self.p.append('ARG')
                elif self.__z[i] in self.ASN:
                    self.p.append('ASN')
                elif self.__z[i] in self.ASP:
                    self.p.append('ASP')
                elif self.__z[i] in self.CYS:
                    self.p.append('CYS')
                elif self.__z[i] in self.GLN:
                    self.p.append('GLN')
                elif self.__z[i] in self.GLU:
                    self.p.append('GLU')
                elif self.__z[i] in self.GLY:
                    self.p.append('GLY')
                elif self.__z[i] in self.HIS:
                    self.p.append('HIS')
                elif self.__z[i] in self.ILE:
                    self.p.append('ILE')
                elif self.__z[i] in self.LEU:
                    self.p.append('LEU')
                elif self.__z[i] in self.LYS:
                    self.p.append('LYS')
                elif self.__z[i] in self.MET:
                    self.p.append('(_MET_)')
                elif self.__z[i] in self.PHE:
                    self.p.append('PHE')
                elif self.__z[i] in self.PRO:
                    self.p.append('PRO')
                elif self.__z[i] in self.SER:
                    self.p.append('SER')
                elif self.__z[i] in self.THR:
                    self.p.append('THR')
                elif self.__z[i] in self.TRP:
                    self.p.append('TRP')
                elif self.__z[i] in self.TYR:
                    self.p.append('TYR')
                elif self.__z[i] in self.VAL:
                    self.p.append('VAL')
                elif self.__z[i] in self.PRD:
                    self.p.append('|STOP|')
                i -= i
        elif self.__nletras == 1:
            for i in range(len(self.__z)):
                if self.__z[i] in self.ALA:
                    self.p.append('A')
                elif self.__z[i] in self.ARG:
                    self.p.append('R')
                elif self.__z[i] in self.ASN:
                    self.p.append('N')
                elif self.__z[i] in self.ASP:
                    self.p.append('D')
                elif self.__z[i] in self.CYS:
                    self.p.append('C')
                elif self.__z[i] in self.GLN:
                    self.p.append('Q')
                elif self.__z[i] in self.GLU:
                    self.p.append('E')
                elif self.__z[i] in self.GLY:
                    self.p.append('G')
                elif self.__z[i] in self.HIS:
                    self.p.append('H')
                elif self.__z[i] in self.ILE:
                    self.p.append('I')
                elif self.__z[i] in self.LEU:
                    self.p.append('L')
                elif self.__z[i] in self.LYS:
                    self.p.append('K')
                elif self.__z[i] in self.MET:
                    self.p.append('(M)')
                elif self.__z[i] in self.PHE:
                    self.p.append('F')
                elif self.__z[i] in self.PRO:
                    self.p.append('P')
                elif self.__z[i] in self.SER:
                    self.p.append('S')
                elif self.__z[i] in self.THR:
                    self.p.append('T')
                elif self.__z[i] in self.TRP:
                    self.p.append('W')
                elif self.__z[i] in self.TYR:
                    self.p.append('Y')
                elif self.__z[i] in self.VAL:
                    self.p.append('V')
                elif self.__z[i] in self.PRD:
                    self.p.append('|STOP|')
        return self.p

    def print_dupla_fita(self):
        for i in range(len(self.__sequp)):
            self.__dpl1.append(self.__sequp[i])
            i -= i
        for i in range(len(self.__dpl1)):
            if self.__dpl1[i] == 'A':
                self.__dpl2.append('T')
            elif self.__dpl1[i] == 'T':
                self.__dpl2.append('A')
            elif self.__dpl1[i] == 'G':
                self.__dpl2.append('C')
            elif self.__dpl1[i] == 'C':
                self.__dpl2.append('G')
            i-=i
        x = '{}\n{}\n{}\n{}'.format(''.join(self.__dpl1),('|'*len(self.__dpl1)),('|' *len(self.__dpl1)), ''.join(self.__dpl2))
        return x

if __name__ == '__main__':
    seq = 'ATGCTAGGTAACAAGCGACTGGGGCTGTCCGGACTGACCCTCGCCCTGTCCCTGCTCGTGTGCCTGGGTGCGCTGGCCGAGGCGTACCCCTCCAAGCCGGACAACCCGGGCGAGGACGCACCAGCGGAGGACATGGCCAGATACTACTCGGCGCTGCGACACTACATCAACCTCATCACCAGGCAGAGATATGGAAAACGATCCAGCCCAGAGACACTGATTTCAGACCTCTTGATGAGAGAAAGCACAGAAAATGTTCCCAGAACTCGGCTTGAAGACCCTGCAATGTGGTGATGGGAAATGAGACTTGCTCTCTGGCCTTTTCCTATTTT'
    f1 = Enggen(seq,1,1)
    f2 = Enggen(seq,2,1)
    f3 = Enggen(seq,3,1)
    f1.transcricao()
    f2.transcricao()
    f3.transcricao()
    f1.sepcodons()
    f2.sepcodons()
    f3.sepcodons()
    res1 = f1.traduzir_codons()
    res2 = f2.traduzir_codons()
    res3 = f3.traduzir_codons()
    x = 80*'='
    print(x)
    print(' '.join(res1))
    print(x)
    print(' '.join(res2))
    print(x)
    print(' '.join(res3))
    print(x)
    print(f1.print_dupla_fita())
    
