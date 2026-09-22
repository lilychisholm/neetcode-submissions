class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = 0
        if nums[0] >= nums[-1]:
            l, r = 0, len(nums) - 1
            while l <= r:
                if l == r:
                    offset = l
                    break
                middle = l + (r-l) // 2
                if nums[middle+1] < nums[middle]:
                    offset = middle+1
                    break
                elif nums[middle - 1] > nums[middle]:
                    offset = middle
                    break
                if nums[middle] == target:
                    return middle
                elif nums[middle] < nums[l]:
                    r = middle - 1
                else:
                    l = middle + 1

        newArr = nums[offset:] + nums[0:offset]
        l, r = 0, len(newArr) - 1
        while l <= r:
            if l == r and newArr[l] == target:
                index = l + offset
                if index >= len(newArr):
                    index = index - len(newArr)
                return index

            else:
                middle = l + (r-l) // 2
                if newArr[middle] == target:
                    middle = middle + offset
                    if middle >= len(newArr):
                        middle = middle - len(newArr) 
                    return middle
                elif newArr[middle] > target:
                    r = middle - 1
                else:
                    l = middle + 1                 

        return -1

        