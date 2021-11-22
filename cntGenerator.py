# The goal of this program is not to generate a single type of carbon
# nanotube. Instead, it is a general set of functions to generate any carbon
# nanotube as need-be.
#
# Geometric definitions are from Yengejeh, Kazemi, and Öchsner, "A Primer
# on the Geometry of Nanotubes." Springer, 2018; and Qin, "Determination of
# the chiral indicies (n, m) of carbon nanotubes by electron diffraction."
# RSC Physical Chemistry Chemical Physics, 2006. doi:10.1039/b614121h.

import numpy as np

a = 1/np.sqrt(3) # Lattice constant of graphene. (~0.246 nm)

# Rather than attempt to build a graphene lattice and fold it---as is 
# commonly described in literature---I'll create a carbon "ring" of sorts, 
# and then rotate that with a fixed angle, determined by the n and m 
# indices.

def chiralVector(n, m): # Define the chiral vector for the atoms.
    return a*n + a*m

# helicity(n, m)---taken from Qun (2006)---is essentially the angle of 
# rotation for each graphene ring.

def helicity(n, m):
    return np.arctan( m / (a * (2 * n + m)) )

# Define the radius of the carbon nanotube

def radius(n, m):
    return ( a / (2 * np.pi) ) * np.sqrt(n**2 + n*m + m**2)


# Now create three basis vectors that will generate a graphene unit cell.
#
# A basis vector, b[i][j], consists of two parts:
#     - i, which determines the x-, or z-axis,
#     - j, which is an x-, or z-value.
# Luckily, there are only four states for a basis vector:
#     - b[0][0]---the first x-value;
#     - b[0][1]---the second x-value;
#     - b[1][0]---the first z-value;
#     - b[1][1]---the second z-value.


def basisOne(n, m):
    alpha = helicity(n, m)
    j = n + m - 1
    x = []
    z = []
    b = 6/np.pi
    c = np.sqrt(3)
    x10 = j * a * np.cos(alpha)# x values
    z10 = -j * a * np.sin(alpha)# z values
    x11 = x10 - (a/c) * np.cos(b - alpha)
    z11 = z10 - (a/c) * np.sin(b - alpha)
    x.append(x10)
    x.append(x11)
    z.append(z10)
    z.append(z11)
    return [x, z]

def basisTwo(n, m):
    alpha = helicity(n, m)
    b = np.pi/3
    c = np.sqrt(3)
    j = 2 * n - m - 1
    x = []
    z = []
    x20 = j * a * np.cos(b - alpha)
    z20 = -j * a * np.sin(b - alpha)
    x21 = x20 + (a / c) * np.sin(alpha)
    z21 = z20 - (a / c) * np.cos(alpha)
    x.append(x20)
    x.append(x21)
    z.append(z20)
    z.append(z21)
    return [x, z]

def basisThree(n, m):
    alpha = helicity(n, m)
    b = np.pi/6
    c = np.sqrt(3)
    j = 2*n + m - 1
    x = []
    z = []
    x30 = -j * a * np.sin(b - alpha)
    z30 = j * a * np.cos(b - alpha)
    x31 = x30 + (a / c) * np.sin(b + alpha)
    z31 = z30 + (a / c) * np.cos(b + alpha)
    x.append(x30)
    x.append(x31)
    z.append(z30)
    z.append(z31)
    return [x, z]


# The totalCell(n, m) function, as you can see below, is horrific. I don't
# know how for loops work, and at this point, I'm too afraid to ask.

def totalCell(n, m):
    j = basisOne(n, m)
    k = basisTwo(n, m)
    l = basisThree(n, m)
    y = [j, k, l]
    x = []
    z = []
    w = 0
    while w < len(y):
        x.append(y[w][0][0])
        x.append(y[w][0][1])
        z.append(y[w][1][0])
        z.append(y[w][1][1])
        w+=1

    return [x, z]

# Now, with those basis vectors defined, we can begin to place them on a
# circle.
#
# Assume that a single unit cell is lying on a circle. Since the 
# circumference of a circle is C = [pi] * diameter, we can therefore assume 
# that the nanotube's circumference is
# C = 2[pi] * radius = (1/2) * a * sqrt(n^2 + nm + m^2)

def circumference(n, m):
    return 0.5 * a * np.sqrt(n**2 + n * m + m**2)

# This then allows us to put our unit cels onto a circle with an inscribed
# triangle problem.

