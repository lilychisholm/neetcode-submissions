import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #ideas: put into tuples sorted by start time. use DFS to find all possible paths,
        #and path with highest profit. DFS can use index to go through list of tuples.
        #have a cache dict to keep up with visited tuples to avoid redundant pathfinding
        #base case: i  == len(tuples): return 0 here since this will not have an associated profit
        #if the next value in dfs(i) has a starttime before the endtime of the current tuple, make new path with res = dfs(i + 1)
        #next need to see which tuple is next consecutively, do j = bisect.bisect(intervals, 
        #(intervals[i][1], -1, -1)). last, add this j profit to path of current tuple, since its the next 
        # thing in the path. cache[i] = res = max(res, tuples[i][2] + dfs(j))
        #return res

        #return dfs(0) is function call to start looking through tuples list

        tuples = sorted(zip(startTime, endTime, profit));
        cache = dict()

        def dfs(i):
            if i == len(tuples):
                return 0
            if i in cache:
                return cache[i]
            res = dfs(i + 1) #get everything not yet in cache

            j = bisect.bisect(tuples, (tuples[i][1], -1, -1))
            cache[i] = res = max(res,tuples[i][2]+dfs(j))
            return res
        return dfs(0)

