'''
The goal of this program is not to generate a single type of carbon
nanotube. Instead, it is a general set of functions to generate any carbon
nanotube as need-be.

Geometric definitions are from Yengejeh, Kazemi, and Öchsner, "A Primer
on the Geometry of Nanotubes." Springer, 2018; and Qin, "Determination of
the chiral indicies (n, m) of carbon nanotubes by electron diffraction."
RSC Physical Chemistry Chemical Physics, 2006. doi:10.1039/b614121h.
'''
import numpy as np

a = 1/np.sqrt(3) # Lattice constant of graphene. (~0.246 nm)

'''
Rather than attempt to build a graphene lattice and fold it---as is commonly
described in literature---I'll create a carbon "ring" of sorts, and then
rotate that with a fixed angle, determined by the n and m indices.
'''

def chiralVector(n, m): # Define the chiral vector for the atoms.
    return a*n + a*m

'''
helicity(n, m)---taken from Qun (2006)---is essentially the angle of 
rotation for each graphene ring.
'''

def helicity(n, m):
    return np.arctan( m / (a * (2 * n + m)) )

'''
Define the diameter of the carbon nanotube
'''

def radius(n, m):
    return ( a / (2 * np.pi) ) * np.sqrt(n**2 + n*m + m**2)

'''
Now create three basis vectors that will generate a graphene unit cell.
'''

def basisOne(n, m):
    alpha = helicity(n, m)
    j = n + m - 1
    y10 = []
    y11 = []
    b = 6/np.pi
    c = np.sqrt(3)
    x10 = j * a * np.cos(alpha)# x values
    z10 = -j * a * np.sin(alpha)# z values
    x11 = x10 - (a/c) * np.cos(b - alpha)
    z11 = z10 - (a/c) * np.sin(b - alpha)
    y10.append( [x10, z10] )
    y11.append([x11, z11])
    return [y10, y11]

def basisTwo(n, m):
    alpha = helicity(n, m)
    b = np.pi/3
    c = np.sqrt(3)
    j = 2 * n - m - 1
    y20 = []
    y21 = []
    x20 = j * a * np.cos(b - alpha)
    z20 = -j * a * np.sin(b - alpha)
    x21 = x20 + (a / c) * np.sin(alpha)
    z21 = z20 - (a / c) * np.cos(alpha)
    y20.append([x20, z20])
    y21.append([x21, z21])
    return [y20, y21]

def basisThree(n, m):
    alpha = helicity(n, m)
    b = np.pi/6
    c = np.sqrt(3)
    j = 2*n + m - 1
    y30 = []
    y31 = []
    x30 = -j * a * np.sin(b - alpha)
    z30 = j * a * np.cos(b - alpha)
    x31 = x30 + (a / c) * np.sin(b + alpha)
    z31 = z30 + (a / c) * np.cos(b + alpha)
    y30.append([x30, z30])
    y31.append([x31, z31])
    return [y30, y31]

