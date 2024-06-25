import os
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

# Directory containing CSV files
data_dir = "path/to/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports"

# Ingesting data
for file in os.listdir(data_dir):
    if file.endswith('.csv'):
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)
        df.to_sql('daily_reports', con=engine, if_exists='append', index=False)
