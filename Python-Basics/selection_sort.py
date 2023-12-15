class Solution:
    def selection_sort(self,lst):
        print((lst))

        for i in range(len(lst)):
            midIndex = i
            for j in range(i+1,len(lst)):
                if lst[j] < lst[midIndex]:
                    midIndex = j
            lst[midIndex],lst[i] = lst[i],lst[midIndex]
            print(f"List {lst}")

list1 = [3,6,10,8,5,9,2,4,7,1]
l1 = Solution()
l1.selection_sort(list1)
