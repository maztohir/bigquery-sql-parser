import re


class Line:
    def __init__(self, text, identation=""):
        self._text = identation + text

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = value
        
    @property
    def syntax(self):
        return re.sub(r"^\s+", "", self._text)
    
    @syntax.setter
    def syntax(self, value):
        self._text = self.indentation + value
    
    @property
    def indentation(self):
        matches = re.match(r"^\s+", self._text)
        if matches:
            return matches.group(0)
        return ""

    @property
    def is_from_clause(self):
        matches_normal = re.match(r'(?i)[\s,`\'\"]+from[\s,`\'\"]+', self._text)
        matches_first_line = re.match(r'(?i)^from[\s,`\'\"]+', self._text)
        return True if (matches_normal or matches_first_line) else False

    @property
    def is_select_clause(self):
        return "select" in self._text.lower()

    @property
    def is_only_select_clause(self):
        matches = re.match(r"(?i)^\s*select\s*\n", self._text)
        return True if matches else False

    def add_comma(self):
        self._text = self._text + ","
