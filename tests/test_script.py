from src.bigquery_sql_parser.script import Script

    
syntax_cte = """
    CREATE FUNCTION x AS (());
    WITH
    tab1 AS (
        SELECT a,b,c FROM table_1
    ),
    tab2 AS (
        SELECT a,
            b,
            c 
        FROM 
            table_2
    ),
    tab2 AS (
        SELECT 
            a AS no,
            b AS yes,
            SUM(c) AS total 
        FROM 
            table_2
    )
    SELECT 
        no, yes,
        total
    FROM tab2
    """

def test_script_blocks():
    syntax = """
    DELETE TABLE x;
    
    INSERT INTO x;
    
    SELECT
        a,
        b,
        c,
    FROM d
    """

    script = Script(syntax)
    blocks = script.blocks
    assert blocks[0]._text == "\n    DELETE TABLE x;"
    assert blocks[2]._text == """\n    
    SELECT
        a,
        b,
        c,
    FROM d
    """
    
def test_script_ctes():
    script  = Script(syntax_cte)
    ctes = script.ctes
    assert ctes[0].text == """(
        SELECT a,b,c FROM table_1
    )"""
    assert ctes[2].text == """(
        SELECT 
            a AS no,
            b AS yes,
            SUM(c) AS total 
        FROM 
            table_2
    )"""