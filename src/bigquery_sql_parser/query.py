import re

from .multiline import Multiline
from .column import Column


class Query(Multiline):
    def __init__(self, syntax):
        super(Query, self).__init__(syntax)

    @property
    def _column_area(self):
        UNSEPARATED_COLUMN = r"(?i)(?:\s*select\s+)((?:(?![,\s]+from[`\s]+)[\S\s])*)(?:,?[,\s]+from[`\s]+)?"
        matches = re.findall(UNSEPARATED_COLUMN, self.syntax)
        if len(matches) > 1:
            raise ValueError("Query should contain only 1 SELECT statement")

        if matches:
            column_area = matches[0]
            return self._remove_unused_character(column_area)

        else:
            raise ValueError("SELECT statment not found")

    @property
    def _column_syntax(self):
        SEPARATED_COLUMN = r"(?i)(?!\s)([\w+\s\+\*\-\.]+)"
        matches = re.findall(SEPARATED_COLUMN, self._column_area)
        return matches

    def _remove_unused_character(self, syntax):
        UNUSED_CHARACTER_PATTERN = r"(?:[,\s]*)$"
        result = re.sub(UNUSED_CHARACTER_PATTERN, "", syntax)
        return result

    @property
    def full_table_ids(self):
        TABLE_PATTERN = r"(?i)(?:FROM|JOIN)\s+`?([\w-]+)\.([\w-]+)\.(\w+)"
        matches = re.findall(TABLE_PATTERN, self.syntax)
        return ["{}.{}.{}".format(match[0], match[1], match[2]) for match in matches]

    @property
    def columns(self):
        column_syntaxes = self._column_syntax
        columns = [Column(syntax) for syntax in column_syntaxes]
        return columns
