# This is a module contains all the Xin's data structure and algorithm 

class sorting():
    def merge_sort (self,input_list):
        #print ("The input list is {}".format(input_list))
        if input_list == None or len(input_list) <= 1:
            return input_list

        left = self.merge_sort(input_list[ : len(input_list)//2])
        right = self.merge_sort(input_list[len(input_list)//2 : ])
        
        #print(left)
        #print(right)

        temp = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                temp.append(left[i])
                i+=1
            else:
                temp.append(right[j])
                j+=1
        
        if i < len(left):
            temp.extend(left[i:])
        if j < len(right):
            temp.extend(right[j:])

        return temp

    def quick_sort(self, input_list, sta, end):
        
        if input_list == None or sta >= end:
            return

        pi = self.partition(input_list,sta,end)

        self.quick_sort(input_list, sta, pi-1)
        self.quick_sort(input_list, pi + 1, end)

    
    def partition(self,input_list,sta,end):
        '''
        Using the last element as the pivot point
        '''
        pi = input_list[end]
        i = sta -1
        for j in range (sta, end):
            if input_list[j] < pi:
                i+=1
                input_list[i], input_list[j] = input_list[j], input_list[i]

        input_list[i+1], input_list[end] = input_list[end], input_list[i+1]

        return i+1

class link_list_node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class link_list:
    def __init__(self,head):
        self.head = head

    def traverse_linked_list(self):
        temp = []
        cur = self.head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        return temp
    
    def reverse_linked_list(self):
        
        if self.head == None:
            return self.head
        
        prev = None
        cur = self.head

        while cur.next:
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp 
        
        cur.next = prev
        return cur



class tree_node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class binary_search_tree:
    def __init__ (self,node):
        self.root = node
    
    def insert(self, num):
        self.root = self.insert_helper(self.root, num)  
    
    def insert_helper(self,root,num):
        if root is None:
            return tree_node(num)
        
        if num >= root.val:
            root.right = self.insert_helper(root.right,num)
        else:
            root.left = self.insert_helper(root.left, num)
        
        return root 

        
if __name__ == "__main__":
    sorting_xin = sorting()
    #list_sorted = sorting_xin.merge_sort([1,4,3,2,5])
    list_sorted = [10,1,4,3,2,5,3.3,100,6,4,4,4,4,10,1.3,4.6,0.8]
    sorting_xin.quick_sort(list_sorted,0,len(list_sorted)-1)
    print (list_sorted)

    # Construct Linked list
    node1 = link_list_node(1)
    node2 = link_list_node(1.5)
    node3 = link_list_node(4)
    node4 = link_list_node(0.5)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    linked_list = link_list(node1)
    linked_list_tranverse =  linked_list.traverse_linked_list() 
    print (linked_list_tranverse)  

    linked_list_tranverse =  link_list(linked_list.reverse_linked_list()).traverse_linked_list()
    print (linked_list_tranverse) 