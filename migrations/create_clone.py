import snowflake.connector
ctx = snowflake.connector.connect(
        user = "pradeep",
        password = "Training@123",
        account = "io63122.central-india.azure",
        role = "ACCOUNTADMIN"
    )
	
res = ctx.cursor().execute('create database TRAINING_NEW_backup clone TRAINING_NEW')
