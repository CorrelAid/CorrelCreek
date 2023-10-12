from dagster import Definitions, EnvVar
from creek_control.jobs import pipeline
from dagster_meltano import meltano_resource
from creek_control.resources import PostgresQuery,GithubClient

defs = Definitions(jobs=[pipeline], resources={
    "meltano": meltano_resource.configured({"project_dir": "../meltano/"}),
    "postgres_query": PostgresQuery(
            db=EnvVar("POSTGRES_DB"),
            user=EnvVar("POSTGRES_USER"),
            pw=EnvVar("POSTGRES_PASSWORD"),
            host=EnvVar("POSTGRES_HOST"),
            port=EnvVar("POSTGRES_PORT"),
            schema_name=EnvVar("POSTGRES_SCHEMA"),
        ),
    "github_client": GithubClient(access_token=EnvVar("GITHUB_ACCESS_TOKEN"), repo_name=EnvVar("GITHUB_REPO_NAME")),
  },)
