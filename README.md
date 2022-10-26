# Bigquery SQL Parser
Simple and out of the box Bigquery SQL Parser for python. 
Convert your SQL into python object which you can modify programatically.

![repo-size](https://img.shields.io/github/repo-size/maztohir/bigquery-sql-parser)
![license](https://img.shields.io/github/license/maztohir/bigquery-sql-parser)

## Installation
```bash
pip3 install bigquery-sql-parser
```

## Usage
Since the SQL will be converted to Python object, hence the variable name will be very important to understand. <br/> 
Please see how we use the variable and terms below.
#### Query
Below is what we call syntax of query, and `Query` is the object python name.
```sql
# path/query.sql
SELECT
    id,
    name AS customer_name,
FROM
    customer_table AS customer
```

#### Column
`id`, `customer_name` is columns and we have a `Column` python object for it.
> `id` is the `Column.value` as long as the `Column.name`, but
> `name` is `Column.value` and `customer_name` is the `Column.name`

Got the different of `value` and `name` of `Column` object? I hope so.

Python sample:
```python
from bigquery_sql_parser.query import Query

query = Query(your_query_here)
columns = query.columns
for column in query.columns
	print(column.value, column.name)

#> id, id
#> name, customer_name
```

#### Table
You can just get the table name by calling `Query` Object `Query.full_table_ids`
```python
from bigquery_sql_parser.query import Query

query = Query(your_query_here)
print(query.full_table_ids)
```

#### CTE
Well, if you use CTE like this
```sql
WITH
cte1 AS (
	xxxx
),
cte2 AS (
	xxxx
)
SELECT *
FROM cte2,cte1
```
It can't using `Query` object directly, you need to use `Script` instead
```python
from bigquery_sql_parser.script import Script
from bigquery_sql_parser.query import Query

script = Script.from_file('query_path.sql')
cte_list = script.ctes
for cte in cte_list:
	print(cte.name)
	print(cte.text)

	query = Query(cte.text)
	query... # any query variable can call here
```

#### Blocks
Since BigQuery support scripting, sometime you might want to scan query that has a lot of blocks and use Semicolon as separator.
```sql
CREATE FUNCTION x AS (());
DELETE TABLE x;
INSERT INTO x;
WITH cte1 AS (
	SELECT * FROM table
)
SELECT
    a AS b,
    c AS d
FROM table_1
```
It can't using `Query` object directly, you need to use `Script` instead
```python
from bigquery_sql_parser.script import Script
from bigquery_sql_parser.query import Query

script = Script.from_file('query_path.sql')
blocks = script.blocks
for block in blocks:
	if block.is_cte_statement and block.is_select_statement:
		print(cte.name)
		print(cte.text)
		cte_query = Query(cte.text)
		cte_query...

	final_query = Query(block.final_cte_query)
	final_query...
```

And keep counting for others to supported...
- Where/Filter statement Object
- Column Functions, Complex Column Composition
- DML Object
- Adding context from BigQuery actual table like its partition, clusters, description, etcs
- Write back from python Object to actual query

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)