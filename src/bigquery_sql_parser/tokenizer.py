from __future__ import annotations
from typing import List

from .utils import hash_string

import re
class TokenizedSyntax:
    def __init__(self, tokenized_text:str, translated_text:str, keys:List[str], knowledge:dict, childs:List[TokenizedSyntax]) -> None:
        self.translated_text = translated_text
        self.tokenized_text = tokenized_text
        self.keys = keys
        self.knowledge = knowledge
        self.childs = childs

class Tokenizer:

    TOKENIZE_PARENTHESES = "tokenize_parentheses"
    TOKENIZE_COLUMN_PARENTHESES = "tokenize_column_parentheses"
    TOKENIZE_TRIPLE_QUOTE = "tokenize_triple_quote"

    def __init__(self, text, token_prefix="BQ00012_", tokenize_type=TOKENIZE_PARENTHESES):
        self.text = text
        if tokenize_type == self.TOKENIZE_TRIPLE_QUOTE:
            self.text = text.replace("'''", '"""')

        self.token_prefix = token_prefix
        self.tokenize_type = tokenize_type
        self.tokenized_text, self.knowledge = self._tokenize(self.text)

    def translate_key(self, key, recursive=False):
        value = self.knowledge[key]
        if recursive:
            sub_keys = self._find_keys(value)
            for sub_key in sub_keys:
                value = value.replace(
                    sub_key, self.translate_key(sub_key, recursive=recursive)
                )
        return value

    def _remove_first_and_last_parenthesis(self, text):
        if text.startswith("(") and text.endswith(")"):
            text = text[1:-1]
        return text

    def _tokenize_pattern(self):
        return {
            self.TOKENIZE_PARENTHESES: r"\w*\((?:[^()]|\([\w\S\s]*?\))*\)",
            self.TOKENIZE_COLUMN_PARENTHESES: r"\w*\s*\((?:[^()]|\([\w\S\s]*?\))*\)",
            self.TOKENIZE_TRIPLE_QUOTE: r'"""[\w\S\s]*?"""',
        }[self.tokenize_type]

    def _find_parenthesis(self, text):
        LOWER_TOKENIZE_PATTERN = self._tokenize_pattern()
        return re.findall(
            LOWER_TOKENIZE_PATTERN, self._remove_first_and_last_parenthesis(text)
        )

    def _find_lowest_parenthesis(self, text):
        lowest = []
        matches = self._find_parenthesis(text)

        if not matches:
            lowest.append(text)

        for match in matches:
            if match == text:
                lowest.append(match)
            else:
                _lowest = self._find_lowest_parenthesis(match)
                lowest = lowest + _lowest

        return lowest

    def _find_keys(self, text):
        KEY_PATTERN = r"({}\w+)".format(self.token_prefix)
        matches = re.findall(KEY_PATTERN, text)
        return matches

    def translate_text(self, text):
        keys = self._find_keys(text)
        for key in keys:
            text = text.replace(key, self.translate_key(key, recursive=True))
        return text
    
    def _extract_key(self, key, recursive=False) -> TokenizedSyntax:
        value = self.knowledge[key]
        translated = self.translate_text(value)
        keys = self._find_keys(value)
        knowledges = { key: self.knowledge[key] for key in keys }
        childs = []

        if recursive:
            for sub_key in keys:
                child = self._extract_key(sub_key, recursive=recursive)
                childs.append(child)
        return TokenizedSyntax(value, translated, keys, knowledges, childs)
    
    @property
    def tokenized_syntax(self):
        tokenized_text = self.tokenized_text
        translated = self.translate_text(tokenized_text)
        keys = self._find_keys(tokenized_text)
        knowledges = { key: self.knowledge[key] for key in keys }
        childs = []
        for sub_key in keys:
            child = self._extract_key(sub_key, recursive=True)
            childs.append(child)
        return TokenizedSyntax(tokenized_text, translated, keys, knowledges, childs)        

    def _tokenize(self, text):
        knowledge = {}

        while self._find_parenthesis(text):
            lowests = self._find_lowest_parenthesis(text)
            for lowest in lowests:
                token = self.token_prefix + hash_string(lowest)
                knowledge[token] = lowest
                text = text.replace(lowest, token)

        return text, knowledge
