from sqlalchemy import create_engine

# Replace the placeholder values with your own database connection details
DB_USER = 'postgres'
DB_PASSWORD = '696592'
DB_NAME = 'money_manager'
CLOUD_SQL_CONNECTION_NAME = '34.72.46.216'

db = create_engine(
    # Equivalent URL:
    # postgres+psycopg2://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername='postgres+psycopg2',
        username=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        query={
            'unix_socket': '/cloudsql/{}'.format(CLOUD_SQL_CONNECTION_NAME)
        }
    ),
    # ... Specify additional properties here.
    # ...
)