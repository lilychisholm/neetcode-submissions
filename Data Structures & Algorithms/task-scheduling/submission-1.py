from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #heap aaaaaaaa
        #keep a max heap - it's always better to use the largest values first to fill up spots faster
        #also keep a timer to track how many time units are being taken up
        #we can also also keep track of when we can use a letter again by using a queue to track the letters left of that letter, and the time at which it can be added in again
        #using a queue works becuase it stores things in the order they are added, which in our case works as it stores the time order of things added
        #each loop, we check the queue. if the current time is equal to the time of the first object in the queue, we can push that number back onto the maxheap, since it's now free to be used again
        #once we hit 0 for everything in the maxheap, if the queue is not empty, we increment the timer and loop again
        #if we hit 0 for everything in the maxheap and the queue is empty, our operation is finished
        if n == 0:
            return len(tasks)

        task_nums = defaultdict(int)
        for i in range(len(tasks)):
            task_nums[tasks[i]] += 1
        
        task_nums = list(task_nums.values())
        heapq.heapify_max(task_nums)

        timer = 0
        queue = deque()
        while True:
            timer += 1
            if queue and queue[0][1] == timer:
                heapq.heappush_max(task_nums, queue.popleft()[0])
            if task_nums:
                num = heapq.heappop_max(task_nums)
                if num - 1 > 0:
                    queue.append([num-1, timer + 1 + n])
            if not queue and not task_nums:
                break
        return timer
            



