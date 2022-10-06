from math import sqrt

# verifie que c'est bien un triangle
'''
Avec a =(xa,ya)
b=(xb,yb) et c=(xc,yc)
'''
def iscoherent(a,b,c):
    res = True
    #Verifie que les trois points n'aient pas les mêmes coord
    if(a[0]==b[0])and (a[0]==c[0]) and (c[0]==b[0]) and (a[1]==b[1]) and (a[1]==c[1]) and (c[1]==b[1]):
        res=False
      #Verifie que  deux points n'aient pas les mêmes coord  
    if(a[0]==b[0])and (a[1]==b[1]):
        res=False
    if(c[0]==b[0])and (c[1]==b[1]):
        res=False
    if(a[0]==c[0])and (a[1]==c[1]):
        res=False
    #Verifie que les alignements points ne soient pas alignées
    xVectAB=b[0]-a[0]

    yVectAB=b[1]-a[1]

    xVectAC=c[1]-a[0]

    yVectAC=c[1]-a[1]

    if(xVectAB*yVectAC-xVectAC*yVectAB==0):
        res=False
    else :
        res = True
    
    return res
     
#Verifie que c'est bien un Triangle en fonction des longeurs
'''
a=longueur de ab
b=longueur de bc
c=longueur de ca
'''
def  iscoherentlong(a,b,c):
    res=True
    if a < (b+c) and b < (a+c) and c < (a+b) : 
        res= True
    else: 
        res=False
    return res

#Avec les points
a=[2, 7.5]
b=[1, 4]
c=[0, 3]
#print("Est coherent avec les points",icoherent(a,b,c))

#Avec les longueurs
ab=(sqrt((b[1]-a[1])**2+(b[0]-a[0])**2))
bc=(sqrt((c[1]-b[1])**2+(c[0]-b[0])**2))
ca=(sqrt((c[1]-a[1])**2+(c[0]-a[0])**2))
#print("Est coherent avec les longueurs",isCoherentLong(ab,bc,ca))


# verifie que c'est bien  iso
'''
a=longueur de ab
b=longueur de bc
c=longueur de ca
'''
def isisosceles(a,b,c):
    if a == b or b == c or c == a : 
        return True
    return False

# verifie que c'est bien équilateral
'''
a=longueur de ab
b=longueur de bc
c=longueur de ca
'''
def isequilateral(a,b,c):
    if a == b and b == c : 
        return True
    return False

## verifie que c'est bien un rectangle
'''
a=longueur de ab
b=longueur de bc
c=longueur de ca
'''

def isrectangle(a,b,c):
    if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b : 
        return True
    return False


def test_answer_iso():
    assert not(isisosceles(5,11,12))
    assert isisosceles(5,5,12)

def test_answer_rect():
    assert isrectangle(5,12,13)

def test_answer_equi():
    assert isequilateral(12,12,12)

def test_answer_coh():
    assert iscoherent(a,b,c)