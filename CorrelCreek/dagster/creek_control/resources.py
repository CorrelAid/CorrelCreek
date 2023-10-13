from dagster import ConfigurableResource, List
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy import select, text
from sqlalchemy.engine import Connectable
from pydantic import PrivateAttr
from github import Github, Auth


class PostgresQuery(ConfigurableResource):
    db: str
    user: str
    pw: str
    port: str
    host: str
    schema_name: str
    _db_connection: Connectable = PrivateAttr()

    @contextmanager
    def yield_for_execution(self, context):
        engine = create_engine(f"postgresql://{self.user}:{self.pw}@{self.host}:{self.port}/{self.db}")
        with engine.connect() as conn:
            # set up the connection attribute so it can be used in the execution
            self._db_connection = conn

            # yield, allowing execution to occur
            yield self

    def get_all(self, table: str) -> List[List[str]]:
        query = select("*").select_from(text("analytics.daily_stats"))
        with self.yield_for_execution(context=None) as pg_query:
            rows = pg_query._db_connection.execute(query)
            data = [[str(value) for value in row] for row in rows]
        return data


class GithubClient(ConfigurableResource):
    access_token: str
    repo_name: str

    def upload_content_to_repo(self, file_name, content):
        auth = Auth.Token(self.access_token)
        github = Github(auth=auth)
        repo = github.get_repo(self.repo_name)
        try:
            # Try to get the contents of the file
            file_contents = repo.get_contents(file_name)

            # If the file exists, update it
            repo.update_file(
                file_contents.path,
                "Update file",
                content,
                file_contents.sha,
                branch="main",
            )
        except github.UnknownObjectException:
            # If the file doesn't exist, create it
            repo.create_file(file_name, "Create file", content, branch="main")
