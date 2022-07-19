
class Node:
	def __init__(self, value):
		self.value = value
		self.leftChild = None
		self.rightChild = None
		
	def inserir(self, data):
		if self.value == data:
			return False
			
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.inserir(data)
			else:
				self.leftChild = Node(data)
				return True

		else:
			if self.rightChild:
				return self.rightChild.inserir(data)
			else:
				self.rightChild = Node(data)
				return True
				
	def encontrar(self, data):
		if(self.value == data):
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.encontrar(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.encontrar(data)
			else:
				return False

	def preordem(self):
		if self:
			print (str(self.value))
			if self.leftChild:
				self.leftChild.preordem()
			if self.rightChild:
				self.rightChild.preordem()