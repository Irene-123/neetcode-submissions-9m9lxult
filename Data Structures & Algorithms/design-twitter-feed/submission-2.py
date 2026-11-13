import collections
import heapq as hq

class Twitter:

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.followers = collections.defaultdict(set)
        self.time = 0  

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((-self.time, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followers[userId] | {userId}
        pq = []
        results = []

        for follower in followers:
            f_tweets = self.tweets[follower]

            if len(f_tweets) > 0:
                idx = len(f_tweets) -1
                t, tweet_id = f_tweets[idx] 
                hq.heappush(pq, (t, tweet_id , follower, idx))

        while pq:
            time, tweet, f, idx = hq.heappop(pq)

            if len(results) == 10:
                return results
            results.append(tweet)

            idx -= 1
            if idx < 0:
                continue

            nextTS, nextTweet = self.tweets[f][idx][0], self.tweets[f][idx][1]
            hq.heappush(pq, (nextTS, nextTweet, f, idx))

        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
