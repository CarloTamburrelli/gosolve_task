from dataclasses import dataclass
from typing import Optional

@dataclass
class SearchResult:
    index: int
    value: int
    message: Optional[str] = None
