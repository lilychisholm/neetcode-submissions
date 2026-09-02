class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = []
        longestlen = 0

        for i in range(len(nums)):
            if len(longest) == 0:
                longest.append(nums[i])
            else:
                if nums[i] == longest[-1]:
                    continue
                elif nums[i] == longest[-1] + 1:
                    longest.append(nums[i])
                else:
                    if len(longest) > longestlen:
                        longestlen = len(longest)
                    longest = [nums[i]]
            print(longest)
        if len(longest) > longestlen:
            longestlen = len(longest)
        return longestlen