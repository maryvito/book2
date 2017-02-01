class BinaryTree:
    def __init__(self, rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None

    def addLeftChild(self, key):
        if self.leftChild == None:
            self.leftChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.leftChild = self.leftChild
            self.leftChild = t



    def addRightChild(self, key):
        if self.rightChild == None:
            self.rightChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.rightChild = self.rightChild
            self.rightChild = t



    def getRoot(self):
        return self.root

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRoot(self, obj):
        self.root = obj


def preorder(obj):
    if obj:
        print(obj.getRoot())
        preorder(obj.getLeftChild())
        preorder(obj.getRightChild())


bt = BinaryTree(0)

bt.addLeftChild(BinaryTree(-4))
bt.addLeftChild(BinaryTree(-2))
bt.addLeftChild(BinaryTree(-1))

bt.addRightChild(BinaryTree(7))
bt.addRightChild(BinaryTree(3))
bt.addRightChild(BinaryTree(1))

bt.getLeftChild().getLeftChild().addRightChild(-5)
bt.getLeftChild().addRightChild(-7)
bt.getLeftChild().addRightChild(-3)
bt.getLeftChild().getRightChild().addLeftChild(-6)

bt.getRightChild().getRightChild().addLeftChild(6)
bt.getRightChild().addLeftChild(4)
bt.getRightChild().addLeftChild(2)
bt.getRightChild().getLeftChild().addRightChild(5)



preorder(bt)



