import re


class Line(object):
    def __init__(self, syntax, identation=""):
        self.syntax = identation + syntax

    @property
    def identation(self):
        matches = re.match(r"^\s+", self.syntax)
        if matches:
            return matches.group(0)
        return ""

    @property
    def is_from_clause(self):
        return "from" in self.syntax.lower()

    @property
    def is_select_clause(self):
        return "select" in self.syntax.lower()

    @property
    def is_only_select_clause(self):
        matches = re.match(r"(?i)^\s*select\s*\n", self.syntax)
        return True if matches else False

    def add_comma(self):
        self.syntax = self.syntax + ","
