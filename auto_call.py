class Fraction():
	'''A number represented as a fraction.'''
	

	def __init__(self, num, denom):
		'''num and denom are integers'''
		assert type(num) == int and type(denom) == int
		self.num = num
		self.denom = denom

	def __str__(self):
		'''Returns string representation of a fraction.'''
		return f'{str(self.num)} / {str(self.denom)}'

	def __add__(self, other):
		'''Returns a new fraction representing the total.'''
		top = self.num*other.denom + self.denom*other.num
		bottom = self.denom*other.denom
		return Fraction(top, bottom)

	def __sub__(self, other):
		'''Returns a new fraction representing the difference.'''
		top = self.num*other.denom - self.denom*other.num
		bottom = self.denom*other.denom
		return Fraction(top, bottom)

	def __float__(self):
		'''Returns a float value of the fraction.'''
		return self.num / self.denom

	def inverse(self):
		'''Returns a new fraction representing the inverse fraction.'''
		return Fraction(self.denom, self.num)

a = Fraction(1, 4)
# The print function calls the __str__ method and prints the string. 
print(a)

b = Fraction(3, 4)
print(b)

# The + sign calls the __add__ method.
c = a + b
print(c)

# The float statement calls the float method.
print(float(c))

# This is an explicit call.
print(Fraction.__float__(c))

# The inverse method doesn't have preceding or trailing underscores.
# Thus they must be called like as would call a normal method. 
print(float(b.inverse()))

# The type of object
print(type(c))

# To check whether c is an instance of Fraction.
print(isinstance(c, Fraction))