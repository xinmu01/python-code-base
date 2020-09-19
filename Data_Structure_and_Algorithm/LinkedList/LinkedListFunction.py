class SingleListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class DoubleListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.prev = None


def reverseLinkedList(head):
    if not head:
        return head 
    prev = None
    cur = head
    while cur.next:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp 
    cur.next = prev
    return cur 

def listLength(head):
    cnt = 0
    if not head:
        return cnt
    cur = head
    while cur:
        cnt += 1
        cur = cur.next
    return cnt

def checkExist(head, value):
    if not head:
        return False
    cur = head
    while cur:
        if cur.val == value:
            return True
        cur = cur.next
    return False    

def insertNodeLinkedList(head,value,pos):
    temp = SingleListNode(value)
    if not head:
        return temp    
    if pos == 0:
        temp.next = head
        return temp
    listLen = listLength(head)
    if pos >= listLen:
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = temp
        return head
    cnt = 1
    cur = head
    while cnt < pos:
        cur = cur.next
        cnt += 1
    nxt = cur.next
    cur.next = temp
    temp.next = nxt
    return head

def deleteNodeLinkedList(head,pos):
    if not head:
        return head
    listLeng = listLength(head)
    if pos >= listLeng:
        return head
    if pos == 0:
        return head.next
    prev = head
    cnt = 1
    while cnt != pos:
        prev = prev.next 
        cnt += 1
    prev.next = prev.next.next
    return head

if __name__ == "__main__":   

    node1 = SingleListNode(1)
    node2 = SingleListNode(2)
    node3 = SingleListNode(3)
    node4 = SingleListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    #1.Reverse Link List
    rev=reverseLinkedList(node1)
    cur = rev
    while (cur.next):
        print (cur.val, '->', end = ' ')
        cur = cur.next
    print (cur.val)

    #2.Insert Node
    cur = insertNodeLinkedList(node1,5,3)
    while (cur.next):
        print (cur.val, '->', end = ' ')
        cur = cur.next
    print (cur.val)

    #3 Check existence
    checker = checkExist(node1, 10)
    print(checker)

    #4. Delete Node
    cur = deleteNodeLinkedList(node1, 3)
    while (cur.next):
        print (cur.val, '->', end = ' ')
        cur = cur.next
    print(cur.val)