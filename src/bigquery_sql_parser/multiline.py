from typing import Union
from .line import Line


class Multiline:
    def __init__(self, text):
        lines_split = text.split("\n")
        self.lines = [Line(line) for line in lines_split]

    @property
    def text(self):
        return "\n".join([line.text for line in self.lines])

    def get(self, index) -> Line:
        return self.lines[index]

    def add(self, line: Union[Line, str], index=None, auto_indent=False):
        if not isinstance(line, Line):
            line = Line(line)
            
        if index:
            self.lines.insert(index, line)
        else:
            self.lines.append(line)
