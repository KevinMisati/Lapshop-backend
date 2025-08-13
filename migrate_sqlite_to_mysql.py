import sqlite3
import mysql.connector
from decouple import config

# ==== CONFIG ====
SQLITE_DB = "db.sqlite3"  

MYSQL_HOST = config('DB_HOST', default='localhost')
MYSQL_USER = config('DB_USER')
MYSQL_PASSWORD = config('DB_PASSWORD')
MYSQL_DB = config('DB_NAME')
# ===============

# Connect to SQLite
sqlite_conn = sqlite3.connect(SQLITE_DB)
sqlite_cursor = sqlite_conn.cursor()

# Connect to MySQL
mysql_conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)
mysql_cursor = mysql_conn.cursor()

# Get all SQLite tables
sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = sqlite_cursor.fetchall()

for table_name in tables:
    table = table_name[0]
    print(f"Copying table: {table}")

    # Get all data
    sqlite_cursor.execute(f"SELECT * FROM {table}")
    rows = sqlite_cursor.fetchall()

    if not rows:
        continue

    # Get column names
    col_names = [desc[0] for desc in sqlite_cursor.description]
    placeholders = ", ".join(["%s"] * len(col_names))
    col_list = ", ".join(col_names)

    # Insert into MySQL
    for row in rows:
        try:
            mysql_cursor.execute(f"INSERT INTO {table} ({col_list}) VALUES ({placeholders})", row)
        except Exception as e:
            print(f"Error inserting row in {table}: {e}")

mysql_conn.commit()
mysql_conn.close()
sqlite_conn.close()

print("✅ Migration complete!")
