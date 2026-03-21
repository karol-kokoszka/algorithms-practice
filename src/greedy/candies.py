from typing import List

"""
You teach a class of children sitting in a row, each of whom has a rating based on their performance. 
You want to distribute candies to the children while abiding by the following rules:
- Each child must receive at least one candy.
- If two children sit next to each other, the child with the higher rating must receive more candies.
- Determine the minimum number of candies you need to distribute to satisfy these conditions.
"""
def candies(ratings: List[int]) -> int:
    given = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            given[i] = given[i - 1] + 1
    for i in range(len(ratings) - 1, 0, -1):
        if ratings[i - 1] > ratings[i]:
            if given[i - 1] <= given[i]:
                given[i - 1] = given[i] + 1
    sum = 0
    for i in given:
        sum += i
    return sum
