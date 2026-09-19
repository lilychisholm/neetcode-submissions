class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start, stop, target, nums):
            if start >= stop:
                if nums[start] == target:
                    return start
                return -1
            if nums[((stop - start)//2) + start] == target:
                return (stop - start)//2 + start
            elif nums[((stop - start)//2) + start] > target:
                return binarySearch(start, (((stop - start)//2) + start)-1, target, nums)
            elif nums[((stop - start)//2) + start] < target:
                return binarySearch((((stop - start)//2) + start) + 1, stop, target, nums)

        return binarySearch(0, len(nums)-1, target, nums)


        