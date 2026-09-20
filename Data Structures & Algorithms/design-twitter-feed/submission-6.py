from collections import defaultdict

class Twitter:
    """
    postTweet --> publish new tweet with ID tweetId, by user userId.
    getNewsFeed --> 10 most recent tweetIds in given user's news feed. all of the items must belong to users followed by this user. Most recent to least recent
    
    > hashmap of userId : set<userId> --> all userIds followed by key userId
    > unfollow, follow --> remove from this list. --> add, remove in O(1) time.Anyway cant have duplicates
    > hashmap of userId : max heap of tweetIds given by recency.
    > We queried return all max_heaps to get news feed. Iterate from 1 to 10, and across the first top elements across all heaps. Take the largest highest one (most recent timestamp) and repeat 10 times.
    """

    timestamp : int
    users_and_followers : dict 
    users_and_tweets : dict

    def __init__(self):
        self.timestamp = 0
        self.users_and_followers = defaultdict(set)
        self.users_and_tweets = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1 #add 1 more cycle

        #check if user inside users_and_tweets -> already posted smth
        if userId in self.users_and_tweets:
            tweets_max_heap = self.users_and_tweets[userId]
            heapq.heappush(tweets_max_heap, (-self.timestamp, tweetId))
            self.users_and_tweets[userId] = tweets_max_heap

        else:
            tweets = []
            heapq.heapify(tweets)

            heapq.heappush(tweets, (-self.timestamp, tweetId))

            self.users_and_tweets[userId] = tweets
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.timestamp += 1
        all_followed_users = self.users_and_followers[userId]

        print(userId, all_followed_users)

        top_10 = []
        tweets_to_add_back = defaultdict(set)
        
        for i in range(10):

            max_per_iter = None

            for followed_user in all_followed_users:
                followed_tweets = self.users_and_tweets[followed_user]

                if len(followed_tweets) == 0:
                    continue
                
                top_tweet = heapq.heappop(followed_tweets)

                if max_per_iter == None:
                    max_per_iter = (followed_user, top_tweet)
                    tweets_to_add_back[followed_user].add(top_tweet)
                
                elif -max_per_iter[1][0] < -top_tweet[0]:
                    heapq.heappush(self.users_and_tweets[max_per_iter[0]], max_per_iter[1])
                    tweets_to_add_back[max_per_iter[0]].remove(max_per_iter[1])
                    
                    max_per_iter = (followed_user, top_tweet)
                    tweets_to_add_back[followed_user].add(top_tweet)
                
                else:
                    heapq.heappush(self.users_and_tweets[followed_user], top_tweet) # put back


            if userId in self.users_and_tweets:

                tweets = self.users_and_tweets[userId]

                if len(tweets) == 0:

                    if max_per_iter == None:
                        continue
                    
                    top_10.append(max_per_iter[1][1])
                    
                    continue
                
                user_own_top_tweet = heapq.heappop(self.users_and_tweets[userId])
                
                if max_per_iter == None:
                    max_per_iter = (userId, user_own_top_tweet)
                    tweets_to_add_back[userId].add(user_own_top_tweet)
                
                elif -max_per_iter[1][0] < -user_own_top_tweet[0]:
                    heapq.heappush(self.users_and_tweets[max_per_iter[0]], max_per_iter[1])
                    tweets_to_add_back[max_per_iter[0]].remove(max_per_iter[1])
                    
                    max_per_iter = (userId, user_own_top_tweet)
                    tweets_to_add_back[userId].add(user_own_top_tweet)
                
                else:
                    heapq.heappush(self.users_and_tweets[userId], user_own_top_tweet) # put back

            if max_per_iter == None:
                continue
            
            top_10.append(max_per_iter[1][1])

        #Add back all of the popped tweets to their respective user heaps. 
        for user_id in tweets_to_add_back:
            tweets_heap_for_user = self.users_and_tweets[user_id]
            
            for tweet_to_add in tweets_to_add_back[user_id]:
                heapq.heappush(tweets_heap_for_user, tweet_to_add)
            
            self.users_and_tweets[user_id] = tweets_heap_for_user

        return top_10 
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.timestamp += 1
        self.users_and_followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.timestamp += 1
        if followerId in self.users_and_followers.keys():
            if followeeId in self.users_and_followers[followerId]:
                self.users_and_followers[followerId].remove(followeeId)
            else:
                print(f"Error, followeeId not present in followed users by {followerId}")
        
