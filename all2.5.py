# -*- coding: utf-8 -*-

class Enggen(object):
    def __init__(self,seq,frame,nletras):
        self.seq = seq
        self.frame = frame
        self.y = self.seq
        self.nletras = nletras
        self.lista = self.seq
        self.z = self.seq
        self.x = self.seq

    @property
    def seq(self):
        return self.seq

    @seq.setter
    def seq(self, seq):
        self.seq = seq

    def retifica(self, y):
        self.a = []
        for i in range(len(y)):
            self.a.append(y[i].upper())
            i -= i

        for i in range(len(self.a)):
            if self.a[i] == 'T':
                self.a[i] = 'U'
            else:
                pass
            i -= i
        return self.a

    def sepcodons(self, x, frame):
        if self.frame == 1:
            self.a = x[0:(len(x) - 1):3]
            self.b = x[1:(len(x) - 1):3]
            self.c = x[2:(len(x)):3]
            x = [self.a, self.b, self.c]
            self.z = list(zip(*x))
            for i in range(len(self.z)):
                self.z[i] = str(self.z[i][0] + self.z[i][1] + self.z[i][2])
                i -= i

        if self.frame == 2:
            self.a = x[1:(len(x) - 1):3]
            self.b = x[2:(len(x) - 1):3]
            self.c = x[3:(len(x)):3]
            x = [self.a, self.b, self.c]
            self.z = list(zip(*x))
            for i in range(len(self.z)):
                self.z[i] = str(self.z[i][0] + self.z[i][1] + self.z[i][2])
                i -= i

        if self.frame == 3:
            self.a = x[2:(len(x) - 1):3]
            self.b = x[3:(len(x) - 1):3]
            self.c = x[4:(len(x)):3]
            x = [self.a, self.b, self.c]
            self.z = list(zip(*x))
            for i in range(len(self.z)):
                self.z[i] = str(self.z[i][0] + self.z[i][1] + self.z[i][2])
                i -= i

        return self.z

    def verifaug(self, z):
        if 'aug' not in z:
            print('A sequência não contem um "start códon"')
            return False
        else:
            return True

    def traduzir_codons(self, lista, nletras):
        self.ALA = 'GCU', 'GCC', 'GCA', 'GCG'
        self.ARG = 'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'
        self.ASN = 'AAU', 'AAC'
        self.ASP = 'GAU', 'GAC'
        self.CYS = 'UGU', 'UGC'
        self.GLN = 'CAA', 'CAG'
        self.GLU = 'GAA', 'GAG'
        self.GLY = 'GGU', 'GGC', 'GGA', 'GGG'
        self.HIS = 'CAU', 'CAC'
        self.ILE = 'AUU', 'AUC', 'AUA'
        self.LEU = 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'
        self.LYS = 'AAA', 'AAG'
        self.MET = 'AUG'
        self.PHE = 'UUU', 'UUC'
        self.PRO = 'CCU', 'CCC', 'CCA', 'CCG'
        self.SER = "UCU", 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'
        self.THR = 'ACU', 'ACC', 'ACA', 'ACG'
        self.TRP = 'UGG'
        self.TYR = 'UAU', 'UAC'
        self.VAL = 'GUU', 'GUC', 'GUA', 'GUG'
        self.PRD = 'UAG', 'UGA', 'UAA'

        self.z = []
        if self.nletras == 3:
            for i in range(len(self.lista)):
                if self.lista[i] in self.ALA:
                    self.z.append('ALA')
                elif self.lista[i] in self.ARG:
                    self.z.append('ARG')
                elif self.lista[i] in self.ASN:
                    self.z.append('ASN')
                elif self.lista[i] in self.ASP:
                    self.z.append('ASP')
                elif self.lista[i] in self.CYS:
                    self.z.append('CYS')
                elif self.lista[i] in self.GLN:
                    self.z.append('GLN')
                elif self.lista[i] in self.GLU:
                    self.z.append('GLU')
                elif self.lista[i] in self.GLY:
                    self.z.append('GLY')
                elif self.lista[i] in self.HIS:
                    self.z.append('HIS')
                elif self.lista[i] in self.ILE:
                    self.z.append('ILE')
                elif self.lista[i] in self.LEU:
                    self.z.append('LEU')
                elif self.lista[i] in self.LYS:
                    self.z.append('LYS')
                elif self.lista[i] in self.MET:
                    self.z.append('MET')
                elif self.lista[i] in self.PHE:
                    self.z.append('PHE')
                elif self.lista[i] in self.PRO:
                    self.z.append('PRO')
                elif self.lista[i] in self.SER:
                    self.z.append('SER')
                elif self.lista[i] in self.THR:
                    self.z.append('THR')
                elif self.lista[i] in self.TRP:
                    self.z.append('TRP')
                elif self.lista[i] in self.TYR:
                    self.z.append('TYR')
                elif self.lista[i] in self.VAL:
                    self.z.append('VAL')
                elif self.lista[i] in self.PRD:
                    self.z.append('STOP')
                i -= i
        elif self.nletras == 1:
            for i in range(len(self.lista)):
                if self.lista[i] in self.ALA:
                    self.z.append('A')
                elif self.lista[i] in self.ARG:
                    self.z.append('R')
                elif self.lista[i] in self.ASN:
                    self.z.append('N')
                elif self.lista[i] in self.ASP:
                    self.z.append('D')
                elif self.lista[i] in self.CYS:
                    self.z.append('C')
                elif self.lista[i] in self.GLN:
                    self.z.append('Q')
                elif self.lista[i] in self.GLU:
                    self.z.append('E')
                elif self.lista[i] in self.GLY:
                    self.z.append('G')
                elif self.lista[i] in self.HIS:
                    self.z.append('H')
                elif self.lista[i] in self.ILE:
                    self.z.append('I')
                elif self.lista[i] in self.LEU:
                    self.z.append('L')
                elif self.lista[i] in self.LYS:
                    self.z.append('K')
                elif self.lista[i] in self.MET:
                    self.z.append('M')
                elif self.lista[i] in self.PHE:
                    self.z.append('F')
                elif self.lista[i] in self.PRO:
                    self.z.append('P')
                elif self.lista[i] in self.SER:
                    self.z.append('S')
                elif self.lista[i] in self.THR:
                    self.z.append('T')
                elif self.lista[i] in self.TRP:
                    self.z.append('W')
                elif self.lista[i] in self.TYR:
                    self.z.append('Y')
                elif self.lista[i] in self.VAL:
                    self.z.append('V')
                elif self.lista[i] in self.PRD:
                    self.z.append('STOP')
        return self.z


##seq = (input('Digite sua sequência\n=> '))
##ret = retifica(seq)
### print(ret)
##cdnsf1 = sepcodons(ret, 1)
##cdnsf2 = sepcodons(ret, 2)
##cdnsf3 = sepcodons(ret, 3)
##a = traduzir_codons(cdnsf1, 1)
##b = traduzir_codons(cdnsf2, 1)
##c = traduzir_codons(cdnsf3, 1)
##print(a)
##print(b)
##print(c)

if __name__ == '__main__':
    fasta = Enggen("""ATGAAAACTATCGTGGTTATTTTTGCCTTTTGCATTTGCGTTAATGCAATGACAATTGAAGAATTGAAAATCCAATTACATGATGTGCAGGAAATTTGCAAGACAGAATCTGGCATTGATCAGCAAACAGTAGATGACATTAATGAAGTGAACTTCGATGTAGAAGATGAGAAACCTCAACGCTACAATGAATGCATACTAAAACAATTCAATATTGTTGATGAGAGTGGAAACTTTAAGGAAAATATCGTTCAAGAACTAACGAGTATATATTTAGATGAAAATGTAATTAAGAAATTAGTCGCCGAATGTTCGGTTATCTCTGATGCCAATATATATATAAGATTTAATAAACTAGTGAAGTGTTTTGGAAAATATAAAACAATGAAAGAAGTATTAAATCTCTAAATATTCAATTATTAAAAGAAAAAGAGATTTATTTATAATACAATATATTTTTTAACTTTGATTATACTTTTTAACTTTGAAAATATTTAAAAAATTATATCAATAAATTAATATACGATTACTTA""",1,1)

