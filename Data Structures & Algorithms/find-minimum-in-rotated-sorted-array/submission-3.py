class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]< nums[-1]:
            return nums[0]

        else:
            l, r = 0, len(nums)-1
            minimum = float('inf')
            while l <= r:
                if l == r:
                    minimum = nums[l]
                    break
                else:
                    middle = l + (r-l) // 2
                    if nums[middle - 1] > nums[middle]:
                        minimum = nums[middle]
                        break
                    elif nums[middle + 1] < nums[middle]:
                        minimum = nums[middle+1]
                        break
                    if nums[middle] > nums[r]:
                        l = middle + 1
                    elif nums[middle] < nums[l]:
                        r = middle - 1

            return minimum

                        


        