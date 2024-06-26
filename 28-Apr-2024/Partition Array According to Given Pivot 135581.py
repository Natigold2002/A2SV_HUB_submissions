# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        least=[]
        more=[]
        equal=[]
        for num in nums:
            if num>pivot:
                more.append(num)
            elif num<pivot:
                least.append(num)
            else:
                equal.append(num)
        least.extend(equal)
        least.extend(more)
        return least
                

        