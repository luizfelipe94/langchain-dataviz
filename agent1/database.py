from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///database.db")
# print(db.dialect)
# print(db.get_usable_table_names())
# db.run("SELECT * FROM vendas LIMIT 10;")