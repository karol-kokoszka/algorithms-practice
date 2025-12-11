# In number theory, a happy number is defined as a number that, 
# when repeatedly subjected to the process of squaring its digits
# and summing those squares, eventually leads to 1.
# An unhappy number will never reach 1 during this process,
# and will get stuck in an infinite loop.

def happy_number(n: int) -> bool:
    visited = set()
    while n not in visited and n != 1:
        visited.add(n)
        n = square_digits_and_sum(n)
    return True if n == 1 else False

def square_digits_and_sum(n: int) -> int:
    newNumber = 0
    while n // 10 > 0 or n % 10 > 0:
        newNumber += (n % 10) ** 2
        n = n // 10
    return newNumber