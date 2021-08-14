from typing import List

class Cte:
    def __init__(self, name:str, text:str):
        self.text = self._remove_first_and_last_parenthesis(text)
        self.name = name

    def _remove_first_and_last_parenthesis(self, text):
        if text.startswith("(") and text.endswith(")"):
            text = text[1:-1]
        return text