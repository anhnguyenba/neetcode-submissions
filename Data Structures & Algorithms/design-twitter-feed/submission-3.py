class Twitter:
    # tweet: tweetId, userId, timestamp
    # connection: (userId) followerId -> (userId) followeeId
    # 10 most recent tweedIds, timestamp
    # 1, 10, 0
    # 2, 20, 1
    # 1: [(0, 10), ...]
    # 2: [(1, 20), ...]
    # 1: [2]
    # 2: []


    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                timestamp, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [timestamp, tweetId, followeeId, index - 1])
        
        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                timestamp, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, [timestamp, tweetId, followeeId, index - 1])
        return res          


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
