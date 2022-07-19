from Node import Node

class Tree:
	def __init__(self):
		self.root = None

	def inserir(self, data):
        ## insere se houver raiz
		if self.root:
			return self.root.inserir(data)
        ## insere se não houver raiz prédeterminada
		else:
			self.root = Node(data)
			return True

	def encontrar(self, data):
        ## encontra se houver raiz
		if self.root:
			return self.root.encontrar(data)
        ## retorna se não houver raiz no objeto árvore
		else:
			return False
	
	def remover(self, data):
		# caso a árvore esteja vazia
		if self.root is None:
			return False
			
		# caso o nodo seja a própria raiz	
		elif self.root.value == data:
			if self.root.leftChild is None and self.root.rightChild is None:
				self.root = None
			elif self.root.leftChild and self.root.rightChild is None:
				self.root = self.root.leftChild
			elif self.root.leftChild is None and self.root.rightChild:
				self.root = self.root.rightChild
			elif self.root.leftChild and self.root.rightChild:
				delNodeParent = self.root
				delNode = self.root.rightChild
				while delNode.leftChild:
					delNodeParent = delNode
					delNode = delNode.leftChild
					
				if delNode.rightChild:
					if delNodeParent.value > delNode.value:
						delNodeParent.leftChild = delNode.rightChild
					elif delNodeParent.value < delNode.value:
						delNodeParent.rightChild = delNode.rightChild
				else:
					if delNode.value < delNodeParent.value:
						delNodeParent.leftChild = None
					else:
						delNodeParent.rightChild = None
				self.root.value = delNode.value
						
			return True
		
		parent = None
		node = self.root
		
		# encontrar o node que deve ser removido
		while node and node.value != data:
			parent = node
			if data < node.value:
				node = node.leftChild
			elif data > node.value:
				node = node.rightChild
		
		# caso 1: valor não foi encontrado na árvore
		if node is None or node.value != data:
			return False
			
		# caso 2: remover o node, caso não haja filhos
		elif node.leftChild is None and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = None
			else:
				parent.rightChild = None
			return True
			
		# caso 3: remover o node caso só exista leftChild
		elif node.leftChild and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = node.leftChild
			else:
				parent.rightChild = node.leftChild
			return True
			
		# caso 4: remover o node caso só exista rightChild
		elif node.leftChild is None and node.rightChild:
			if data < parent.value:
				parent.leftChild = node.rightChild
			else:
				parent.rightChild = node.rightChild
			return True
			
		# caso 5: remover o node que possui ambos os filhos
		else:
			delNodeParent = node
			delNode = node.rightChild
			while delNode.leftChild:
				delNodeParent = delNode
				delNode = delNode.leftChild
				
			node.value = delNode.value
			if delNode.rightChild:
				if delNodeParent.value > delNode.value:
					delNodeParent.leftChild = delNode.rightChild
				elif delNodeParent.value < delNode.value:
					delNodeParent.rightChild = delNode.rightChild
			else:
				if delNode.value < delNodeParent.value:
					delNodeParent.leftChild = None
				else:
					delNodeParent.rightChild = None

	def preordem(self):
		if self.root is not None:
			print("PreOrder")
			self.root.preordem()
