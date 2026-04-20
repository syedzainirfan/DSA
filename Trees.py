class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = [] 

root = TreeNode("CEO")
manager1 = TreeNode("Manager 1")
manager2 = TreeNode("Manager 2")
root.children.extend([manager1, manager2])

print(root.value)
print([child.value for child in root.children])

