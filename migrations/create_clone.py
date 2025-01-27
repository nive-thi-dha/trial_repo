import snowflake.connector
import sys

def restore_snowflake_db(backup_db, target_db, user, password, account, warehouse, database, schema):
    """
    Restores a Snowflake database from a cloned database (backup).

    :param backup_db: The name of the backup database (DB_BACKUP)
    :param target_db: The name of the target database (DB) to restore to
    :param user: Snowflake user
    :param password: Snowflake password
    :param account: Snowflake account identifier
    :param warehouse: The name of the Snowflake warehouse
    :param database: The name of the Snowflake database to work with
    :param schema: The schema to work within
    """
    try:
        # Establish Snowflake connection
        ctx = snowflake.connector.connect(
            user="nivethidhas",
            password="Snowflake@2025",
            account="dj65498.central-india.azure",
            warehouse="COMPUTE_WH",
            database="DB",
            schema="SCH"
        )

        # Create a cursor object to execute SQL commands
        cursor = ctx.cursor()
		
		# SQL command to note down the timestamp
        timestamp_command = f"select current_timestamp();"
		cursor.execute(timestamp_command)
		
		# SQL command to create a clone of the database
        clone_command = f"CREATE DATABASE DB_BKP CLONE DB;"
		cursor.execute(clone_command)
		
		# SQL command to test
        sql_command = f"CREATE DATABASE DB_TEST CLONE DB;"
		cursor.execute(sql_command)
		
		# SQL command to restore the database from cloned database in case of any failure
		drop_command= f"DROP DATABASE DB;"
        restore_command = f"CREATE DATABASE DB CLONE DB_BKP AT (TIMESTAMP => {timestamp_command});"
		
        except Exception as e:
        print(f"Error during restore: {e}")
        sys.drop_command()
		sys.restore_command()
		       
        
        print(f"Database DB successfully restored from DB_BKP.")

    
    finally:
        cursor.close()
        ctx.close()

# Example usage
backup_db = "DB_BACKUP"  # Name of the backup database
target_db = "DB"  # Name of the target database to restore
user = "your_username"
password = "your_password"
account = "your_account.snowflakecomputing.com"  # Snowflake account
warehouse = "your_warehouse"  # Snowflake warehouse
database = "your_database"  # The current database
schema = "public"  # Your schema, usually "public"

restore_snowflake_db(backup_db, target_db, user, password, account, warehouse, database, schema)
