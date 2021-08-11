from enum import auto
from typing import Union
from .line import Line


class Multiline:
    def __init__(self, text:str):
        lines_split = text.split("\n")
        self.lines = [Line(line) for line in lines_split]

    @property
    def text(self):
        return "\n".join([line.text for line in self.lines])

    def get(self, index:int) -> Line:
        return self.lines[index]

    def get_before(self, index:int) -> Line:
        index = index - 1 if index > 1 else 0
        return self.get(index)

    def get_after(self, index:int) -> Line:
        index = index + 1
        return self.get(index)

    def last(self) -> Line:
        last_index = len(self.lines)
        return self.get(last_index-1)
    
    def _proposed_indent(self, index:int) -> str:
        indent = ''
        if index == None:
            indent = self.last().indentation
        elif index == 1:
            indent = self.get_after(index).indentation
        else:
            indent = self.get_before(index).indentation
        return indent

    def add(self, line: Union[Line, str], index:int=None, auto_indent:bool=False):
        if not isinstance(line, Line):
            line = Line(line)
        
        if auto_indent:
            indent = self._proposed_indent(index)
            line.indentation = indent
        
        if index:
            self.lines.insert(index, line)
        else:
            self.lines.append(line)
