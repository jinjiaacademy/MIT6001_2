class Int_set(object):
	'''An Int_set is a set of integers'''
	# Information about the implementation (not the abstraction):
	# Value of a set is represented by a list of ins, self._vals.
	# Each int in a set occurs in self._vals exactly once.

	def __init__(self):
		'''Create an empty set of integers'''
		self._vals = []

	def insert(self, e):
		'''Assumes e is an integer and inserts e into self'''
		if e not in self._vals:
			self._vals.append(e)

	def member(self, e):
		'''Assumes e is an integer
		Returns True if e is in self, and False otherwise'''
		return e in self._vals

	def remove(self, e):
		'''Assumes e is an integer and removes e from self
		Raises ValueError if e is not in self'''
		try:
			self._vals.remove(e)
		except:
			raise ValueError(str(e) + ' not found')

	def get_members(self):
		'''Returns a list containing the elements of self._vals
		Nothing can be assumed about the order of the elements'''
		return self._vals[:]

	def union(self, other):
		'''Other is an Int_set
		mutates self so that it contains exactly the elements in self
		plus the elements in other'''
		for e in other:
			if e not in self._vals:
				self._vals.append(e) 
		'''Replace the union method you added to Int_set by a method 
		that allows clients of Int_set to use the ­+ operator to denote 
		set union.'''
		# new_Int_set = Int_set()
		# new_Int_set._vals = [{self._vals + other._vals}]
		# return new_Int_set

	def __str__(self):
		'''Returns a string representation of self'''
		if self._vals == []:
			return '{}'
		self._vals.sort()
		result = ''
		for e in self._vals:
			result += str(e) + ','
		return f'{{{result[:-1]}}}'