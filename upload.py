import sqlite3

import pandas as pd

# Create a connection to the SQLite database file


def get_df(file, sep=";"):
    return pd.read_csv(
        f"data/{file}.csv",
        sep=sep,
    )


def upload_client():
    # Load your DataFrame into a pandas DataFrame
    table = "client"
    table_name = f"dashboard_{table}"
    df = get_df(table)

    df["gender"] = df["gender"].apply(lambda x: "M" if x == "male" else "F")

    cursor.execute(f"DELETE FROM {table_name}")
    for _, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name} (id,first_name,last_name,gender,adress,country,email,phone_number,birthday) VALUES (?,?,?,?,?,?,?,?,?)",
            (
                row["id"],
                row["first_name"],
                row["last_name"],
                row["gender"],
                row["adress"],
                row["country"],
                row["email"],
                row["phone_number"],
                row["birthday"],
            ),
        )
    conn.commit()
    print(f"{table} uploaded")


def upload_employee():
    table = "employee"
    table_name = f"dashboard_{table}"
    df = get_df(table)

    df["gender"] = df["gender"].apply(lambda x: "M" if x == "male" else "F")

    cursor.execute(f"DELETE FROM {table_name}")
    for _, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name}  (id,first_name,last_name,birthday,gender,email,phone_number,hire_date,role,salary) VALUES (?,?,?,?,?,?,?,?,?,?)",
            (
                row["id"],
                row["first_name"],
                row["last_name"],
                row["birthday"],
                row["gender"],
                row["email"],
                row["phone_number"],
                row["hire_date"],
                row["role"],
                row["salary"],
            ),
        )
    conn.commit()
    print(f"{table} uploaded")


def upload_consulation():
    table = "consultation"
    table_name = f"dashboard_{table}"
    df = get_df(table)

    cursor.execute(f"DELETE FROM {table_name}")
    for _, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name}  (id,employee_id,client_id,date,duration,revenue) VALUES (?,?,?,?,?,?)",
            (
                row["id"],
                row["employee_id"],
                row["client_id"],
                row["date"],
                row["duration"],
                row["revenue"],
            ),
        )
    conn.commit()
    print(f"{table} uploaded")


def upload_ETF():
    table = "etf"
    table_name = f"dashboard_{table}"
    df = get_df(table)

    cursor.execute(f"DELETE FROM {table_name}")
    for _, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name}  (id,name,exchange,ipo_date,status) VALUES (?,?,?,?,?)",
            (
                row["symbol"],
                row["name"],
                row["exchange"],
                row["ipoDate"],
                row["status"],
            ),
        )
    conn.commit()
    print(f"{table} uploaded")


def upload_timestamp():
    table = "timestamp"
    table_name = f"dashboard_{table}"
    df = get_df(table)

    cursor.execute(f"DELETE FROM {table_name}")
    for _, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name}  (etf_id,timestamp,open,high,low,close,volume) VALUES (?,?,?,?,?,?,?)",
            (
                row["symbol"],
                row["timestamp"],
                row["open"],
                row["high"],
                row["low"],
                row["close"],
                row["volume"],
            ),
        )
    conn.commit()
    print(f"{table} uploaded")


def upload_transaction():
    table = "transaction"
    table_name = f"dashboard_{table}"
    df = get_df(table)

    # if option is sell change amount to negative
    df["amount"] = df.apply(
        lambda row: row["amount"] * -1 if row["type"] == "sell" else row["amount"],
        axis=1,
    )

    cursor.execute(f"DELETE FROM {table_name}")
    for _, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name}  (client_id,etf_id,date,option,amount,frequency) VALUES (?,?,?,?,?,?)",
            (
                row["client_id"],
                row["etf_id"],
                row["date"],
                row["type"],
                row["amount"],
                row["frequency"],
            ),
        )
    conn.commit()
    print(f"{table} uploaded")


def upload_cost():
    table = "cost"
    table_name = f"dashboard_{table}"
    df = get_df(table)

    cursor.execute(f"DELETE FROM {table_name}")
    for _, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name}  (date,cost,reason,target) VALUES (?,?,?,?)",
            (
                row["date"],
                row["cost"],
                row["reason"],
                row["target"],
            ),
        )
    conn.commit()
    print(f"{table} uploaded")


conn = sqlite3.connect("etf/db.sqlite3")
cursor = conn.cursor()
upload_client()
upload_employee()
upload_consulation()
upload_ETF()
upload_timestamp()
upload_transaction()
upload_cost()


# get all transactions. If option is sell change amount to negative
# cursor.execute(
#     """
#     SELECT * FROM dashboard_transaction WHERE option = 'sell'
#     """
# )
# transactions = cursor.fetchall()
# print(transactions)
# # the amount is a interger
# for transaction in transactions:
#     cursor.execute(
#         f"""
#         UPDATE dashboard_transaction SET amount = ? WHERE id = ?
#         """,
#         (transaction[4] * -1, transaction[0]),
#     )
# conn.commit()
