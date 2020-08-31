
from bigquery_sql_parser.line import Line


def test_identation():
    string = '    column_name'

    line = Line(string)
    assert len(line.identation) == 4


def test_from_clause():
    string = '  from table'

    line = Line(string)
    assert line.is_from_clause


def test_select_clause():
    string = 'select * from table'

    line = Line(string)
    assert line.is_select_clause
    assert not line.is_only_select_clause


def test_add_comma():
    string = 'select name'

    line = Line(string)
    line.add_comma()
    assert line.content == 'select name,'
