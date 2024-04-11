cursor.executemany(f"INSERT INTO {table_name} ({','.join(df.columns)}) VALUES ({','.join([':' + str(i + 1) for i in range(len(df.columns))])})", df.values.tolist())
connection.commit()
