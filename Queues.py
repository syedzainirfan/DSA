class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queues:

    def __init__(self):
        self.front=None
        self.last=None
        self.length=0

    def Equeue(self,head):
        currentNode=node(head)
        if self.last is None:
            self.front=self.last=currentNode
            self.length+=1
            return
        self.last.next=currentNode
        self.last=currentNode
        self.length+=1

    def Dequeue(self):
        data1=self.front
        self.front=data1.next
        self.length-=1
        if self.front is None:
            self.last= None
        return data1.data

    def printQueue(self):
        data1 = self.front
        while data1:
            print(data1.data, end=" -> ")
            data1 = data1.next
        print()

Queue = queues()
Queue.Equeue(7)
Queue.Equeue(8)
Queue.Equeue(2)
Queue.Equeue(11)
Queue.Equeue(88)

# print("Queue: ", end="")
# Queue.printQueue()
# print("Dequeue: ", Queue.Dequeue())
# print("Queue after Dequeue: ", end="")
# Queue.printQueue()
#________________________________________________________________________________________________________________

