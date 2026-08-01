class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        group={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in group:
                return [group[diff],i]
            group[n]=i
         