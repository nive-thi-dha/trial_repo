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
		
		# SQL command to create a clone of the backup database
        clone_command = f"CREATE DATABASE {target_db} CLONE {backup_db};"
		
		# SQL command to create a table named secondtable
        sql_command = f"USE SCHEMA DEMO;"
	table_command= f"CREATE TABLE SECONDTABLE(NAME VARCHAR , AGE NUMBER );"
        except Exception as e:
        print(f"Error during restore: {e}")
        sys.restore_command()
		
        # SQL command to restore the database from cloned database in case of any failure
        restore_command = f"CREATE DATABASE {target_db} CLONE {backup_db} AT (TIMESTAMP => {timestamp_command});"

        # Execute the clone command to restore the database
        cursor.execute(clone_command)
        print(f"Database {target_db} successfully restored from {backup_db}.")

    
    finally:
        cursor.close()
        ctx.close()


