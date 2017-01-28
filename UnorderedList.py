class Node:
    def __init__(self, item):
        self.item = item
        self.nextNode = None

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, node):
        self.nextNode = node

    def getItem(self):
        return self.item

    def setItem(self, item):
        self.item = item


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNextNode(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNextNode()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getItem() == item:
                found = True
            current = current.getNextNode()
        return found

    def printL(self):
        current = self.head

        while current != None:
            i = str(current.getItem())
            print(i+" ")
            current = current.getNextNode()


mylist = UnorderedList()
mylist.add(7)
mylist.add(8)
mylist.add(9)
mylist.add(0)

mylist.printL()
print(mylist.search(10))
print(mylist.size())
print(mylist.isEmpty())



