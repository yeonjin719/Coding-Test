class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if (nums[i] >= target):
                pass
            for j in range(i+1, len(nums)):
                if (nums[j] >= target):
                    pass
                if (nums[i]+nums[j] == target):
                    return [i, j]
                else: 
                    pass
        