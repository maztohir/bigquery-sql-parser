from __future__ import annotations
from typing import List

from src.bigquery_sql_parser.cte import Cte
from src.bigquery_sql_parser.multiline import Multiline
from src.bigquery_sql_parser.tokenizer import Tokenizer
from src.bigquery_sql_parser.utils import read_file

import re

class Script(Multiline):
    
    CTE_AREA_PATTERN = r"(?i)with\s+(?:\w+\s+)(?:(?:AS)\s+)?\([\w\S\s]*\)(?=\s+select)"
    
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

        matches = tokenized_text.split(';')
        blocks = []
        for match in matches:
            match_translated = tokenizer.translate_text(match)
            block = Script(match_translated)
            blocks.append(block)
    
        return blocks

    @property
    def cte_area(self):
        matches = re.findall(self.CTE_AREA_PATTERN, self._text)
        if not matches:
            return ""
        match_str = "".join(matches)
        return match_str
    
    @property
    def ctes(self) -> List[Cte]:
        cte_area = self.cte_area
        if not cte_area:
            return []
        
        tokenizer = Tokenizer(re.sub(r"(?i)with", "", cte_area))
        ctes_match_list = re.findall(
            r"(?i)(\w+\s+)(?:(?:AS)\s+)?({}\w+)".format(tokenizer.token_prefix),
            tokenizer.tokenized_text
        )

        cte_list = []
        if ctes_match_list:
            for cte_group in ctes_match_list:
                cte_name = cte_group[0]
                cte_token = cte_group[1]
                cte_str = tokenizer.translate_key(cte_token, recursive=True)
                cte = Cte(cte_name, cte_str)
                cte_list.append(cte)

        return cte_list

    @property
    def final_cte_query(self):
        _, _, after_match = self._text.partition(self.cte_area)
        return after_match
        
    @property
    def is_temp_function(self):
        matches = re.findall('(?i:CREATE TEMPORARY FUNCTION)', self._text)
        if matches:
            return True
        return False

    @property
    def is_insert_statement(self):
        matches = re.findall('(?i:INSERT INTO)', self._text)
        if matches:
            return True
        return False

    @property
    def is_update_statement(self):
        matches = re.findall('(?i:UPDATE)', self._text)
        if matches:
            return True
        return False

    @property
    def is_delete_statement(self):
        matches = re.findall('(?i:DELETE FROM)', self._text)
        if matches:
            return True
        return False

    @property
    def is_cte_statement(self):
        matches = re.findall('(?i:WITH)', self._text)
        if matches:
            return True
        return False

    @property
    def is_select_statement(self):
        matches = re.findall('(?i:SELECT)', self._text)
        if matches:
            return True
        return False
