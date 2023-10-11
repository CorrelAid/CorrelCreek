from dagster import Definitions, EnvVar
from creek_control.jobs import run_elt_job
from dagster_meltano import meltano_resource
from creek_control.resources import PostgresQuery

defs = Definitions(jobs=[run_elt_job], resources={
    "meltano": meltano_resource.configured({"project_dir": "../meltano/"}),
    "postgres_query": PostgresQuery(
            db=EnvVar("POSTGRES_DB"),
            user=EnvVar("POSTGRES_USER"),
            pw=EnvVar("POSTGRES_PASSWORD"),
            host=EnvVar("POSTGRES_HOST"),
            port=EnvVar("POSTGRES_PORT"),
        ),
  },)
