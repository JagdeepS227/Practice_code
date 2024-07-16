class Node:
    def __init__(self, val=None):
        self.next = None
        self.prev = None
        self.val = val

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        cnt = 0
        head = self.head
        while head:
            if cnt == index:
                return head.val
            cnt += 1
            head = head.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return
        head = self.head
        while head.next:
            head = head.next
        head.next = node
        node.prev = head

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        head = self.head
        cnt = 0
        while head:
            if cnt == index - 1:
                node = Node(val)
                node.next = head.next
                node.prev = head
                if head.next:
                    head.next.prev = node
                head.next = node
                return
            head = head.next
            cnt += 1
        # If index is greater than the length of the list, do nothing

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            return
        head = self.head
        cnt = 0
        while head:
            if cnt == index - 1 and head.next:
                temp = head.next.next
                if temp:
                    temp.prev = head
                del head.next
                head.next = temp
                return
            head = head.next
            cnt += 1

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
param_1 = obj.get(0)
print(param_1)
param_1 = obj.get(1)
print(param_1)
param_1 = obj.get(2)
print(param_1)
obj.deleteAtIndex(1)
param_1 = obj.get(1)
print(param_1)
