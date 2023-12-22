class Solution:
    def selection_sort_method_1(self,lst):
        print((lst))
        for i in range(len(lst)):
            midIndex = i
            for j in range(i+1,len(lst)):
                if lst[j] < lst[midIndex]:
                    midIndex = j
            lst[midIndex],lst[i] = lst[i],lst[midIndex]
            print(f"List {lst}")

    def selection_sort_method_2(self,lst):
        print(lst)
        low = mid = 0
        high = len(lst) -1
        print(f"low={low}, mid={mid}, high={high}")
        while mid <= high:
            if lst[mid] == 0:
                lst[low],lst[mid] = lst[mid],lst[low]
                mid+=1
                low+=1
                print(f"when mid is 0, {lst}")
            elif lst[mid] == 1:
                mid+=1
                print(f"when mid is 1, {lst}")
            else:
                lst[mid],lst[high] =lst[high],lst[mid]
                print(f"when mid is 2, {lst}")
                high-=1

l1 = Solution()

list1 = [2,0,2,1,1,0]
l1.selection_sort_method_1(list1)

list1 = [2,0,2,1,1,0]
l1.selection_sort_method_2(list1)

list1 = [8,4,10,7,2,5,9,1,3,6,2]
l1.selection_sort_method_2(list1)
