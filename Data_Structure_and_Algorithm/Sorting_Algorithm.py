# This is a module contains all the Xin's sorting algorithm 

class sorting():
    def merge_sort (self,input_list):
        #print ("The input list is {}".format(input_list))
        if input_list == None or len(input_list) <= 1:
            return input_list

        left = self.merge_sort(input_list[ : len(input_list)//2])
        right = self.merge_sort(input_list[len(input_list)//2 : ])
        
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
        self.quick_sort(input_list, pi+1, end)

    
    def partition(self,input_list,sta,end):
        '''
        Using the last element as the pivot point
        '''
        p = input_list[end]
        i = sta -1
        for j in range (sta, end):
            if input_list[j] < p:
                i+=1
                input_list[i], input_list[j] = input_list[j], input_list[i]

        input_list[i+1], input_list[end] = input_list[end], input_list[i+1]

        return i+1
        
if __name__ == "__main__":
    sorting_engine = sorting()
    list_sorted_mergesort = sorting_engine.merge_sort([1,4,3,2,5])
    print ("Merge Sort Results: \n {}".format(list_sorted_mergesort))

    #quick sort is the in_place sorting
    list_quick_sorted = [10,1,4,3,2,5,3.3,100,6,4,4,4,4,10,1.3,4.6,0.8]
    sorting_engine.quick_sort(list_quick_sorted,0,len(list_quick_sorted)-1)
    print ("Quick Sort Results: \n {}".format(list_quick_sorted))
