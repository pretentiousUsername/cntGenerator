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

x = []
y = []

a = basisOne(n, m)

for i in len( extractX(a, 0) ):

x.append( extractX(a, 0) )
y.append( extractY(a, 0) )


#plt.scatter(x, y)
#plt.savefig('plot.png')

