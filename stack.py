# class stack:
#     def __init__(self):
#         self.Stack=[]
#     def push(self,name):
#         self.Stack.append(name)
#         return self.Stack
#     def isEmpty(self):
#         return len(self.Stack)==0
#     def pop(self):
#         if self.isEmpty():
#             return "stack is empty"
#         return self.Stack.pop()
#     def peek(self):
#         if self.isEmpty():
#             return "stack is empty"
#         return self.Stack[-1]
#     def size(self):
#         return len(self.Stack)
    
# my_object= stack()
# my_object.push("rafay")
# my_object.push("zain")
# print(my_object.push("hassan"))
# print(my_object.pop())
# print(my_object.peek())
# print(my_object.isEmpty())
# print(my_object.size())

#_______________________________________________________________________

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if not self.head:
            return None
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.data   

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")  
            currentNode = currentNode.next
        print("None")  


data1 = stack()
data1.push("a")
data1.push("b")
data1.push("c")

print("LinkedList: ", end="")
data1.traverseAndPrint()
print("Pop: ", data1.pop())
print("LinkedList after pop: ", end="")
data1.traverseAndPrint()
    