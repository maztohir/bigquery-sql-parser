from src.bigquery_sql_parser.line import Line
from src.bigquery_sql_parser.multiline import Multiline

text = """select
    column
    from
    where true"""

text_result = """select
    column
    column1
    from
    where true
    order by 1"""


def test_lines():
    multi = Multiline(text)
    assert len(multi.lines) == 4
    assert multi.get(1).text == "    column"


def test_add_line():
    multi = Multiline(text)
    multi.add(Line("    column1"), 2)
    multi.add(Line("    order by 1"))

    assert multi.text == text_result
    
def test_add_line():
    multi = Multiline(text)
    multi.add(Line("    column1"), 2)
    # indent = multi.get()
    multi.add("order by 1", auto_indent=True)

    assert multi.text == text_result