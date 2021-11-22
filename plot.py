import matplotlib.pyplot as plt

exec( open('cntGenerator.py').read() )

def extractX(l, k):
    x = []
    i = len(l)
    j = 0
    while j < i:
        x.append( l[j][k][0] )
        j+=1
    return x

def extractY(l, k):
    y = []
    i = len(l)
    j = 0
    while j < i:
        y.append( l[j][k][1] )
        j+=1
    return x

n = 10
m = 10

