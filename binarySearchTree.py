class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def print(self):

        if self.root:
            self._print(self.root,0)
        else:
            print("Дерево пусто")


    def _print(self, current, n):

        print("_"+str(current.payload))
        if current.hasLeftChild():
            n+=2
            print(" "*n+"|")
            self._print(current.leftChild, n)
        else:
            n+=2
            print("|_")

        if current.hasRightChild():
            n-=2
            print(" "*n+"|")
            self._print(current.rightChild, n)
        else:
            n-=2
            print("|_")


    def put(self, key, payload):
        if self.root:
            self._put(self.root, key, payload)
        else:
            self.root = TreeNode(key, payload)
        self.size += 1

    def _put(self, currentNode, key, payload):
        if currentNode.key == key:
            currentNode.payload = payload

        elif key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(currentNode.leftChild, key, payload)
            else:
                currentNode.leftChild = TreeNode(key, payload, parent= currentNode)

        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(currentNode.rightChild, key, payload)
            else:
                currentNode.rightChild = TreeNode(key, payload, parent= currentNode)



class TreeNode:
    def __init__(self, key, payload, left= None, right= None, parent= None):
        self.key = key
        self.payload = payload
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return self.parent == None

    def isLeaf(self):
        return not (self.leftChild and self.rightChild)

    def hasAnyChild(self):
        return self.rightChild or self.leftChild

    def replaceNodeData(self, key, payload, lf, rt):
        self.key = key
        self.payload = payload
        self.leftChild = lf
        self.rightChild = rt
        if self.leftChild:
            self.leftChild.parent = self
        if self.rightChild:
            self.rightChild.parent = self





t = BinarySearchTree()
t.put(100, "R")
t.put(110, "right")
t.put(80, "left")
t.put(130, "N4")
t.put(120, "N3")
t.put(90, "N2")
t.put(70, "N1")
t.print()











