class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __eq__(self, other: Interval) -> bool:
        return self.start == other.start and self.end == other.end
    
    def __str__(self) -> str:
         return f"[{self.start}, {self.end}]"