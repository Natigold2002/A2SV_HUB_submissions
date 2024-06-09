# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        
        for i in range(len(nums)-3,-1,-1):
            if nums[i]+nums[i+1]>nums[i+2]:
                ans=nums[i]+nums[i+1]+nums[i+2]
                break
            
        return ans

        

     