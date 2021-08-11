import re


class Line:
    def __init__(self, syntax, identation=""):
        self.syntax = identation + syntax

    @property
    def indentation(self):
        matches = re.match(r"^\s+", self.syntax)
        if matches:
            return matches.group(0)
        return ""

    @property
    def is_from_clause(self):
        matches_normal = re.match(r'(?i)[\s,`\'\"]+from[\s,`\'\"]+', self.syntax)
        matches_first_line = re.match(r'(?i)^from[\s,`\'\"]+', self.syntax)
        return True if (matches_normal or matches_first_line) else False

    @property
    def is_select_clause(self):
        return "select" in self.syntax.lower()

    @property
    def is_only_select_clause(self):
        matches = re.match(r"(?i)^\s*select\s*\n", self.syntax)
        return True if matches else False

    def add_comma(self):
        self.syntax = self.syntax + ","
