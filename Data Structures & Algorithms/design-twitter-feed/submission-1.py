from collections import defaultdict
class Twitter:

    def __init__(self):
        #initialse twitter object, but idk what to initialise
        #initialise tweets dict with tweetid as key and user id as value
        #follow dict for storing userid as key and following ids as values
        self.tweets=defaultdict(list)
        self.followList=defaultdict(set)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        #create a new tweet with unique id by the user id and add it to tweets
        self.time-=1
        self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        #use a min heap to get the latest tweets from the follow list of user and find min heap root and 
        #add it to the list of 10 tweets, once one from the follow list is taken replace it with next from that user
        topTenTweets=[]
        minHeap=[]

        self.followList[userId].add(userId)
        #list of following users
        #last tweets from all of that list
        #while min heap, popleft and add to topTenTweets
        #if that tweet index is not zero then add its predecessor to min heap
        # do this until topTenTweets is full i.e len(topTenTweets)==10

        for followingId in self.followList[userId]:
            if followingId in self.tweets:
                index=len(self.tweets[followingId])-1
                tweetTime,tweetId=self.tweets[followingId][index]
                heapq.heappush(minHeap,(tweetTime,tweetId,followingId,index))

        
        while minHeap and len(topTenTweets)<10:
                tweetTime,tweetId,followingId,index=heapq.heappop(minHeap)
                topTenTweets.append(tweetId)

                if index!=0:
                    index-=1
                    tweetTime,tweetId=self.tweets[followingId][index]
                    heapq.heappush(minHeap,(tweetTime,tweetId,followingId,index))
        
        return topTenTweets
                

    def follow(self, followerId: int, followeeId: int) -> None:
        #add the followee id to the list of following accounts of user(followerId)
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #remove followee id from that list
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)
