class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numlist = dict()
        for item in nums:
            if item not in numlist:
                numlist[item] = 1
            else:
                return True

        return False
        

        