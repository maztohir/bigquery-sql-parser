import re

from .multiline import Multiline


class QueryRef(Multiline):
    def __init__(self, syntax):
        super().__init__(syntax)
        self._map = {}

    @property
    def _unseparated_column(self):
        UNSEPARATED_COLUMN = (
            r"(?i)(?:\s*select\s+)((?:(?!\s+from\s+)[\S\s])*)(?:\s+from\s*)?"
        )
        matches = re.findall(UNSEPARATED_COLUMN, self.syntax)
        if matches:
            return matches[0]
        return ""

    @property
    def columns(self):
        SEPARATED_COLUMN = r"([\.\w]+)"
        matches = re.findall(SEPARATED_COLUMN, self._unseparated_column)
        return matches

    @property
    def full_table_ids(self):
        TABLE_PATTERN = r"(?i)(?:FROM|JOIN)\\s+`?([\\w-]+)\\.([\\w-]+)\\.(\\w+)`?"
        matches = re.findall(TABLE_PATTERN, self.query)
        return [f"{match[0]}.{match[1]}.{match[2]}" for match in matches]
