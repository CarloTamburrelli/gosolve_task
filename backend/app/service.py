from bisect import bisect_left
from typing import List, Optional
from .models import SearchResult




class SearchService:
    def __init__(self, file_path: str):
        self.values = self.load_values(file_path)
        self.value_to_index = {v: i for i, v in enumerate(self.values)}
    
    def load_values(self, path: str) -> List[int]:
        with open(path) as f:
            return list(map(int, f.read().split()))

    def search(self, target: int) -> Optional[SearchResult]:
        '''
            The algorithm first searches for the value in the hash map. 
            If it's not found, it then performs a binary search on the list.
        '''

        if not isinstance(target, int):
            raise TypeError("Expected an integer as target")

        if target in self.value_to_index:
            return SearchResult(index=self.value_to_index[target], value=target)

        pos = bisect_left(self.values, target)
        tolerance = target * 0.1
        best_match = None
        for i in [pos - 1, pos, pos + 1]:
            if 0 <= i < len(self.values):
                diff = abs(self.values[i] - target)
                if diff <= tolerance:
                    if best_match is None or diff < abs(best_match[1] - target):
                        best_match = (i, self.values[i])
        
        if best_match:
            return SearchResult(index=best_match[0], value=best_match[1], message="Approximate match")

        return None
