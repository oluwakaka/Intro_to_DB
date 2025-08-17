# MySQLServer.py
import sys
import getpass

try:
    import mysql.connector
    from mysql.connector import Error
except Exception as e:
    print("Error: mysql-connector-python is not installed.")
    print("Install it with:  python -m pip install mysql-connector-python")
    sys.exit(1)


def main():
    host = "localhost"
    user = "root"

    # Prompt for password without echoing
    try:
        password = getpass.getpass("Enter MySQL root password: ")
    except Exception:
        # Fallback if getpass fails in some terminals
        password = input("Enter MySQL root password: ")

    conn = None
    cursor = None

    try:
        # Connect to MySQL server (no database selected yet)
        conn = mysql.connector.connect(host=host, user=user, password=password)

        # Create the database if it does not exist (no SELECT/SHOW used)
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: Could not create database. Details: {err}")

    finally:
        # Cleanly close cursor and connection
        try:
            if cursor is not None:
                cursor.close()
        except Exception:
            pass
        try:
            if conn is not None and conn.is_connected():
                conn.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()
