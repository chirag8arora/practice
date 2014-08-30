# AC Rate: 18.9%
# SOURCE URL: https://oj.leetcode.com/problems/candy/
# 
# 

# There are N children standing in a line. Each child is assigned a rating value. 

# 
# 

# You are giving candies to these children subjected to the following requirements:

# 
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# 
# 

# What is the minimum candies you must give?

# 
# 


class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = []
        start = 0
        last_candy = 0
        last_rating = ratings[0]
        for k, v in enumerate(ratings):
            if v <= last_rating:
                if v == last_rating:
                    start = k
                if v < last_rating and candies[-1] == 1:
                    pointer = len(candies) - 1
                    candies[pointer] += 1
                    while(pointer - 1 >= 0 and ratings[pointer] < ratings[pointer - 1] and candies[pointer] >= candies[pointer - 1]):
                        pointer -= 1
                        candies[pointer] += 1
                last_candy = 1
            else:
                last_candy += 1
                start = k
            candies.append(last_candy)
            last_rating = v
        return sum(candies)
