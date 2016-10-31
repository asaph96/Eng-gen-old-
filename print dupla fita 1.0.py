def print_dupla_fita(self):
    self.__dpl1 = []
    self.__dpl2 = []

    for i in range(len(self.__a)):
        if self.__a[i] == 'U':
            self.__dpl1[i] = 'T'            
        else:
            self.__dpl1[i] = self.__a[i]    
        i-=i
    for i in range(len(self.__dpl1)):
        if self.__dpl1 == 'A':
            self.__dpl2 = 'T'
        elif self.__dpl1 == 'T':
            self.__dpl2 = 'A'
        elif self.__dpl1 == 'G':
            self.__dpl2 = 'C'
        elif self.__dpl1 == 'C':
            self.__dpl2 = 'G'
    
    x = '{}\n{}\n{}\n{}'.format(''.join(dpl1),|*len(self.__dpl1),|*len(self.__dpl1),''.join(dpl2))
