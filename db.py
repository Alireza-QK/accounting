import sqlite3
from constants import DATABASE_NAME


def connection():
    connect = sqlite3.connect(DATABASE_NAME)
    cursor = connect.cursor()
    # Create Table User
    sql_user = """
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY,
                first_name VARCHAR (70),
                last_name VARCHAR (70),
                username VARCHAR (80),
                password VARCHAR (150),
                age tinyint (120),
                email VARCHAR (254),
                phone_number VARCHAR (12)
            )
        """

    cursor.execute(sql_user)
    connect.commit()
    connect.close()


# get connection
def get_connection():
    connect = sqlite3.connect(DATABASE_NAME)

    return connect


# Define function create
def create(table_name, **kwargs):
    keys = ', '.join(kwargs.keys())
    values = ''
    command = f"INSERT INTO {table_name} ({keys}) VALUES"
    for val in kwargs.values():
        if type(val) == int:
            values += f"{val}, "
        elif type(val) == str:
            values += f"'{val}', "

    if values.endswith(', '):
        values = values.strip(', ')
    command += f" ({values})"

    connect = get_connection()
    cur = connect.cursor()
    result = cur.execute(command)
    connect.commit()
    connect.close()
    return result


# define get all
def get_all(table_name):
    connect = get_connection()
    cur = connect.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    connect.close()
    return rows


# find by id
def find_by_id(table_name, id):
    connect = get_connection()
    cur = connect.cursor()
    if type(id) == int:
        sql = "SELECT * FROM {} WHERE id={}".format(table_name, id)
        cur.execute(sql)
        row = cur.fetchone()
        connect.close()
        return row


# Update
def update(table_name, id, **kwargs):
    connect = get_connection()
    cur = connect.cursor()

    key_and_val = ''
    for key, val in kwargs.items():
        if type(val) is int:
            key_and_val += f"{key}={val}"
        elif type(val) is str:
            key_and_val += f"{key}='{val}', "
    if key_and_val.endswith(', '):
        key_and_val = key_and_val.strip(', ')

    # Query sql
    sql = f"UPDATE {table_name} SET {key_and_val} WHERE id={id}"
    result = cur.execute(sql)
    connect.commit()
    connect.close()

    return result


# Delete
def delete(table_name, id):
    connect = get_connection()
    cur = connect.cursor()

    sql = f"DELETE FROM {table_name} WHERE id={id}"
    res = cur.execute(sql)
    connect.commit()
    connect.close()

    return res


# Check is username
def check_exsist(table_name, and_or='and', **kwargs):
    connect = get_connection()
    cur = connect.cursor()
    sql = f"SELECT * FROM {table_name} WHERE "

    row = ''
    for key, value in kwargs.items():
        if type(value) == int:
            row += f"{key}={value} " + and_or
        else:
            row += f" {key}='{value}' " + and_or
    if row.endswith(' ' + and_or):
        row = row.strip(' ' + and_or)
    sql += row
    result = cur.execute(sql)
    data = result.fetchone()
    if data:
        return True
    return False
