import snowflake.connector
ctx = snowflake.connector.connect(
        user = "nivethidhas",
        password = "Snowflake@2025",
        account = "dj65498.central-india.azure",
        role = "ACCOUNTADMIN"
    )
	
res = ctx.cursor().execute('create database DB_backup clone DB')
