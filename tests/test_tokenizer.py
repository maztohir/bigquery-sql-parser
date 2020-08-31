from bigquery_sql_parser.tokenizer import Tokenizer

syntax = """select
    name,
    cast(phone as int) table
  from
    (select * peoples)
"""

tokenized_syntax = """select
    name,
    fc622415e32281f9f844a3e1cebcfefe table
  from
    84a852ab215534c9aded2f87d89537c1
"""


def test_token():
    tokenizer = Tokenizer(syntax)
    assert tokenizer.tokenized_syntax == tokenized_syntax


nested_syntax = """select
    name,
    cast(phone as int) table
  from
    (select * from (select * from (select * from (select * from name)) as persons) as peoples)"""

tokenized_nested_syntax = """select
    name,
    BQ00012_fc622415e32281f9f844a3e1cebcfefe table
  from
    BQ00012_bfe1a2fe29bbe7c954ea70f1e6b5fc9f"""


def test_nested_token():
    tokenizer = Tokenizer(nested_syntax, prefix="BQ00012_")
    assert tokenizer.tokenized_syntax == tokenized_nested_syntax
