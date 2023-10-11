from dagster import op

@op
def select_table():
    return 5