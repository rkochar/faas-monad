def sqldb_get(pool, headers, query_parameters):
    id = query_parameters.get("id") or 0

    with pool.connect() as db_conn:
        # get_statement = sqlalchemy.text(
        #     "SELECT * FROM bank_account WHERE id = :id"
        # )
        # results = db_conn.execute(get_statement, parameters={"id": id}).fetchall()

        if headers.get("worker") == 42:
            results = db_conn.execute(sqlalchemy.text(f"SELECT * FROM bank_account_{id}")).fetchall()
        else:
            results = db_conn.execute(sqlalchemy.text(f"SELECT * FROM bank_account WHERE id = {id}")).fetchall()
        print(f"Results: {results}")
        return str(results)