import random


class Node:
    def __init__(self, val=None):
        self.val = val
        self.leftNode = None
        self.rightNode = None

    def print_self(self):
        print(self.val)

    def addVal(self, newVal):
        if self.val:
            if self.val < newVal:
                if self.rightNode is not None:
                    self.rightNode.addVal(newVal)
                else:
                    self.rightNode = Node(newVal)
            else:
                if self.leftNode is not None:
                    self.leftNode.addVal(newVal)
                else:
                    self.leftNode = Node(newVal)
        else:
            self.val = newVal

    def printTree(self, level):
        if self.leftNode:
            self.leftNode.printTree(level + 1)
        print("Level:", level, "value:", self.val)
        if self.rightNode:
            self.rightNode.printTree(level + 1)

    def getDepth(self):
        right = 0
        left = 0
        if self.rightNode is not None:
            right = self.rightNode.getDepth() + 1

        if self.leftNode is not None:
            left = self.leftNode.getDepth() + 1

        if right > left:
            return right
        else:
            return left

    def getNodes(self):
        right = 0
        left = 0
        if self.rightNode is not None:
            right = self.rightNode.getNodes()

        if self.leftNode is not None:
            left = self.leftNode.getNodes()

        return left + right + 1


if __name__ == '__main__':
    rands = [120, 9, 8, 10]
    root = Node(rands[0])
    for i in range(1, len(rands)):
        root.addVal(rands[i])

    print("Diepte is: ", root.getDepth())
    print("Aantal nodes is: ", root.getNodes())
