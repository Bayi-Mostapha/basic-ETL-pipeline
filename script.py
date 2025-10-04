import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

data = pd.read_csv("./data/student_exam_scores.csv")

data.previous_scores = data.previous_scores.astype(float)
data.student_id = pd.Series(range(1, len(data) + 1), dtype=int)

def check_type(df):
    assert pd.api.types.is_integer_dtype(df.student_id)
    assert pd.api.types.is_float_dtype(df.hours_studied)
    assert pd.api.types.is_float_dtype(df.sleep_hours)
    assert pd.api.types.is_float_dtype(df.attendance_percent)
    assert pd.api.types.is_float_dtype(df.previous_scores)
    assert pd.api.types.is_float_dtype(df.exam_score)
    print("All types are good ✅")

check_type(data)

username = "admin"
password = "admin"
host = "db"
port = 5432
database = "students"

try:
    # Create the engine
    engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
    
    # Push DataFrame to PostgreSQL
    data.to_sql(
        "students",
        engine,
        if_exists="replace",
        index=False
    )
    
    print("Data loaded successfully ✅")

except SQLAlchemyError as e:
    # Catch SQLAlchemy-specific errors
    print("SQLAlchemy error:", e)

except Exception as e:
    # Catch other general errors
    print("Unexpected error:", e)