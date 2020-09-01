from bigquery_sql_parser.line import Line
from bigquery_sql_parser.multiline import Multiline

syntax = """select
    column
    from
    where true"""

syntax_result = """select
    column
    column1
    from
    where true
    order by 1"""


def test_lines():
    multi = Multiline(syntax)
    assert len(multi.lines) == 4
    assert multi.get(1).syntax == "    column"


def test_add_line():
    multi = Multiline(syntax)
    multi.add(Line("    column1"), 2)
    multi.add(Line("    order by 1"))

    assert multi.syntax == syntax_result
