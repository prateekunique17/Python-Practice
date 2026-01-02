class Solution:
    def twoSum(self, nums, target):
        seen = {}   # value : index
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

nums = [2, 7, 11, 15]
target = 9

sol = Solution()
result = sol.twoSum(nums, target)
print(result) 
