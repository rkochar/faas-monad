import sqlalchemy
import functions_framework
from google.cloud.sql.connector import Connector, IPTypes
from os import environ


@functions_framework.http
def template(request):
    query_string_parameters = request.args
    headers = request.headers

    instance_connection_name, dbname, username, password = environ['INSTANCE_CONNECTION_NAME'], environ[
        "DATABASE_NAME"], environ["USERNAME"], environ["PASSWORD"]

    pool = connect(instance_connection_name, username, password, dbname)

    body = ""

    return body


def connect(instance_connection, username, password, dbname):
    def getconn():
        conn = Connector().connect(
            instance_connection,
            "pymysql",
            user=username,
            password=password,
            db=dbname
        )
        return conn

    return sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn
    )