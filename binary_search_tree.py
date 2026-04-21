class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def search(Node,Target):
    if Node is None:
        return None
    elif Node.data == Target:
        return Node
    elif Target < Node.data:
        return search(Node.left,Target)
    else:
        return search(Node.right,Target)
    
root=Tree(100)
Node1=Tree(80)
Node2=Tree(90)
Node3=Tree(60)
Node4=Tree(70)
Node5=Tree(40)
Node6=Tree(50)
Node7=Tree(20)
Node8=Tree(30)
Node9=Tree(10)

root.left=Node1
root.right=Node2

Node1.left=Node3
Node1.right=Node4

Node2.left=Node5
Node2.right=Node6

Node3.left=Node7
Node3.right=Node8

Node4.left=Node9

result=search(root,80)
if result:
    print("Found")
else:
    print("Not found")



