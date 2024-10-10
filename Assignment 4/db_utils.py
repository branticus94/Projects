import mysql.connector
from mysql.connector import Error
from config import HOST, USER, PASSWORD

database_name = 'libraries_database'

def create_database_connection(database):
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PASSWORD,
            database=database
        )
        return cnx
    except Error as err:
        return f"Failed to connect to database: {err}"

def execute_query(sql_query_string, user_input=None, query_type=None):
    db_connection = None
    try:
        db_connection = create_database_connection(database_name)

        with db_connection.cursor() as cur:
            if user_input is not None and query_type in ['PUT', 'POST', 'DELETE']:
                cur.execute(sql_query_string, user_input)
                db_connection.commit()
                if query_type == 'DELETE':
                    if cur.rowcount == 0:
                        raise ValueError("No rows were deleted. The specified ID does not exist in the database.")
                elif query_type == 'PUT':
                    if cur.rowcount == 0:
                        raise ValueError("No rows were updated. The specified ID does not exist in the database.")
                elif query_type == 'POST':
                    if cur.rowcount == 0:
                        raise ValueError("No rows were inserted. Check your input data.")
            elif user_input is not None:
                cur.execute(sql_query_string, user_input)
            else:
                cur.execute(sql_query_string)

            if query_type is None or query_type == 'GET':
                results = cur.fetchall()
                return results

    except mysql.connector.Error as mysql_error:
        print(f"MySQL error occurred: {mysql_error}")
        raise mysql_error

    except Exception as e:
        print(f"Couldn't execute database query: {e}")
        raise e

    finally:
        if db_connection:
            db_connection.close()

