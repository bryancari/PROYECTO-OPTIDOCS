from typing import Optional
from datetime import datetime

class ResultOCR:
    def __init__(self, raw, clean, success, mistakes,
                 id: Optional [int] = None, created_at: Optional [datetime] = None):
        self.id = id
        self.raw = raw
        self.clean = clean
        self.success = success
        self.mistakes = mistakes
        self.created_at = created_at