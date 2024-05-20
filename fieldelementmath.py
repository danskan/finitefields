from finitefields import FieldElement

print(f'Defining a as field element 7 and 13, for example')
a=FieldElement(7, 13)

print(f'Defining b as field element 6 and 13, for example')
b=FieldElement(6, 13)

print(f'Checking if a is equal to b')
print(a==b)

print(f'Checking if a is equal to a')
print(a==a)

print(f'Checking if b is equal to b')
print(b==b)

print(f'Now let\'s do some math')
print(f'If finite field prime=13 has 7 and 12 in it, what is 7 plus 12?')
a = FieldElement(7,13)
b= FieldElement(12,13)
c = FieldElement(6,13)
print(a+b)
print(a-b)

print(f'pause')
