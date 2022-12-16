from graphviz import Digraph

class Value:
    #Self is roughly eqivalant to this, 
    #__init__ is the constructor
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op
    #repr is the toString override
    def __repr__(self):
    #Is this constructing a new object every time?
        return f"Value(data={self.data})"
        
    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out
        
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
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
    
def trace(root):
    #Builds a set of all nodes and edges in a graphviz
    nodes, edges = set(), set()
    

    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges
 
    
def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir' : 'LR'}) ##LR = left to right
    
    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        
        #for any value in the graph, create a rectangular ('record') node for items
        dot.node(name = uid, label = "{ data %.4f }" % ( n.data, ), shape='record')
        #and connect this node to items
        dot.edge(uid + n._op, uid)
        
        for n1, n2 in edges:
       #Connect n1 to the op node of n2
            dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    return dot
       
       
       
        
a = Value(2.0)

b = Value(-3.0)

c = Value(10.0)

d = a*b + c
#a.setOtherData(5)
#a.getOtherData
#print(a.getOtherData())
#print(a.toComplex())
#print(a.toConjugateTranspose())


print(d)
print(d._prev)
print(d._op)

draw_dot(d)
