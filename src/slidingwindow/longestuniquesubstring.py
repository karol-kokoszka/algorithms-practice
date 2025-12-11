from collections import defaultdict

def longest_substring_with_unique_chars(s: str) -> int:
    if len(s) < 1:
        return 0
   
    occurrences = defaultdict(int)
    leftP, rightP = 0, 0

    longest = 0
    currLenght = 0
    while rightP < len(s):
        occurrences[s[rightP]] += 1
        if occurrences[s[rightP]] == 1:
            currLenght += 1
        else:
            if currLenght > longest:
                longest = currLenght
            while s[leftP] != s[rightP]:
                occurrences[s[leftP]] -= 1
                leftP += 1
                currLenght -= 1
            occurrences[s[leftP]] -= 1
            leftP += 1
        rightP += 1
    
    return longest if longest > currLenght else currLenght
   