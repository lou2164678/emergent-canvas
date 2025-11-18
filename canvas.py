import re
from typing import List, Dict, Any

class Canvas:
    def __init__(self, width: int = 32, height: int = 24):
        self.width = width
        self.height = height
        self.grid: List[List[str]] = [[" " for _ in range(width)] for _ in range(height)]
        self.colors: List[List[str]] = [["white" for _ in range(width)] for _ in range(height)]  # not rendered yet, but ready for future
        self.history: List[str] = []
    
    def set(self, x: int, y: int, char: str):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = char
            self.history.append(f"Pixel set at ({x},{y}) to '{char}'")
    
    def fill(self, x1: int, y1: int, x2: int, y2: int, char: str):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.grid[y][x] = char
        self.history.append(f"Fill ({x1},{y1})-({x2},{y2}) with '{char}'")
    
    def clear(self):
        self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]
        self.history.append("Canvas cleared")
    
    def render_ascii(self) -> str:
        border = "+" + "-" * self.width + "+"
        lines = [border]
        for row in self.grid:
            lines.append("|" + "".join(row) + "|")
        lines.append(border)
        return "\n".join(lines)
    
    def get_recent_events(self, n: int = 5) -> str:
        return "\n".join(self.history[-n:]) or "No recent events."
