from __future__ import annotations
from typing import List

from src.bigquery_sql_parser.cte import Cte
from src.bigquery_sql_parser.multiline import Multiline
from src.bigquery_sql_parser.tokenizer import Tokenizer

import re

class Script(Multiline):
    
    CTE_AREA_PATTERN = r"(?i)with\s+(?:\w+\s+)(?:(?:AS)\s+)?\([^.]*\)"
    
    def __init__(self, text:str):
        self._text = text
    
    @property
    def text(self):
        return self._text
    
    @property
    def blocks(self) -> List[Script]:
        matches = re.findall(r"(?:[^.]+?);", self._text)
        blocks = []
        for match in matches:
            block = Script(match)
            blocks.append(block)
    
        outside_match = re.sub(r"(?:[^.]+?);", "", self._text)
        if outside_match:
            block_left = re.findall(r"\w+", outside_match)
            if block_left:
                blocks.append(Script(outside_match))
        
        return blocks

    @property
    def cte_area(self):
        matches = re.findall(self.CTE_AREA_PATTERN, self._text)
        if not matches:
            return ""
        match_str = "".join(matches)
        _, _, after_match = self._text.partition(match_str)
        return match_str + after_match
    
    @property
    def ctes(self) -> List[Cte]:
        cte_area = self.cte_area
        if not cte_area:
            return []
        
        tokenized = Tokenizer(cte_area).tokenized_syntax
        ctes = []
        for child in tokenized.childs:
            cte = Cte(child.translated_text)
            ctes.append(cte)
        return ctes
        
            
        