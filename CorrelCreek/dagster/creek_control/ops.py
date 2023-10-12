from dagster import op, Out, Output, In, Nothing
from typing import List
from io import StringIO
import csv
from creek_control.resources import PostgresQuery, GithubClient


@op(ins={"start": In(Nothing)},out={"list": Out(list)})
def extract_postgres(postgres_query: PostgresQuery):
    yield Output(postgres_query.get_all("daily_stats"), "list")

@op(out={"csv": Out(str)})
def gen_csv(data: List[List[str]]):
    csv_data = StringIO()
    csv.writer(csv_data).writerows(data)
    csv_data = csv_data.getvalue()
    yield Output(csv_data, "csv")

@op()
def upload_to_gh(csv_data: str, github_client: GithubClient):
   return github_client.upload_content_to_repo("data.csv", csv_data)