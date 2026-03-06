from typing import List, Set
from collections import deque

letters = "abcdefghijklmnopqrstuvwxyz"


def shortest_transformation_sequence(start: str, end: str, dictionary: List[str]) -> int:
    if start not in dictionary or end not in dictionary:
        return 0

    word_set = set(dictionary)
    q = deque([(start, 1)])
    visited = {start}

    while q:
        word, distance = q.popleft()

        if word == end:
            return distance

        for neighbor in build_transformations(word):
            if neighbor in word_set and neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, distance + 1))

    return 0


def build_transformations(word: str) -> Set[str]:
    result = set()
    for i in range(len(word)):
        for c in letters:
            if c != word[i]:
                result.add(word[:i] + c + word[i + 1:])
    return result