from bigquery_sql_parser.column import Column


def test_alias_name():
    assert Column("name").name == "name"
    assert Column("name1 name").name == "name"
    assert Column("name3 name").name == "name"
    assert Column("name3 as name").name == "name"
    assert Column(".").name == "."


def test_column_value():
    assert Column("name1 name").value == "name1"
    assert Column("name3 AS name").value == "name3"
    assert Column("name").value == "name"
