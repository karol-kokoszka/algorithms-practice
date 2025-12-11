def is_palindrome_valid(s: str) -> bool:    
    start, end = 0, len(s) - 1
    while start < end:
        while start < end and not s[start].isalnum():
            start+=1
        while start < end and not s[end].isalnum():
            end-=1
        if not start < end:
            return True
        if s[start] != s[end]:
            return False
        start+=1
        end-=1
    return True
    