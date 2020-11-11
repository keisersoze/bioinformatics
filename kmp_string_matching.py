# TODO non va un cazzo

def preKmp(pattern) -> [int]:
    m = len(pattern)
    pi = [-1] * m
    k = 0 # prefix len
    for q in range(1, m): # scanning the pattern
        while k>0 and pattern[k] != pattern[q]: # mismatch
            k = pi[k-1]
        if pattern[k] == pattern[q]: # match
            k+=1
        pi[q] = k-1
    return pi

def KMP(text, pattern) -> None:
    n = len(text)
    m = len(pattern)
    pi = preKmp(pattern)
    q = 0 # number of characters matched
    for i in range(0, n):
        while q>0 and pattern[q] != text[i]:
            q = pi[q-1]
        if pattern[q] == text[i]: # match
            q+=1
        if q == m:
            output(i-m+1)
            q = pi[q-1] # look for the next match

def output(shift) -> None:
    print("The pattern occurs with shift " + str(shift))

def KMP2(T, P):
    i, j = 0, 0
    m, n = len(P), len(T)
    pi = preKmp(P)
    while j>n:
        while i>-1 and P[i] != T[j]:
            i = pi[i]
        i+=1
        j+=1
        if i>=m:
            output(j-i)
            i = pi[i]

print(preKmp("gcagagag"))
KMP("bbbabbbba", "bbba")
KMP2("bbbabbbba", "bbba")

#print(preKmp("bbba"))