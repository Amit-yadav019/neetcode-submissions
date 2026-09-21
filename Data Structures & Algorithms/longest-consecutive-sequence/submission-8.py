class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        if len(nums) == 0 :
            return 0
        longest = 1 
        count = 1 

        for i in range(1,n):
            if nums[i] == nums[i-1]:
                continue 
            elif nums[i] == nums[i-1]+1 :
                count = count + 1
            else:
                count = 1 
            longest = max(longest,count)
        return longest 

