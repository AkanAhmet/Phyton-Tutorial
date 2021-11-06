#---------------------- LINKED LIST -----------------------------

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
       
        self.head = None

    def get(self, index):
       
        cur = self.head

        while index:
            if index == 0 and cur:
                return cur.val
            index = index - 1
 
            if cur:  # if cur then go cur.next
                cur = cur.next
            else:  # cur is None then the index is invalid
                return -1

    def addAtHead(self, val):
       
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head

    def addAtTail(self, val):
      
        cur = self.head
        if cur:  # non-empty linked list
            while cur.next:
                cur = cur.next
            cur.next = Node(val)
        else:  # empty linked list
            self.head = Node(val)

    def addAtIndex(self, index, val):
     
        if index == 0:
            self.addAtHead(val)
            return

        cur = self.head
        prev = None
        while index and cur:
            prev = cur
            cur = cur.next
            index -= 1
        if prev:
            if cur:
                new = Node(val)
                new.next = cur
                prev.next = new
            else:
                prev.next = Node(val)

    def deleteAtIndex(self, index):
        
        cur = self.head
        prev = None
        while index and cur:
            prev = cur
            cur = cur.next
            index -= 1
        if prev and cur:
            prev.next = cur.next

    def __repr__(self):
        s = ''
        cur = self.head
        while cur:
            s += str(cur.val) + ' -> '
            cur = cur.next
        return 'linked_list:' + str(s if self.head else 'None')


import time

# funcs = ["addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtIndex","addAtHead","addAtHead","deleteAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtHead","get","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtTail","get","addAtHead","deleteAtIndex","get","get","addAtIndex","addAtTail","get","get","addAtTail","addAtHead","addAtTail","addAtTail","addAtHead","get","addAtIndex","get","addAtHead","addAtHead","addAtTail","addAtHead","get","addAtTail","addAtHead","addAtHead","get","addAtHead","addAtHead","addAtHead","addAtIndex","get","addAtTail","addAtHead","addAtHead","addAtTail","get","addAtIndex","deleteAtIndex","get","addAtTail","addAtTail","get","addAtIndex","addAtIndex","addAtTail","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtHead","addAtIndex","addAtTail","addAtHead","addAtTail","addAtTail","addAtTail","deleteAtIndex","deleteAtIndex","addAtTail","addAtHead","addAtTail","addAtTail","get","addAtIndex","addAtTail","addAtHead","addAtTail","addAtIndex","addAtHead","addAtTail","addAtIndex","addAtIndex","addAtIndex","addAtTail","addAtTail","addAtHead","deleteAtIndex","addAtIndex"]
# params = [[24],[1],[79],[10],[51],[3,37],[92],[53],[6],[5],[6],[33],[47],[7,42],[6,40],[82],[9],[37],[6,84],[2,50],[21],[22],[6],[51],[7],[10],[2],[3,5],[8],[15],[6],[89],[32],[99],[65],[51],[9],[15,62],[20],[83],[10],[3],[10],[3],[21],[22],[22],[7],[87],[73],[85],[19,17],[29],[2],[23],[88],[21],[6],[20,46],[4],[38],[59],[36],[36],[32,99],[23,79],[84],[82],[89],[98],[48],[75],[55],[4,24],[90],[8],[24],[7],[17],[37],[10],[32],[15],[9],[18],[19],[53,96],[31],[11],[96],[4,44],[69],[65],[33,22],[38,55],[31,31],[12],[0],[47],[65],[54,37]]

funcs = ["addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
params = [[1], [3], [1, 2], [1], [1], [1]]

obj = MyLinkedList()
for idx, item in enumerate(funcs):
    command = 'obj.{}(*'.format(item) + str(params[idx]) + ')'
    print(command)
    exec(command)
    print(obj)
    time.sleep(1)

#---------------------- STACK -----------------------------
def printStack():
    print(stack)

stack = []

stack.append(5)
stack.append(10)
stack.append(15)

printStack()

for i in range(0,len(stack)):
    stack.pop()
    
printStack()
#---------------------- QUEQE -----------------------------

queqe = []
queqe.extend(('a','b','c'))

queqe.pop(0)
print(queqe)

queqe.pop(0)
print(queqe)