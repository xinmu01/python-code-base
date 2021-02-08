class Heap:
    def __init__(self):
        self.heap = [0]

    def insert(self,val):
        self.heap.append(val)
        index = len(self.heap) - 1
        self.shiftUp(index)
    
    def deleteMin(self):
        if len(self.heap) == 1:
            print('Error! The heap is empety.')
            return
        
        if len(self.heap) == 2:
            self.heap.pop()
            return 

        self.heap[1],self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[1]
        self.heap.pop()

        self.shiftDown(1)

    def delete(self,val):
        for i in range(1,len(self.heap)):
            if self.heap[i] == val:
                break
        
        if i == len(self.heap)-1 and self.heap[i] != val:
            print("{} is not in heap!".format(val))
            return

        if i == len(self.heap) - 1:
            self.heap.pop()
            return 

        self.heap[i], self.heap[len(self.heap)-1] =  self.heap[len(self.heap)-1],self.heap[i]
        self.heap.pop()
        
        self.shiftUp(i)
        self.shiftDown(i)

    def shiftUp(self,index):
        while index // 2 > 0:
            if self.heap[index] >= self.heap[index // 2]:
                break
            else:
                self.heap[index],self.heap[index//2] =  self.heap[index//2],self.heap[index]
                index = index//2

    def shiftDown(self,index):        
        while index*2 <= len(self.heap) - 1:
            if index*2 + 1 <= len(self.heap) - 1:
                if self.heap[index*2] < self.heap[index*2+1]:
                    temp = index*2
                else:
                    temp = index*2+1
            else:
                temp = index*2
            
            if self.heap[index] <= self.heap[temp]:
                return 
            else:
                self.heap[index], self.heap[temp] = self.heap[temp],self.heap[index]
                index = temp


        

