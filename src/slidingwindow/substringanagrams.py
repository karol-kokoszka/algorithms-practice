from collections import defaultdict

def substring_anagrams(s: str, t: str) -> int:
    if len(s) < len(t) or len(t) == 0:
        return 0
    leftP, rightP = 0, len(t) - 1
    tOccur = defaultdict(int)
    sOccur = defaultdict(int)
    i, matchesCount = 0, 0
    for i in range(len(t)):
        tOccur[t[i]] += 1
        sOccur[s[i]] += 1

    while rightP < len(s):
        matches = True
        for key, value in tOccur.items():
            if sOccur[key] - value < 0:
                matches = False
                break
        if matches:
            matchesCount += 1
        sOccur[s[leftP]] -= 1
        leftP += 1
        rightP += 1
        if rightP < len(s):
            sOccur[s[rightP]] += 1
    return matchesCount
    
    
