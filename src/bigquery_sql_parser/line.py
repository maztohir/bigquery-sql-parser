import re


class Line:
    def __init__(self, text:str, indentation:str=""):
        self._text = indentation + text
        self._indentation = self._get_indent(text)
        self._syntax = self._get_syntax(text)

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, value):
        self._text = value
        self._indentation = self._get_indent(value)
        self._syntax = self._get_syntax(value)
        
    @property
    def syntax(self):
        return self._syntax
    
    @syntax.setter
    def syntax(self, value):
        self._syntax = value
        self._text = self._indentation + value
    
    @property
    def indentation(self):
        return self._indentation
    
    @indentation.setter
    def indentation(self, value):
        self._indentation = value
        self._text = value + self._syntax
    
    def _get_syntax(self, value):
        return re.sub(r"^\s+", "", value)
    
    def _get_indent(self, value):
        matches = re.match(r"^\s+", value)
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
