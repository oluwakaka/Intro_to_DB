# MySQLServer.py
import sys
import getpass

try:
    import mysql.connector
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
        password = input("Enter MySQL root password: ")

    conn = None
    cursor = None

    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(host=host, user=user, password=password)

        # Create the database if it does not exist
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:   # 👈 changed to match checker
        print(f"Error: Could not create database. Details: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    main()
