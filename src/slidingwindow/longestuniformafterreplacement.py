from collections import defaultdict

def longest_uniform_substring_after_replacements(s: str, k: int) -> int:
    leftP, rightP = 0, 0
    highestFreq = 0
    currLength = 0
    occurrences = defaultdict(int)

    while rightP < len(s):
        occurrences[s[rightP]] += 1
        currLength = rightP - leftP + 1
        newMax = max(highestFreq, occurrences[s[rightP]])
        if currLength - newMax > k:
            occurrences[s[leftP]] -= 1
            leftP += 1
            currLength -= 1
        else:
            highestFreq = newMax
        rightP += 1

    return currLength
