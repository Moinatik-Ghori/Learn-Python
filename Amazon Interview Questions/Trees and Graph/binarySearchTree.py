class Treenode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def buildTree(lst):

    # Create the Root Node from the first element of the list
    root = Treenode(lst[0])

    # Initialize the stack with Root node
    stack = [root]

    # Index to maintain the list
    i = 1
    while i < len(lst):
        current = stack.pop(0)
        #print(current)
        i+=1


lst = [2,1,3]
root = buildTree(lst)
