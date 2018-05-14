j = 0
k = 0
b = ""

def ends(s,j): #s itu suffix/prefix('meng','ku',dll)
    l = len(s)
    o = self.k-l
    o += 1
    for i in range(0,l):
        if (b[o+i] != s[i]):
            return False

    j = k - l
    return True

def starts(s):
    l = len(s)
    for i in range (0,l):
        if (b[i] != s[i]):
            return False

    return True

def cons(i):
    if (b[i]=="a" |
        b[i]=="e" |
        b[i]=="i" |
        b[i]=="o" |
        b[i]=="u"):
        return False
    return True

def m():
    n = 0
    i = 0
    while (True):
        if (i > j):
            return n
        if (not cons(i)):
            break
        i+=1
    i+=1
    while (True):
        while (True):
            if (i > j):
                return n
            if (cons(i)):
                break
            i+=1
        i+=1
        n+=1
        while (True):
            if (i > j):
                return n
            if (not cons(i)):
                break
            i+=1
        i+=1

def setto(s, j, k):
    if (m() > 2):
        l = len(s)
        o = j
        o+=1
        for i in range(0,l):
            b[o+i] = s[i]
        k = j+l

def startsv(s):
    l = len(s)
    o = l
    o -= 1
    if (not cons(o)):
        return True
    return False