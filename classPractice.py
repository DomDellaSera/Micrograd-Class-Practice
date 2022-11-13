class Value:
    #Self is roughly eqivalant to this, 
    #__init__ is the constructor
    def __init__(self, data):
        self.data = data
    #repr is the toString override
    def __repr__(self):
    #Is this constructing a new object every time?
        return f"Value(data={self.data})"
        
    def __add__(self, other):
        out = Value(self.data + other.data)
        return out
        
    def __mul__(self, other):
        out = Value(self.data * other.data)
        return out
        
   
        
    def toComplex(self):
        return complex(self.data, 0)
        
    def toConjugateTranspose(self):
    #d/dx cos x + i sin x = -sinx + i cos x
  #  Theorem 1: A complex function f(z)=u(x,y)+iv(x,y) has a
  #complex derivative f′(z) if and only if its real and imaginary part are
#  continuously differentiable and satisfy the Cauchy-Riemann equations
#(whatever the hell that means)

    #It means a holomorphic function
        #It means complex analytic
#ux=vy,uy=−vx

#where ux(x0,y0) and vx(x0,y0) denote the first-order partial derivatives 
#with respect to x of the function u and v, 

#In this case, the complex derivative of f(z) is equal to any of the following expressions:
#f′(z)=ux+ivx=vy−iuy.−iuy.
        print("ConjTrans", self.toComplex().imag)
        #return toComplex(-self.)
        
        
a = Value(2.0)

b = Value(-3.0)

#a.setOtherData(5)
#a.getOtherData
#print(a.getOtherData())
#print(a.toComplex())
#print(a.toConjugateTranspose())

print(a+b)
print(a*b)
