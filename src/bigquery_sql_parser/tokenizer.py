import re
from .utils import hash_string


class Tokenizer:
    def __init__(self, syntax, prefix=""):
        self.syntax = syntax
        self.tokenized_syntax, self.knowledge = self._tokenize(syntax, prefix=prefix)

    def _remove_first_and_last_parenthesis(self, syntax):
        if syntax.startswith("(") and syntax.endswith(")"):
            syntax = syntax[1:-1]
        return syntax

    def find_parenthesis(self, syntax):
        FIND_PARENTHESIS = r"\w*\((?:[^()]*|\([^.]*\))*\)"
        return re.findall(
            FIND_PARENTHESIS, self._remove_first_and_last_parenthesis(syntax)
        )

    def find_lowest_parenthesis(self, syntax):
        lowest = []
        matches = self.find_parenthesis(syntax)

        if not matches:
            lowest.append(syntax)

        for match in matches:
            if match == syntax:
                lowest.append(match)
            else:
                _lowest = self.find_lowest_parenthesis(match)
                lowest = lowest + _lowest

        return lowest

    def _tokenize(self, syntax, prefix=""):
        knowledge = {}

        while self.find_parenthesis(syntax):
            lowests = self.find_lowest_parenthesis(syntax)
            for lowest in lowests:
                token = prefix + hash_string(lowest)
                knowledge[token] = lowest
                syntax = syntax.replace(lowest, token)

        return syntax, knowledge
