import re


class Line:
    def __init__(self, content):
        self.content = content

    @property
    def identation(self):
        matches = re.match(r'^\s+', self.content)
        if matches:
            return matches.group(0)
        return ''

    @property
    def is_from_clause(self):
        return 'from' in self.content.lower()

    @property
    def is_select_clause(self):
        return 'select' in self.content.lower()

    @property
    def is_only_select_clause(self):
        matches = re.match(r'(?i)^\s*select\s*\n', self.content)
        return True if matches else False

    def add_comma(self):
        self.content = self.content+','
