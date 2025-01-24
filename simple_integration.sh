# simple_integration.sh script that reads workflow.conf file and execute it.
#!/bin/bash
# author: Marcel Castro
set -e
print_log () {
    printf "[`date +'%d/%m/%Y %H:%M:%S'`] [$1] $2\n"
}
export -f print_log

run_workflow () {
    print_log "INFO" "Running workflow"
        print_log "INFO" "Running: workflow"
        ~/snowflake/snowsql -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE --private-key-path $SNOWFLAKE_PRIVATE_KEY -q "create database DB_BKP clone DB"
}

## running workflow
## run_workflow
 echo "TEST"
~/snowflake/snowsql -a $SF_ACCOUNT -u $SF_USERNAME -r $SF_ROLE -w $SF_WAREHOUSE -d $SF_DATABASE --private-key-path $SNOWFLAKE_PRIVATE_KEY -q "create database DB_BKP clone DB"
