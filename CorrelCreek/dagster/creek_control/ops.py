from dagster import op, Out, Output, In
from dagster_meltano import meltano_run_op
from typing import List
from io import StringIO
import csv
from creek_control.resources import PostgresQuery, GithubClient

@op()
def tap_github():
    tap_done = meltano_run_op("tap-github target-postgres")

@op()
def transform():
    tap_done = meltano_run_op("dbt-postgres:run")


@op(out={"list": Out(list)})
def get_data(postgres_query: PostgresQuery):
    yield Output(postgres_query.get_all("daily_stats"), "list")

@op(out={"csv": Out(StringIO)})
def gen_csv(data: List[List[str]]):
    csv_data = StringIO()
    csv.writer(csv_data).writerows(data)
    yield Output(csv_data, "csv")

@op()
def upload_to_gh(csv_data: str, github_client: GithubClient):
   return github_client.upload_content_to_repo("data.csv", csv_data)