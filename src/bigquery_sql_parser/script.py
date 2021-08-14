from __future__ import annotations
from typing import List

from src.bigquery_sql_parser.cte import Cte
from src.bigquery_sql_parser.multiline import Multiline
from src.bigquery_sql_parser.tokenizer import Tokenizer
from src.bigquery_sql_parser.utils import read_file

import re

class Script(Multiline):
    
    CTE_AREA_PATTERN = r"(?i)with\s+(?:\w+\s+)(?:(?:AS)\s+)?\([^.]*\)"
    
    def __init__(self, text:str):
        self._text = text
    
    @classmethod
    def from_file(cls, path):
        text = read_file(path)
        return cls(text)
    
    @property
    def text(self):
        return self._text
    
    @property
    def blocks(self) -> List[Script]:
        original_text   = self._text
        tokenizer       = Tokenizer(original_text, tokenize_type=Tokenizer.TOKENIZE_TRIPLE_QUOTE)
        tokenized_text  = tokenizer.tokenized_text

        matches = re.findall(r"(?:[\w\S\s]+?);", tokenized_text)
        blocks = []
        for match in matches:
            match_translated = tokenizer.translate_text(match)
            block = Script(match_translated)
            blocks.append(block)
    
        outside_match = re.sub(r"(?:[\w\S\s]+?);", "", tokenized_text)
        if outside_match:
            block_left = re.findall(r"\w+", outside_match)
            if block_left:
                outside_match_translated = tokenizer.translate_text(outside_match)
                blocks.append(Script(outside_match_translated))
        
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
        
            
        