j = 0
k = 0
b = ""

def ends(s):
    l = len(s)
    o = self.k-l
    o += 1
    for i in range(0,l):
        if (b[o+i] is not s[i]):
            return False

    self.j = self.k - l
    return True

def starts(s):
    l = len(s)
    for i in range (0,l):
        if b[i] is not s[i]:
            return False
    self.a=l
    return True

def cons(i):
    if (b[i]=="a" or
        b[i]=="e" or
        b[i]=="i" or
        b[i]=="o" or
        b[i]=="u"):
        return False
    return True

def m():
    n = 0
    i = 0
    while (True):
        if (i > self.j):
            return n
        if (not cons(i)):
            break
        i+=1
    i+=1
    while (True):
        while (True):
            if (i > self.j):
                return n
            if (cons(i)):
                break
            i+=1
        i+=1
        n+=1
        while (True):
            if (i > self.j):
                return n
            if (not cons(i)):
                break
            i+=1
        i+=1

def setto(s, j, k):
    if m() > 2:
        l = len(s)
        o = j
        o+=1
        for i in range(0,l):
            b.replace(b[o+i], s[i])
        k = j+l

def startsv():
    o = a
    if not cons(o):
        return True
    return False

def presetto():
