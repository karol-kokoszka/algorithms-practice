from typing import List

"""
You plan to rob houses in a street where each house stores a certain amount of money. 
The neighborhood has a security system that sets off an alarm when two adjacent houses are robbed. 
Return the maximum amount of cash that can be stolen without triggering the alarms.
"""
def neighborhood_burglary(houses: List[int]) -> int:
    if len(houses) == 0:
        return 0
    if len(houses) == 1:
        return houses[0]
    if len(houses) == 2:
        return max(houses[0], houses[1])
    
    # array of tuples (last home robbed, last home not robbed)
    # n(x) = current + max(n(x - 2)), max(n(x - 1))
    best = []
    best.append((houses[0], 0))
    best.append((houses[1], houses[0]))

    for i in range(2, len(houses)):
        best.append((houses[i] + max(best[i - 2][0], best[i - 2][1]),
                     max(best[i - 1][0], best[i - 1][1])))
        
    return max(best[len(houses) - 1][0], best[len(houses) - 1][1])