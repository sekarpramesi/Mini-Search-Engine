def m(self):
    n=0
    i=0
    temp=''
    flag = True
    t=0
    while i < self.j:
        if cons(i):
            temp='c'
        else:
            temp='v'
        if i>0:
            if (temp[i] == 'c' and temp[i-1] == 'v') or \
                (temp[i]=='v'and temp[i-1]=='c'):
                    t+=1
            elif temp[i] == 'c' and temp[i-1] == 'c':
                if (self.b[i-1]=='n' and self.b[i]=='g') or \
                    (self.b[i-1]=='n' and self.b[i]=='y') or \
                    (self.b[i-1]=='k' and self.b[i]=='h'):
                        t+=1
                else:
                    flag = False
            elif temp[i] == 'v' and temp[i-1] == 'v':
                flag=False

        if not flag:
            if t>0:
                n+=1
                t=0
                flag=True
    return n









