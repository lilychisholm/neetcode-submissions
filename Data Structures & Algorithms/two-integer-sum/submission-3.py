class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = dict()
        for index, num in enumerate(nums):
            numdict[num] = index
        for index, num in enumerate(nums):
            diff = target - num
            if diff in numdict and numdict[diff] != index:
                return [index, numdict[diff]]
        
