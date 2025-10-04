import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os

data = pd.read_csv("./data/student_exam_scores.csv")

def transform():
    data.previous_scores = data.previous_scores.astype(float)
    data.student_id = pd.Series(range(1, len(data) + 1), dtype=int)

def check_type():
    assert pd.api.types.is_integer_dtype(data.student_id)
    assert pd.api.types.is_float_dtype(data.hours_studied)
    assert pd.api.types.is_float_dtype(data.sleep_hours)
    assert pd.api.types.is_float_dtype(data.attendance_percent)
    assert pd.api.types.is_float_dtype(data.previous_scores)
    assert pd.api.types.is_float_dtype(data.exam_score)
    print("All types are good ✅")

def connect_db():
    username = os.getenv('DB_USR')
    password = os.getenv('DB_PWD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = "students"
    try:
        return create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")
    except SQLAlchemyError as e:
        print("SQLAlchemy error:", e)
        exit(0)
    except Exception as e:
        print("Unexpected error:", e)
        exit(0)

def load(engine):
    if not engine:
        exit(0)
    try:
        data.to_sql(
            "students",
            engine,
            if_exists="replace",
            index=False
        )
        print("Data loaded successfully ✅")
    except SQLAlchemyError as e:
        print("SQLAlchemy error:", e)
    except Exception as e:
        print("Unexpected error:", e)

def main():
    transform()
    check_type()
    e = connect_db()
    load(e)

if __name__ == "__main__":
    main()