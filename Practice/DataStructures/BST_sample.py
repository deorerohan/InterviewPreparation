import random

class Node:
    K = 2
    def __init__(self, value) -> None:
        self.value = value # tuple of values
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self)->None:
        self.root = None


    def insert_node(self, value):
        """ insert node """

        if self.root == None:
            self.root = Node(value)
            return self.root

        currentNode = self.root
        while currentNode != None:
            if currentNode.value <= value:
                if currentNode.right != None:
                    currentNode = currentNode.right
                    continue
                currentNode.right = Node(value)
                break

            elif currentNode.value > value:
                if currentNode.left != None:
                    currentNode = currentNode.left
                    continue
                currentNode.left = Node(value)
                break
            else:
                print('Invalid scenario')

    def print_BST(self):
        currentNode = self.root
        stack = list()
        stack.append(currentNode)
        while currentNode != None or len(stack) > 0:
            if currentNode != None:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()
                print(currentNode.value)
                currentNode = currentNode.right

    def inOrder (self):
        print ("InOrder:    ", end="")
        def recurse(node):
            if node != None:
                recurse(node.left)
                print(node.value,end = " | ")
                recurse(node.right)
        recurse(self.root)
        print( )

if __name__ == "__main__":
    bst =  BinarySearchTree()

    bst.insert_node(4)
    bst.insert_node(3)
    bst.insert_node(6)
    bst.insert_node(5)
    bst.insert_node(10)
    bst.insert_node(2)
    for _ in range(9999):
        bst.insert_node(random.randint(0, 100))

    bst.inOrder()
    #bst.print_BST()
