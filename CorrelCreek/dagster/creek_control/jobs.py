from dagster import job
from dagster_meltano import meltano_run_op
from creek_control.ops import extract_postgres, gen_csv, upload_to_gh


@job
def pipeline():
    tap_gh_done = meltano_run_op("tap-github target-postgres")()
    transform_done = meltano_run_op("dbt-postgres:run")(after=tap_gh_done)
    upload_to_gh(gen_csv(extract_postgres(transform_done)))
