class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1 = 0
        ptr2 = 0
        sortedArray = []

        total = len(nums1) + len(nums2)
        mid = total // 2
        isOdd = total % 2 == 1

        while len(sortedArray) <= mid:
            if ptr1 >= len(nums1):
                sortedArray.append(nums2[ptr2])
                ptr2 += 1
            elif ptr2 >= len(nums2):
                sortedArray.append(nums1[ptr1])
                ptr1 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                sortedArray.append(nums1[ptr1])
                ptr1 += 1
            else:
                sortedArray.append(nums2[ptr2])
                ptr2 += 1

        if isOdd:
            return sortedArray[mid]
        else:
            return (sortedArray[mid] + sortedArray[mid - 1]) / 2