import pandas as pd, sqlite3
from langchain_community.utilities import SQLDatabase

if __name__ == "__main__":
    con = sqlite3.connect("database.db")
    df = pd.read_csv("./agent1/datasets/file.csv")
    df.to_sql("vendas", con=con, if_exists="replace", index=False)
    db = SQLDatabase.from_uri("sqlite:///database.db")
    # print(db.run("SELECT * FROM vendas"))