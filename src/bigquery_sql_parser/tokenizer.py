import re

from .utils import hash_string


class Tokenizer(object):
    def __init__(self, syntax, prefix="BQ00012_"):
        self.syntax = syntax
        self.prefix = prefix
        self.tokenized_syntax, self.knowledge = self._tokenize(syntax)

    def translate_key(self, key, recursive=False):
        value = self.knowledge[key]
        if recursive:
            sub_keys = self._find_keys(value)
            for sub_key in sub_keys:
                value = value.replace(
                    sub_key, self.translate_key(sub_key, recursive=True)
                )
        return value

    def _remove_first_and_last_parenthesis(self, syntax):
        if syntax.startswith("(") and syntax.endswith(")"):
            syntax = syntax[1:-1]
        return syntax

    def _find_parenthesis(self, syntax):
        FIND_PARENTHESIS_PATTERN = r"\w*\((?:[^()]*|\([^.]*\))*\)"
        return re.findall(
            FIND_PARENTHESIS_PATTERN, self._remove_first_and_last_parenthesis(syntax)
        )

    def _find_lowest_parenthesis(self, syntax):
        lowest = []
        matches = self._find_parenthesis(syntax)

        if not matches:
            lowest.append(syntax)

        for match in matches:
            if match == syntax:
                lowest.append(match)
            else:
                _lowest = self._find_lowest_parenthesis(match)
                lowest = lowest + _lowest

        return lowest

    def _find_keys(self, syntax):
        KEY_PATTERN = r"({}\w+)".format(self.prefix)
        matches = re.findall(KEY_PATTERN, syntax)
        return matches

    def _translate_syntax(self, syntax):
        keys = self._find_keys(syntax)
        for key in keys:
            syntax = syntax.replace(key, self.translate_key(key, recursive=True))
        return syntax

    def _tokenize(self, syntax):
        knowledge = {}

        while self._find_parenthesis(syntax):
            lowests = self._find_lowest_parenthesis(syntax)
            for lowest in lowests:
                token = self.prefix + hash_string(lowest)
                knowledge[token] = lowest
                syntax = syntax.replace(lowest, token)

        return syntax, knowledge
