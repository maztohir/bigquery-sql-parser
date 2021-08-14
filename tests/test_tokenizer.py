from src.bigquery_sql_parser.tokenizer import Tokenizer

text = """select
    name,
    cast(phone as int) table
  from
    (select * peoples)
"""

tokenized_text = """select
    name,
    BQ00012_fc622415e32281f9f844a3e1cebcfefe table
  from
    BQ00012_84a852ab215534c9aded2f87d89537c1
"""


def test_token():
    tokenizer = Tokenizer(text, token_prefix="BQ00012_")
    assert tokenizer.tokenized_text == tokenized_text


nested_text = """select
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

tokenized_nested_text = """select
    name,
    BQ00012_fc622415e32281f9f844a3e1cebcfefe table
  from
    BQ00012_79408cebe73fc48d4af93f6222881dcb"""


def test_nested_token():
    tokenizer = Tokenizer(nested_text, token_prefix="BQ00012_")
    assert tokenizer.tokenized_text == tokenized_nested_text


def test_translate_key():
    tokenizer = Tokenizer(nested_text, token_prefix="BQ00012_")
    assert (
        tokenizer.translate_key("BQ00012_fc622415e32281f9f844a3e1cebcfefe")
        == "cast(phone as int)"
    )


def test_translate_recursive_key():
    tokenizer = Tokenizer(nested_text, token_prefix="BQ00012_")
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


def test_reverse_text():
    tokenizer = Tokenizer(nested_text, token_prefix="BQ00012_")
    assert tokenizer._translate_text(tokenized_nested_text) == nested_text

def test_reverse_text():
    text = '''select
        name,
        """cast(phone as int)""" table''' + """
      from
        '''select * peoples'''
    """

    tokenized_text = '''select
        name,
        BQ00012_c26eb941b5449379fd59a4e13dff21d5 table
      from
        BQ00012_05bc59a975b938acd403a3bba3e6efda
    '''

    tokenizer = Tokenizer(text, token_prefix="BQ00012_", tokenize_type=Tokenizer.TOKENIZE_TRIPLE_QUOTE)
    assert tokenizer.tokenized_text == tokenized_text
