class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #need to use a min heap to track k minimum distances to origin
        #can we do heapify based on an item in an array? that way we could have each point with its distance to the origin, and use the distance to heapify off of
        #take entire list of [point, distance to origin], heapify by distance, then pop until length of heap is k
        #ok looked it up, python automatically compares tuples y their first element! put everything in a tuple with the distance to origin as the first element, then the point as the second element
        #the minimum will be at the top, so we can keep popping and adding popped elements to the final array until the array is of length k. this will give us the k points of minimum distance
        # for i in range(len(points)):
        #     points[i] = ((points[i][0]**2 + points[i][1]**2), points[i])
        # heapq.heapify(points)

        # final = []
        # while len(final) < k:
        #     final.append(heapq.heappop(points)[1])

        # return final



#max heap approach:
#have a final heap list to store the answer
#loop through the initial array. each loop, add the new (distance to origin, point) combination to the final heap. then, pop the biggest item from the heap
        final = []
        for i in range(k):
            heapq.heappush_max(final, ((points[i][0]**2 + points[i][1]**2), points[i]))
        for i in range(k, len(points)):
            heapq.heappush_max(final, ((points[i][0]**2 + points[i][1]**2), points[i]))
            heapq.heappop_max(final)
        
        for i in range(len(final)):
            final[i] = final[i][1]

        return final



        