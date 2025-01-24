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
    workflow_config=$(echo sed -e 's/#.*$//' -e '/^$/d' workflow.conf)
    while IFS= read -r sql_file_name; do
        print_log "INFO" "Running: $sql_file_name"
        print_log "INFO" "Running ~/snowflake/snowsql --connections-file $GITHUB_WORKSPACE/migrations/workflow.config --connection-name cicd
    done < <($workflow_config);
}

## running workflow
run_workflow

