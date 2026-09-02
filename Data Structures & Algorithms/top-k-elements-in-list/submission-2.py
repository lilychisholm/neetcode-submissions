class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = dict()
        for num in nums:
            if num not in numdict:
                numdict[num] = 1
            else:
                numdict[num] += 1
        
        numdict = sorted(numdict.items(), key=lambda item: item[1])
        numdict.reverse()
        numdict = numdict[:k]
        finalarr = []
        for pair in numdict:
            finalarr.append(pair[0])
        return finalarr

        
        