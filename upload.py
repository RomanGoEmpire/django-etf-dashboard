import sqlite3

import pandas as pd

# Create a connection to the SQLite database file


def get_df(file, sep=";"):
    return pd.read_csv(
        f"C:/Users/gerlo/CORE/3 Programming/PycharmProjects/etf_database/data/{file}.csv",
        sep=sep,
    )


def upload_client():
    # Load your DataFrame into a pandas DataFrame
    df = get_df("client")
    df["gender"] = df["gender"].apply(lambda x: "M" if x == "male" else "F")

    # Iterate over each row in the DataFrame and insert it into the SQLite database

    cursor.execute("DELETE FROM dashboard_client")
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO dashboard_client (first_name,last_name,gender,adress,country,email,phone_number,birthday) VALUES (?,?,?,?,?,?,?,?)",
            (
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


def upload_employee():
    df = get_df("employee")
    print(df.head())


def upload_consulation():
    df = get_df("consultation")
    print(df.head())


def upload_ETF():
    df = get_df("listing_status")
    print(df.head())


def upload_timestamp():
    df = get_df("timestamps")
    print(df.head())


def upload_transaction():
    df = get_df("transaction")
    print(df.head())


def upload_cost():
    df = get_df("")
    print(df.head())


conn = sqlite3.connect("etf/db.sqlite3")
cursor = conn.cursor()
# upload_client()
upload_employee()
upload_consulation()
upload_ETF()
upload_timestamp()
upload_transaction()
upload_cost()
