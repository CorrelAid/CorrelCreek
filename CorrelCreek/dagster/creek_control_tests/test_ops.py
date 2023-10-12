from creek_control.ops import get_data, gen_csv, upload_to_gh
from io import StringIO
from creek_control.resources import PostgresQuery, GithubClient
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def test_get_all():
    data =  list(get_data(PostgresQuery(
            db=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            pw=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            schema_name=os.getenv("POSTGRES_SCHEMA"),
        )))
    assert isinstance(data[0]._value, list)  

def test_gen_csv():
    input_list = [["Header 1", "Header 2"], ["Value 1", "Value 2"], ["Value 3", "Value 4"]]    
    csv_output = list(gen_csv(input_list))

    csv_data = csv_output[0]._value  # Get the value of the output
    assert isinstance(csv_data, StringIO)  # Ensure the output is of type io.BytesIO

    csv_string = csv_data.getvalue()

    assert csv_string == 'Header 1,Header 2\r\nValue 1,Value 2\r\nValue 3,Value 4\r\n'

def test_upload_to_gh():
    csv_data = 'Header 1,Header 2\r\nValue 1,Value 2\r\nValue 3,Value 4\r\n'
    print(os.getenv("GITHUB_ACCESS_TOKEN"))
    print(os.getenv("GITHUB_REPO_NAME"))
    result =  upload_to_gh(csv_data, GithubClient(
            access_token=os.getenv("GITHUB_ACCESS_TOKEN"),
            repo_name=os.getenv("GITHUB_REPO_NAME"),
        ))
    print(result)

    