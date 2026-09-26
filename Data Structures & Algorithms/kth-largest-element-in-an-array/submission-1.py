class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #two methods in mind: max heap, min heap
        #max heap: heapify, then pop until we've popped k elements
        #min heap: keep a min heap of length k
        #loop through the nums list, adding them to a final heap
        #once the list has reached a length of k, start popping the minimum element each time a new one is added
        #we will be left with a heap of the k largest elements, where the minimum of the k largest is at the top, aka our kth largest element
        
        #min heap approach:
        # heapq.heapify(nums)
        # while len(nums) > k:
        #     heapq.heappop(nums)

        # return nums[0]
        
        #max heap approach:
        final = []
        for i in range(len(nums)):
            heapq.heappush(final, nums[i])
            if len(final) > k:
                heapq.heappop(final)

        return final[0]

