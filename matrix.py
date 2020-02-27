"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

def make_translate( x, y, z ):
    translate = new_matrix()
    ident(translate)
    translate[0][3] = x
    translate[1][3] = y
    translate[2][3] = z
    return translate

def make_scale( x, y, z ):
    scale = new_matrix()
    ident(scale)
    scale[0][0] = x
    scale[1][1] = y
    scale[2][2] = z
    return scale

def make_rotX( theta ):
    rotate = new_matrix()
    ident(rotate)
    rotate[1][1] = math.cos(math.radians(theta))
    rotate[1][2] = -1*math.sin(math.radians(theta))
    rotate[2][1] = math.sin(math.radians(theta))
    rotate[2][2] = math.cos(math.radians(theta))
    return rotate

def make_rotY( theta ):
    rotate = new_matrix()
    ident(rotate)
    rotate[0][0] = math.cos(math.radians(theta))
    rotate[0][2] = math.sin(math.radians(theta))
    rotate[2][0] = -1*math.sin(math.radians(theta))
    rotate[2][2] = math.cos(math.radians(theta))
    return rotate

def make_rotZ( theta ):
    rotate = new_matrix()
    ident(rotate)
    rotate[0][0] = math.cos(math.radians(theta))
    rotate[0][1] = -1*math.sin(math.radians(theta))
    rotate[1][0] = math.sin(math.radians(theta))
    rotate[1][1] = math.cos(math.radians(theta))
    return rotate

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print(s)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
