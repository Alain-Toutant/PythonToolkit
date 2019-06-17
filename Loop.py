# Loop.py
#
# Helper for C-Like for loops and non-standard ranges
#
# usage:
#
#    i = Loop()
#    while i.start(3).next(i**2).stop(10000):
#        print(i)
#
#    3
#    9
#    81
#    6561
#
# Functions of Loop
#
# Basic C-Like: while i.start(1).next(i+1).loop(i<10)
#
# - start(N)           Defines the starting value (can also be provided on constructor)
# - next(calculation)  Computes the next value
# - loop(condition)    Tests the looping condition (stops when false)
# 
# Other features
#
# - The class supports arithmetic operators
# - .value or uniary + : allows using the loop instance as a parameter
#
# Alternative looping function:
#
# - up(by=1)          short form of .next(i+1)
# - down(by=1)        short form of .next(i-1)
# - upTo(last,by=1)   short form of .next(i+1).loop(i<=last)
# - downTo(last,by=1) short form of .next(i-1).loop(i>=last)
# - until(condition)  alternative to loop(), check a stop condition instead
#                     of a "continue" condition. like .loop(not ...)

class Loop:
    def __init__(self,start=0):
        self._firstPass  = True
        self._value      = start

    @property
    def value(self): return self._value
        
    def start(self,initial):
        if self._firstPass : self._value = initial
        return self
    
    def next(self,nextValue=None):
        if nextValue is None : nextValue = self.value + self._increment
        if self._firstPass : self._firstPass = False
        else               : self._value = nextValue 
        return self

    def up(self,by=1):
        return self.next(self.value+by)
    def down(self,by=1):
        return self.next(self.value-by)

    def upTo(self,last,by=1):
        if self._firstPass: self._firstPass = False
        else: self._value  += by
        return self.value <= last

    def downTo(self,last,by=1):
        if self._firstPass: self._firstPass = False
        else: self._value  -= by
        return self.value >= last
    
    def loop(self,condition=True):
        self._firstPass = False
        return condition

    def until(self,condition=False):
        self._firstPass = False
        return not condition

    def __getitem__(self,index):     return self.value[index]
    def __str__(self):               return str(self.value)
    def __int__(self):               return int(self.value)
    def __float__(self):             return float(self.value)    
    def __add__(self,other):         return self.value + other
    def __sub__(self,other):         return self.value - other
    def __mul__(self,other):         return self.value * other
    def __matmul__(self,other):      return self.value.__matmul__(other)
    def __divmod__(self,other):      return divmod(self.value,other)
    def __pow__(self,other):         return self.value ** other
    def __truediv__(self,other):     return self.value / other
    def __floordiv__(self,other):    return self.value // other
    def __mod__(self,other):         return self.value % other
    def __lshift__(self,other):      return self.value << other
    def __rshift__(self,other):      return self.value >> other
    def __lt__(self,other):          return self.value < other
    def __le__(self,other):          return self.value <= other
    def __eq__(self,other):          return self.value == other
    def __ne__(self,other):          return self.value != other
    def __gt__(self,other):          return self.value > other
    def __ge__(self,other):          return self.value >= other
    def __and__(self,other):         return self.value & other
    def __or__(self,other):          return self.value | other
    def __xor__(self,other):         return self.value ^ other
    def __invert__(self):            return -self.value
    def __neg__(self):               return -self.value
    def __pos__(self):               return self.value
    def __abs__(self):               return abs(self.value)    
    def __radd__(self, other):       return other + self.value 
    def __rsub__(self, other):       return other - self.value
    def __rmul__(self, other):       return other * self.value
    def __rmatmul__(self, other):    return other.__matmul__(self.value)
    def __rtruediv__(self, other):   return other / self.value
    def __rfloordiv__(self, other):  return other // self.value
    def __rmod__(self, other):       return other % self.value
    def __rdivmod__(self, other):    return divmod(other,self.value)
    def __rpow__(self, other):       return other ** self.value
    def __rlshift__(self, other):    return other << self.value
    def __rrshift__(self, other):    return other >> self.value
    def __rand__(self, other):       return other & self.value
    def __rxor__(self, other):       return other ^ self.value
    def __ror__(self, other):        return other | self.value

if __name__ == "__main__":
    i = Loop()
    while i.start(100).next(i//2).loop(i>2):
        print(+i)
        for j in range(+i,i+5): print("  ",j)
    print("")
    i = Loop(start=100)
    while i.next(i/2).until(i<=2):
        print(i)
    print("")
    i = Loop()
    while i.start(1).upTo(10):
        print(i) # 1,2,...,9,10
    print("")
    i = Loop()
    while i.upTo(100,by=5):
        print(i) # 0,5,10,15,20,...,95,100
    print("")
    i = Loop(100)
    while i.down(by=5).until(i<20):
        print(i) # 100,95,90,...,25,20
    print("")
    f = Loop(start=(1,1))
    while f.next((f[1],sum(f))).until(f[0] > 100):
        print(f[0])
