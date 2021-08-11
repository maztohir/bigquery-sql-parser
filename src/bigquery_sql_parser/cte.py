from typing import List
from src.bigquery_sql_parser.query import Query

class Cte:
    def __init__(self, text:str):
        self.text = text
        
    def queries() -> List[Query]:
        pass