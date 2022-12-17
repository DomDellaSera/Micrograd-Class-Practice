import math

class Value:
    #Self is roughly eqivalant to this, 
    #__init__ is the constructor
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = 0.0
        # Stores how we are going to chain the outputs gradients into the inputs gradients
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __eq__(self, other):
        #This equal is going to be ill defined until I decide how "neurons" should be properly defined
        #I will define it initally for just the data for testing and it should be improved upon 
        return self.data == other.data
    def __hash__(self):
        return id(self.data)
        
    #repr is the toString override
    def __repr__(self):
    #Is this constructing a new object every time?
        return f"Value(data={self.data})"
        
    def __add__(self, other):
        #To allow us to write expressions such as Value(1.0) + 1 the below expression is added. Without the next line the evaluation adds an int to a Value object
        other = other if isinstance(other, Value) else Value(other)
        
        out = Value(self.data + other.data, (self, other), '+')
        
        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad
       # We don't want to call the function, we just want to store it so we're not calling _backward(). Calling the function returns nun
        out._backward = _backward
        return out
        
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')
        
        def _backward():
            #self.grad = self.data * other.data This is what I put initially. Is this the same as below?
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out
    
    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supporting int/float powers for now"
        out = Value(self.data**other, (self,), f'**{other}')
        
        def _backward():
            self.grad += other * (self.data **(other - 1)) * out.grad
        out._backward = _backward
        return out
        
    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)
        
        self.grad = 1.0
        
        for node in reversed(topo):
            node._backward()


    def __rmul__(self, other):
        return self * other
    def __radd__(self, other):
        return self + other
    
    def __truediv__(self, other): #self / other
        return self * other**-1
    
    def exp(self):
        x = self.data
        out = Value(math.exp(x), (self, ), 'exp')
        
        def _backward():
            self.grad = out.data * out.grad
        out._backward = _backward
        
        return out
    def tanh(self):
        x = self.data
        t = (math.exp(2*x) - 1)/(math.exp(2*x) + 1)
        
        out = Value(t, (self, ), label='tanh')
        
        def _backward():
            self.grad += (1 - t**2) * out.grad
        out._backward = _backward
        return out