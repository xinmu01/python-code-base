class SingleListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class DoubleListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.prev = None

class SingleLinkedList: 
    def __init__(self,headVal):
        self.head = SingleListNode(headVal)
        self.length = 1
        self.isEmpty = False
    def connect(self,nextVal):
        if not self.head:
            self.head =  SingleListNode(nextVal)
            self.length += 1
            self.isEmpty = False
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = SingleListNode(nextVal)
        self.length += 1
    def printList(self):
        if not self.head:
            print("This linked lis is empty")
            return
        cur = self.head
        while cur.next:
            print(cur.val, '->', end=" ")
            cur = cur.next
        print (cur.val)
    def reverseLinkedList(self):
        if not self.head:
            print("This linked list is empty")
            return
        prev = None
        cur = self.head
        while cur.next:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp 
        cur.next = prev
        self.head = cur
    def checkExist(self, value):
        cur = self.head
        while cur:
            if cur.val == value:
                return True
            cur = cur.next
        return False
    def insertNodeLinkedList(self,value,pos):
        temp = SingleListNode(value)  
        if not self.head:
            self.head = temp
            self.length += 1
            self.isEmpty = False
            print("This linked list is empty. Put this node as the head.")
        elif pos == 0:
            temp.next = self.head
            self.head = temp
            self.length += 1
        elif pos >= self.length:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = temp
            self.length += 1
        else:
            cnt = 1
            cur = self.head
            while cnt < pos:
                cur = cur.next
                cnt += 1
            nxt = cur.next
            cur.next = temp
            temp.next = nxt
            self.length += 1
    def deleteNodeLinkedListPosition(self,pos):
        if not self.head:
            print("This linked list is empty")
            return
        elif pos >= self.length:
            print ("There is no this position in LinkedList")
            return
        elif pos == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            prev = self.head
            cnt = 1
            while cnt != pos:
                prev = prev.next 
                cnt += 1
            prev.next = prev.next.next
            self.length -= 1
        if not self.head:
            self.isEmpty = True
    def deleteNodeLinkedListValue(self,val):
        if not self.checkExist(val):
            print ("There is no this node in LinkedList")
            return
        while self.head and self.head.val == val:
            self.head = self.head.next
            self.length -= 1
        if self.head:
            prev = self.head
            cur = self.head.next    
            while cur:
                if cur.val == val:
                    prev.next = cur.next
                    cur = cur.next
                    self.length -= 1
                else:
                    prev = cur
                    cur = cur.next
        else:
            print("The linkedlist is empty now")
            self.isEmpty = True

    

         






     







