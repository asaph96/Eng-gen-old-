def sepcodonsf1(seq):

    try:
        
        b = []
        for i in range(len(seq)):
            if i%3==0:
                    b.append(a[i]+a[i+1]+a[i+2])
                    i-=i
            else:
                    pass

    except NameError:

        b = []
        for i in range(len(seq)):
            if i%3==0:
                    b.append(a[i]+a[i+1]+a[i+2])
                    i-=i
            else:
                    pass
##########################################################
def sepcodonsf2(seq):

    try:
        
        b=[]
        for i in range(len(seq)):
            if i%3==0:
                    b.append(a[i+1]+a[i+2]+a[i+3])
                    i-=i
            else:
                    pass

    except NameError:
        
        b=[]
        for i in range(len(seq)):
            if i%3==0:
                    b.append(a[i+1]+a[i+2]+a[i+3])
                    i-=i
            else:
                    pass
############################################################
def sepcodonsf3(seq):

    try:
        
        b=[]
        for i in range(len(seq)):
            if i%3==0:
                    b.append(a[i+2]+a[i+3]+a[i+4])
                    i-=i
            else:
                    pass
                
    except NameError:
        
        b=[]
        for i in range(len(seq)):
            if i%3==0:
                    b.append(a[i+2]+a[i+3]+a[i+4])
                    i-=i
            else:
                    pass
