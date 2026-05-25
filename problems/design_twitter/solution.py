from collections import defaultdict


class Twitter(object):

    def __init__(self):

        self.time = 0

        # user -> [(time, tweetId)]
        self.tweets = defaultdict(list)

        # follower -> set(followees)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId, tweetId):

        self.time += 1

        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):

        feed = []

        users = self.follow_map[userId].copy()

        users.add(userId)

        all_tweets = []

        # collect relevant tweets only
        for user in users:

            for tweet in self.tweets[user]:

                all_tweets.append(tweet)

        # sort by time descending
        all_tweets.sort(reverse=True)

        # take latest 10
        for i in range(min(10, len(all_tweets))):

            feed.append(all_tweets[i][1])

        return feed

    def follow(self, followerId, followeeId):

        if followerId != followeeId:

            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):

        if followeeId in self.follow_map[followerId]:

            self.follow_map[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)