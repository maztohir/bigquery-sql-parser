import pytest

from bigquery_sql_parser.query import Query


def test_column_area_without_from():
    syntax = "select name, johan"
    query = Query(syntax)
    assert query._column_area == "name, johan"


def test_column_area_without_from_with_space():
    syntax = "select name, johan, "
    query = Query(syntax)
    assert query._column_area == "name, johan"


def test_column_area_with_from():
    syntax = "select name, johan, from`table`"
    query = Query(syntax)
    assert query._column_area == "name, johan"


def test_columns():
    syntax = "select name, johan, adi* raka cika, street as street_name from `table`"
    query = Query(syntax)
    assert query._column_syntax == [
        "name",
        "johan",
        "adi* raka cika",
        "street as street_name",
    ]


def test_table_id():
    syntax = "select name from `project-id.dataset.table`"
    query = Query(syntax)
    assert query.full_table_ids == ["project-id.dataset.table"]


def test_multiple_query_select():
    syntax = "select name, johan from tommy select id from a"
    query = Query(syntax)
    with pytest.raises(ValueError) as e:
        query._column_area
    assert str(e.value) == "Query should contain only 1 SELECT statement"


def test_not_found_select_statement():
    syntax = "name, johan from tommy"
    query = Query(syntax)
    with pytest.raises(ValueError) as e:
        query._column_area
    assert str(e.value) == "SELECT statment not found"


def test_query_columns():
    syntax = """
    SELECT 
        name,
        addresses address,
        62 + phone as phone_number,
        2020 - birth_year year_old
    FROM table_id
    """
    query = Query(syntax)
    columns = query.columns
    column_names = [column.name for column in columns]
    column_values = [column.value for column in columns]
    column_syntax = [column.syntax for column in columns]

    assert column_names == ["name", "address", "phone_number", "year_old"]
    assert column_values == ["name", "addresses", "62 + phone", "2020 - birth_year"]
    assert column_syntax == [
        "name",
        "addresses address",
        "62 + phone as phone_number",
        "2020 - birth_year year_old",
    ]
