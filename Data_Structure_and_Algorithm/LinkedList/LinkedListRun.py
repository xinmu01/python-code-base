import LinkedListClass as LL 

if __name__ == "__main__":   

    #1-Generate Linked List
    linkList = LL.SingleLinkedList(1)
    linkList.connect(2)
    linkList.connect(3)
    linkList.connect(4)
    linkList.connect(1)
    linkList.connect(2)

    #2-Check Linked List
    print (linkList.length)
    print (linkList.checkExist(3))
    print (linkList.checkExist(6))   
    linkList.printList()

    #3-Reverse Linked List
    linkList.reverseLinkedList()    
    linkList.printList()

    #4-Reverse it back
    linkList.reverseLinkedList()
    linkList.printList()

    #5-Insert one noed
    linkList.insertNodeLinkedList(5,5)
    linkList.printList()
    print(linkList.length)
    print(linkList.isEmpty)

    #6-Delete one node by index
    linkList.deleteNodeLinkedListPosition(100)
    linkList.printList()
    linkList.deleteNodeLinkedListPosition(3)
    linkList.printList()
    print(linkList.length)
    print(linkList.isEmpty)

    #7-Delete one node by value
    linkList.deleteNodeLinkedListValue(100)
    linkList.printList()
    linkList.deleteNodeLinkedListValue(2)
    linkList.printList()
    linkList.deleteNodeLinkedListValue(4)
    linkList.printList()
    print (linkList.checkExist(3))
    print (linkList.length)
    linkList.deleteNodeLinkedListValue(1)
    linkList.printList()
    linkList.deleteNodeLinkedListValue(3)
    linkList.printList()
    linkList.deleteNodeLinkedListValue(5)
    linkList.printList()
    print (linkList.length)
    print (linkList.isEmpty)

    #8-Insert one node again
    linkList.insertNodeLinkedList(1,1000)
    linkList.printList()
    print(linkList.length)
    print(linkList.isEmpty)

