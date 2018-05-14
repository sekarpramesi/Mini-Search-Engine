#helper

#endhelper

class Stemmer(object):
    i = 0#index pertama
    a=0#pointer index pertama setelah dipotong(atau setiap melalui proses starts)
    j = 0 #pointer index terakhir setelah dipotong(atau setiap melalui proses ends)
    k = 0#index terakhir
    b=""#kata

    def __init__(self, arg):#menset ulang variabel i,i_ends,j,k,b
        self.b=arg
        self.k=len(arg)-1

    #helper
    def ends(self, s):
        l = len(s)
        o = self.k - l
        o += 1

        print("ends")
        print("s = " + s)
        print("b = " + self.b)
        print("l = " + str(l))
        print("k = " + str(self.k))
        print("o = " + str(o))
        for i in range(0, l):
            if self.b[o + i] is not s[i]:
                return False

        self.j = self.k - l
        return True

    def starts(self, s):
        l = len(s)
        print("starts")
        print("s = " + s)
        print("b = " + self.b)
        print("l = " + str(l))
        for i in range(0, l):
            if self.b[i] is not s[i]:
                return False
        self.a = l
        return True

    def cons(self, i):
        if self.b[i] == "a" or self.b[i] == "e" or self.b[i] == "i" or self.b[i] == "o" or self.b[i] == "u":
            return False
        return True

    def m(self):
        n = 0
        i = 0

        while True:
            if i > self.j:
                return n
            if not self.cons(i):
                break
            i += 1
        i += 1
        while True:
            while True:
                if i > self.j:
                    return n
                if self.cons(i):
                    break
                i += 1
            i += 1
            n += 1
            while True:
                if i > self.j:
                    return n
                if not self.cons(i):
                    break
                i += 1
            i += 1

    def setto(self, s):
        if self.m() > 2:
            l = len(s)
            o = self.j
            o += 1
            for i in range(0, l):
                self.b.replace(self.b[o + i], s[i])
            k = self.j + l

    def presetto(self, s):
        self.b = s + self.b[(self.a):]
        self.k = self.k - self.a + len(s)

    def presetnull(self):
        self.b = self.b[(self.a):]
        self.k = self.k - self.a

    def startsv(self):
        o = self.a
        if not self.cons(o):
            return True
        return False
    #endhelper

    def step1(self):#done
        if self.ends('kah') or self.ends('lah') or self.ends('pun') or self.ends('tah'):
            print("yes")
            if self.m()>2:
                print("potong")
                self.k-=3

    def step2(self): #done
        if self.ends('ku') or self.ends('mu'):
            if self.m()>2:
                self.k-=2
        elif self.ends('nya'):
            if self.m()>2:
                self.k-=3

    def step3(self):#done
        if self.starts('meng'):
            self.presetnull()
        elif self.starts('meny'):
            if self.startsv():
                self.presetto('s')
        elif self.starts('men'):
            self.presetnull()
        elif self.starts('mem'):
            if self.startsv():
                self.presetto('p')
            else:
                self.presetnull()
        elif self.starts('me'):
            self.presetnull()
        else:
            print("step 3 gagal")
            return False

        print("step 3 berhasil")
        return True

    def step4(self, flag):#done
        if self.starts('per') or self.starts('pe') or self.starts('ber'):
            print("m  = " + str(self.m()))
            if(self.m()>2):
                self.presetnull()
        elif self.starts('pel') or self.starts('bel'):
            if (self.m() > 2):
                if self.ends('ajar'):
                    self.presetnull()
        elif self.starts('be'):
            if (self.m() > 2):
                if self.cons(self.a):
                #kalau 'er'
                    self.presetnull()
        if flag:
            if self.starts('peng') or self.starts('pen') or self.starts('pe'):
                if (self.m() > 2):
                    self.presetnull()
            elif self.starts('pem'):
                if (self.m() > 2):
                    if self.cons(self.a):
                        self.presetto('p')
                    else:
                        self.presetnull()
            elif self.starts('peny'):
                if (self.m() > 2):
                    if self.cons(self.a):
                        self.presetto('s')
                    else:
                        self.presetnull()

    def step5(self, flag):
        if self.ends('kan'):
            print("m =" + str(self.m()))
            if self.m()>2:
                self.k-=3
                print(self.k)
                self.b = self.b[:(self.k+1)]
        elif self.ends('i'):
            if self.m()>2:
                self.k-=1
                self.b = self.b[:(self.k+1)]
        elif self.ends('an'):
            if self.m()>2:
                self.k-=2
                self.b = self.b[:(self.k+1)]


    def stem(self):
        self.step1()
        self.step2()
        flag = self.step3()
        if flag:
            self.step4(flag)
            self.step5(flag)
        else:
            self.step5(flag)
            self.step4(flag)
        return self.b





b='mempermainkan'
stemmer = Stemmer(b)
stemword = stemmer.stem()
print(stemword)

