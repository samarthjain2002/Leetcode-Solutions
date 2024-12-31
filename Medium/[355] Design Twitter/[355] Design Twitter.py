"""
Accepted
355 [Medium]
Runtime: 15 ms, faster than 30.90% of Python3 online submissions for Design Twitter.
Memory Usage:  27.78 MB, less than 8.27% of Python3 online submissions for Design Twitter.
"""
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)

        # Tweets by this user
        if self.tweetMap[userId]:
            us_tweets = self.tweetMap[userId][-1]
            heapq.heappush(minHeap, (us_tweets[0], us_tweets[1], userId, len(self.tweetMap[userId]) - 1))
        # Tweets by the followees of this user
        for followee in self.followMap[userId]:
            if self.tweetMap[followee]:
                followee_tweets = self.tweetMap[followee][-1]
                heapq.heappush(minHeap, (followee_tweets[0], followee_tweets[1], followee, len(self.tweetMap[followee]) - 1))

        res = []
        for _ in range(10):
            if minHeap:
                count, tweet, user, i = heapq.heappop(minHeap)
                res.append(tweet)
                i -= 1
                if i >= 0:
                    user_tweet = self.tweetMap[user][i]
                    heapq.heappush(minHeap, (user_tweet[0], user_tweet[1], user, i))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)