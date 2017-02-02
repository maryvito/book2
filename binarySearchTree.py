class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

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

    def put(self):
        


