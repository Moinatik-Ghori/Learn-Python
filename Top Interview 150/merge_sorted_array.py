class Solution:
    def merged_sorted_array(self,nums1,m,nums2,n):
        print(f"Given first array is : {nums1} and Second array is {nums2}")
        merged_array = []
        i,j=0,0
        filtered_arr_01 = nums1[:m]
        filtered_arr_02 = nums2[:n]
        print(f"As per the input ,we have to take first {m} numbers from Array-1 and first {n} numbers from Array-2"
              f"\n Array1 : {filtered_arr_01}"
              f"\n Array2 : {filtered_arr_02}")

        while i < m and j < n:
            if filtered_arr_01[i] < filtered_arr_02[j]:
                merged_array.append(filtered_arr_01[i])
                i += 1
            else:
                merged_array.append(filtered_arr_02[j])
                j += 1
        print(f"Comaparing both the arrays one by one element and added in Result array. Array will look like this"
              f"\nIntermidiate Result array : {merged_array}")
        if i < m:
            merged_array.extend(filtered_arr_01[i:])
        if j < n:
            merged_array.extend((filtered_arr_02[j:]))
        print(f" Due to different length of both the array, still we need to copy the remainign elements from the array"
              f"\nFinal Array will be as below:")
        return merged_array



nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2  = [1,2,2]
n=3

solObject = Solution()
print(f"Final Array: {solObject.merged_sorted_array(nums1,m,nums2,n)}")