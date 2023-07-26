import pandas as pd
from TM1py import TM1Service

TM1_PARAMS = {
    "address": 'localhost',
    "port": 25734,
    "user": "admin",
    "password": "",
    "ssl": True,
}
# read csv
df = pd.read_csv("new_orders.csv", dtype=str)
print(df.head())

# connect
with TM1Service(**TM1_PARAMS) as tm1:
    # write
    tm1.cells.write_dataframe("Sales", df)
