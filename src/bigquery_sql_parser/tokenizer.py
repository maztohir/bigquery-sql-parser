from __future__ import annotations
from typing import List

from .utils import hash_string

import re
class Token:
    def __init__(self, text:str, keys:List[str], knowledge:dict, child:List[TokenizedSyntax]) -> None:
        self.text = text
        self.keys = keys
        self.knowledge = knowledge
        self.child = child

class Tokenizer:
    def __init__(self, text, prefix="BQ00012_"):
        self.text = text
        self.prefix = prefix
        self.tokenized_text, self.knowledge = self._tokenize(text)

    def translate_key(self, key, recursive=False):
        value = self.knowledge[key]
        if recursive:
            sub_keys = self._find_keys(value)
            for sub_key in sub_keys:
                value = value.replace(
                    sub_key, self.translate_key(sub_key, recursive=True)
                )
        return value

    def _remove_first_and_last_parenthesis(self, text):
        if text.startswith("(") and text.endswith(")"):
            text = text[1:-1]
        return text

    def _find_parenthesis(self, text):
        FIND_PARENTHESIS_PATTERN = r"\w*\((?:[^()]|\([^.]*\))*\)"
        return re.findall(
            FIND_PARENTHESIS_PATTERN, self._remove_first_and_last_parenthesis(text)
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
        KEY_PATTERN = r"({}\w+)".format(self.prefix)
        matches = re.findall(KEY_PATTERN, text)
        return matches

    def _translate_text(self, text):
        keys = self._find_keys(text)
        for key in keys:
            text = text.replace(key, self.translate_key(key, recursive=True))
        return text

    def _tokenize(self, text):
        knowledge = {}

        while self._find_parenthesis(text):
            lowests = self._find_lowest_parenthesis(text)
            for lowest in lowests:
                token = self.prefix + hash_string(lowest)
                knowledge[token] = lowest
                text = text.replace(lowest, token)

        return text, knowledge
