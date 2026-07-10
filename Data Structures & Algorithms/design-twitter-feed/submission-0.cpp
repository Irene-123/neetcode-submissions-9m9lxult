class Twitter {
public:
    unordered_map<int, unordered_set<int>> followers;
    unordered_map<int, vector<pair<int, int>>> tweets;
    int time = 0;
    Twitter() {
    }
    
    void postTweet(int userId, int tweetId) {
        
        tweets[userId].push_back({time++, tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        
        unordered_set<int> userFollowers = followers[userId];
        userFollowers.insert(userId);
        priority_queue<pair<pair<int, int>, pair<int, int>>> pq;
        vector<int> feed;


        for (const auto& userFollower: userFollowers) {
            // Push (Tweet), (FollowerId, Current VectorIndex)
            auto userTweets = tweets[userFollower];

            if (!userTweets.empty()) {
                int idx = userTweets.size() - 1;
                pq.push({userTweets[idx], {userFollower, idx}});

            } 
        }

        while (!pq.empty() and feed.size() < 10) {

            auto p = pq.top();
            pq.pop();

            auto tweet = p.first;
            int follower = p.second.first;
            int idx = p.second.second;

            feed.push_back(tweet.second);

            idx--;

            if (idx >= 0) {
                auto newTweet = tweets[follower][idx];
                pq.push({newTweet, {follower, idx}});
            }
        }
        return feed;
    }
    
    void follow(int followerId, int followeeId) {
        
        followers[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {

        if (followers[followerId].find(followeeId) != followers[followerId].end())
            followers[followerId].erase(followeeId);
    }
};
