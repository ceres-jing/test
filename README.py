import psycopg2
import oracledb
import pandas as pd

# PostgreSQL Database Connection Details
pg_conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="dbname",
    user="username",
    password="password"
)

# Oracle Database Connection Details
oracle_dsn = oracledb.makedsn('localhost', 1521, service_name='ORCLCDB')
oracle_conn = oracledb.connect(
    user='oracle_username',
    password='oracle_password',
    dsn=oracle_dsn
)

# Fetch Data from PostgreSQL Database
pg_cursor = pg_conn.cursor()
pg_cursor.execute("SELECT * FROM pg_table_name")
pg_data = pg_cursor.fetchall()
pg_columns = [desc[0] for desc in pg_cursor.description]
pg_df = pd.DataFrame(pg_data, columns=pg_columns)

# Insert Data into Oracle Database
oracle_cursor = oracle_conn.cursor()
for index, row in pg_df.iterrows():
    oracle_cursor.execute("INSERT INTO oracle_table_name (column1, column2, column3) VALUES (:1, :2, :3)", row.tolist())
oracle_conn.commit()

# Close Cursors and Connections
pg_cursor.close()
pg_conn.close()
oracle_cursor.close()
oracle_conn.close()

