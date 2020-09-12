import re


class Column(object):
    def __init__(self, syntax):
        self.syntax = syntax

    @property
    def name(self):
        ALIAS_NAME_PATTERN = r"(\w*)$"
        matches = re.findall(ALIAS_NAME_PATTERN, self.syntax)
        if matches and matches != [""]:
            return matches[0]
        else:
            return self.syntax

    @property
    def value(self):
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
