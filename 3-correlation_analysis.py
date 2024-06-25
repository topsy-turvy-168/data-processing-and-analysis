import pandas as pd
from sqlalchemy import create_engine

# Database configuration
DB_TYPE = 'postgresql'
DB_DRIVER = 'psycopg2'
DB_USER = 'your_user'
DB_PASS = 'your_password'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'covid19'

DATABASE_URI = f"{DB_TYPE}+{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URI)

df = pd.read_sql("SELECT confirmed, deaths FROM cleaned_data", con=engine)
correlation = df.corr()