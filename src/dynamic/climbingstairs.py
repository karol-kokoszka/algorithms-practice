def climbing_stairs(n: int) -> int:
    ways = [0, 1, 2]

    for i in range(3, n + 1):
        ways.append(ways[i - 2] + ways[i - 1])
    return ways[n]      
