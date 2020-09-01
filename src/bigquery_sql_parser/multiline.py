from .line import Line


class Multiline(object):
    def __init__(self, syntax):
        lines_split = syntax.split("\n")
        self.lines = [Line(line) for line in lines_split]

    @property
    def syntax(self):
        return "\n".join([line.syntax for line in self.lines])

    def get(self, index):
        return self.lines[index]

    def add(self, line, index=None):
        if index:
            self.lines.insert(index, line)
        else:
            self.lines.append(line)
