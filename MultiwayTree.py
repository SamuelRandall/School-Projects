#  File: MultiwayTree.py
#  Description: Read in data from two multiway trees then print each tree in preorder and determine if they have the same shape.
#  Student's Name: Samuel Randall
#  Student's UT EID: spr699
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 12/08/17
#  Date Last Modified:12/08/17

class Node (object):
    def __init__(self,initdata):
        self.data = initdata
        self.children = []
      
    def getData (self):
        return self.data            # returns a POINTER

    def getNext (self):
        return self.next            # returns a POINTER

    def setData (self, newData):
        self.data = newData         # changes a POINTER

    def setNextChild (self,newNext):
        self.children.append(newNext)

    def __str__(self):
        return str(self.data)

class MultiwayTree:
    
    # given "pyTree", a Python representation of a tree, create a
    # node-and-pointer representation of that tree.
    def __init__(self,pyTree):
        if pyTree != []:
            self.root = Node(pyTree.pop(0))
            for i in pyTree[0]:
                self.root.setNextChild(MultiwayTree(i))

    # print out the node-and-pointer representation of a tree using preorder.
    def preOrder(self):
        print(self.root, end=' ')
        for child in self.root.children:
            child.preOrder()
            
    # return True if the tree "self" has the same structure as the tree "other", "False" otherwise.
    def isIsomorphicTo(self,other):

        value = True
        
        # check length first
        if len(self.root.children) != len(other.root.children):
            return False

        else:
            # check for isomorphism 
            for i in range(len(self.root.children)):
                value = self.root.children[i].isIsomorphicTo(other.root.children[i])
                
        return value
            
def main():
    
    file = open("MultiwayTreeInput.txt", "r")

    trees = []
    
    for line in file:
        trees.append(eval(line))
        
    file.close()

    # start from 0 end at the len of trees list and interate by 2
    for i in range(0, len(trees), 2):
        treeOne = trees[i]
        treeTwo = trees[i+1]

        print()

        # print the two versions of tree one
        print("Tree %d:" % (i+1), treeOne)
        treeOne = MultiwayTree(treeOne)
        
        print("Tree %d preorder:"  % (i+1), end='')
        treeOne.preOrder()

        print("\n")

        # same for tree two
        print("Tree %d:" % (i+2), treeTwo)
        treeTwo = MultiwayTree(treeTwo)
        print("Tree %d preorder: " % (i+2), end='')
        treeTwo.preOrder()

        print()

        # run isomorphism test
        if treeOne.isIsomorphicTo(treeTwo):
            print("Tree %d is isomorphic to Tree %d" % (i+1, i+2))
        else:
            print("Tree %d is not isomorphic to Tree %d" % (i+1, i+2))

        print()

main()
