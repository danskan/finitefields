# setting up field elements as a class object
class FieldElement:
    
    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime
    
    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __ne__(self, other):
        if self != other:
            return True
        else:
            return False
    
    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num)  % self.prime
        return self.__class__(num, self.prime)
print(f'pause1')

print(f'Now let\'s do some math')
a = FieldElement(7,13)
b= FieldElement(12,13)
c = FieldElement(6,13)
print(a+b==c)

print(f'pause2')
print(f'pause3')
