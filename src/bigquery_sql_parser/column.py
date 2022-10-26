import re


class Column:
    def __init__(self, syntax:str, name=None, value=None):
        self.syntax = syntax
        self.name = self.find_name()
        self.value = self.find_value()

    def find_name(self):
        ALIAS_NAME_PATTERN = r"(\w*)$"
        matches = re.findall(ALIAS_NAME_PATTERN, self.syntax)
        if matches and matches != [""]:
            return matches[0]
        else:
            return self.syntax

    def find_value(self):
        CHECK_AS_PATTERN = r"(?i)(\s+as\s+)"
        VALUE_AS_PATTERN = r"(?i)(.*)(?:\s+as\s?)"

        CHECK_ANONYMOUS_AS_PATTERN = r"\w+\)?\s+\w+"
        VALUE_ANONYMOUS_AS_PATTERN = r"(.*)(?:\s+)"

        if re.findall(CHECK_AS_PATTERN, self.syntax):
            matches = re.findall(VALUE_AS_PATTERN, self.syntax)
            return matches[0]
        elif re.findall(CHECK_ANONYMOUS_AS_PATTERN, self.syntax):
            matches = re.findall(VALUE_ANONYMOUS_AS_PATTERN, self.syntax)
            return matches[0]
        else:
            return self.syntax
