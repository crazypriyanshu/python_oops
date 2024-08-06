class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def print_tree(self):

        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data



root = Node(10)
# root.left = Node(20)
# root.right = Node(30)
# root.left.left = Node(40)
root.insert(5)
root.insert(7)
root.insert(9)
root.insert(15)
root.insert(20)
root.insert(400)

root.print_tree()



