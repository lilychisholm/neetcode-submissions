class Twitter:
    def __init__(self):
        #initialize dict of userIds and set of followers
        #also initialize dict of tweets by userId, tweets indicated by tweetId
        #tweetId and userId can be kept up with by a simple count
        self.count = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = list(self.tweets[userId])
        for followee in self.followers[userId]:
            heap += self.tweets[followee]
        
        heapq.heapify_max(heap)

        final = []

        while len(final) < 10 and len(heap) > 0:
            tweet = heapq.heappop_max(heap)
            final.append(tweet)

        for i in range(len(final)):
            final[i] = final[i][1]
        
        return final


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
