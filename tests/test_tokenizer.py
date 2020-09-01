from bigquery_sql_parser.tokenizer import Tokenizer

syntax = """select
    name,
    cast(phone as int) table
  from
    (select * peoples)
"""

tokenized_syntax = """select
    name,
    BQ00012_fc622415e32281f9f844a3e1cebcfefe table
  from
    BQ00012_84a852ab215534c9aded2f87d89537c1
"""


def test_token():
    tokenizer = Tokenizer(syntax, prefix="BQ00012_")
    assert tokenizer.tokenized_syntax == tokenized_syntax


nested_syntax = """select
    name,
    cast(phone as int) table
  from
    (select * from
      (select * from
        (select * from
          (select * from name)
        ) as persons
      ) as peoples
    )"""

tokenized_nested_syntax = """select
    name,
    BQ00012_fc622415e32281f9f844a3e1cebcfefe table
  from
    BQ00012_79408cebe73fc48d4af93f6222881dcb"""


def test_nested_token():
    tokenizer = Tokenizer(nested_syntax, prefix="BQ00012_")
    assert tokenizer.tokenized_syntax == tokenized_nested_syntax


def test_translate_key():
    tokenizer = Tokenizer(nested_syntax, prefix="BQ00012_")
    assert (
        tokenizer.translate_key("BQ00012_fc622415e32281f9f844a3e1cebcfefe")
        == "cast(phone as int)"
    )


def test_translate_recursive_key():
    tokenizer = Tokenizer(nested_syntax, prefix="BQ00012_")
    assert (
        tokenizer.translate_key(
            "BQ00012_79408cebe73fc48d4af93f6222881dcb", recursive=True
        )
        == """(select * from
      (select * from
        (select * from
          (select * from name)
        ) as persons
      ) as peoples
    )"""
    )


def test_reverse_syntaxx():
    tokenizer = Tokenizer(nested_syntax, prefix="BQ00012_")
    assert tokenizer._translate_syntax(tokenized_nested_syntax) == nested_syntax
