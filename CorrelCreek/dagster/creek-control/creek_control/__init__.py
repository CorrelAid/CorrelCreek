from dagster import Definitions
from creek_control.jobs import run_elt_job
from dagster_meltano import meltano_resource

defs = Definitions(jobs=[run_elt_job], resources={
    "meltano": meltano_resource.configured({"project_dir": "../../meltano/creek-source/"}),
  },)
