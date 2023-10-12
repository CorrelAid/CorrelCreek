
from dagster import job
from creek_control.ops import get_data

@job
def pipeline():
   data = get_data()
   print(data)

