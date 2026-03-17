from typing import List

def min_coin_combination(coins: List[int], target: int) -> int:
    min_coin = [0]
    for i in range(1, target + 1):
        min_coin.append(float('inf'))
        for c in coins:
            if i >= c:
                min_coin[i] = min(min_coin[i], 1 + min_coin[i - c])
    return min_coin[target] if min_coin[target] != float('inf') else -1