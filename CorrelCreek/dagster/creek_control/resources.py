from dagster import ConfigurableResource, List
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.engine import Connectable
from pydantic import PrivateAttr

class PostgresQuery(ConfigurableResource):
    db: str
    user: str
    pw: str
    port: str
    host: str
    _db_connection: Connectable = PrivateAttr()

    @contextmanager
    def yield_for_execution(self, context):
        engine = create_engine(f"postgresql://{self.user}:{self.pw}@{self.host}:{self.port}/{self.db}")
        with engine.connect() as conn:
            # set up the connection attribute so it can be used in the execution
            self._db_connection = conn

            # yield, allowing execution to occur
            yield self

    def single(self, query: str) -> List[str]:
        rows = self._db_connection.execute(query)
        data = [row[0] for row in rows]
        return data[0]

    def execute(self, query: str) -> None:
        self._db_connection.execute(query)