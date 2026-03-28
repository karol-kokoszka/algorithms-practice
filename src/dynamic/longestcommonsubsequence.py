"""
Given two strings, find the length of their longest common subsequence (LCS). 
A subsequence is a sequence of characters that can be derived from a string 
by deleting zero or more elements, without changing the order of the remaining elements.
"""
def longest_common_subsequence(s1: str, s2: str) -> int:
    if len(s1) == 0 or len(s2) == 0:
        return 0
    maxSubsenqunce = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    
    if s1[0] == s2[0]:
        maxSubsenqunce[0][0] = 1

    for i in range(1, len(s1)):
        if s1[i] == s2[0]:
            maxSubsenqunce[i][0] = 1
        else:
            maxSubsenqunce[i][0] = maxSubsenqunce[i - 1][0]
    
    for j in range(1, len(s2)):
        if s1[0] == s2[j]:
            maxSubsenqunce[0][j] = 1
        else:
            maxSubsenqunce[0][j] = maxSubsenqunce[0][j - 1]

    for j in range(1, len(s2)):
        for i in range(1, len(s1)):
            maxSubsenqunce[i][j] = max(maxSubsenqunce[i][j - 1], 
                                       maxSubsenqunce[i - 1][j - 1] if s1[i] != s2[j] else maxSubsenqunce[i - 1][j - 1] + 1,
                                       maxSubsenqunce[i -1][j])

    return maxSubsenqunce[len(s1) - 1][len(s2) - 1]