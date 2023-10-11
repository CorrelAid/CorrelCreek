from dagster_meltano import meltano_run_op
from dagster import job

@job()
def run_elt_job():
   tap_done = meltano_run_op("tap-github target-postgres dbt-postgres:run")()