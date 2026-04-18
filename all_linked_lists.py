# SINGLE LINKED LIST:
class linked_list:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_list(head):
    current_node = head           
    while current_node:         
        print(current_node.data, end="->")
        current_node = current_node.next
    print("null")


data1=linked_list(2)
data2=linked_list(6)
data3=linked_list(9)
data4=linked_list(22)
data5=linked_list(8)
data6=linked_list(10)

data1.next=data2
data2.next=data3
data3.next=data4
data4.next=data5
data5.next=data6

print_list(data1)




# INSERT NEW NODE:

class add_node:
    def __init__(self,data):
        self.data=data
        self.next=None
def transverseNode(head):
            current_node=head
            while current_node:
                print(current_node.data ,end="->")
                current_node=current_node.next
            print("null")  
def insert_node(head,node,position):
            if position==1:
                node.next=head
                return node
            
            current_node=head
            for _ in range(position-2):
                  if current_node == None:
                        break
                  current_node=current_node.next
            node.next=current_node.next
            current_node.next=node
            return head

data1=add_node(2)
data2=add_node(6)
data3=add_node(9)
data4=add_node(22)
data5=add_node(8)
data6=add_node(10)

data1.next=data2
data2.next=data3
data3.next=data4
data4.next=data5
data5.next=data6


print("Original list")
transverseNode(data1)
data7=add_node(100)
new_node=insert_node(data1,data7,4)
print("inserted list")
transverseNode(new_node)



# DOUBLY LINKED LIST:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def for_next(head):
    current_node=head
    while current_node:
        print(current_node.data ,end="<-->")
        current_node=current_node.next
    print("Null")
def for_prev(head,data):
    new_node=Node(data)
    new_node.next=head
    if head:
        head.prev=new_node
    return new_node
head=None
head=for_prev(head,5)
head=for_prev(head,4)
head=for_prev(head,3)
head=for_prev(head,2)
head=for_prev(head,1)
head=for_prev(head,0)
for_next(head)


#CIRCULAR DOUBLY LINKED LIST

class playlist:
    def __init__(self, songs):
        self.songs = songs
        self.next = None
        self.prev = None

def for_prev(head, songs):
    new_songs = playlist(songs)
    if head is None:
        new_songs.next = new_songs
        new_songs.prev = new_songs
        return new_songs
    else:
                                # Insert at beginning
        tail = head.prev               # Last node
        new_songs.next = head
        new_songs.prev = tail
        head.prev = new_songs
        tail.next = new_songs
        return new_songs               # New head

def current(head):
    if not head:
        print("Playlist is empty.")
        return

    print("\nForward:")

    current_song = head
    while current_song:
        print(current_song.songs, end="<--->")
        current_song = current_song.next
        if current_song == head:       #  stop when looped back
            break

    print("\nBackward:")
    current_song = head.prev           # start from tail
    while current_song:
        print(current_song.songs, end="<--->")
        current_song = current_song.prev
        if current_song == head.prev:  #  stop when back to tail
            break
    print()

head = None
head = for_prev(head, "song #5")
head = for_prev(head, "song #4")
head = for_prev(head, "song #3")
head = for_prev(head, "song #2")
head = for_prev(head, "song #1")
head = for_prev(head, "song #0")

current(head)
