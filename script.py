import pandas as pd

data = pd.read_csv("./data/student_exam_scores.csv")

def check_type():
    if not pd.api.types.is_object_dtype(data.student_id):
        print("student_id dtype is wrong:", data.student_id.dtype)
    if not pd.api.types.is_float_dtype(data.hours_studied):
        print("hours_studied dtype is wrong:", data.hours_studied.dtype)
    if not pd.api.types.is_float_dtype(data.sleep_hours):
        print("sleep_hours dtype is wrong:", data.sleep_hours.dtype)
    if not pd.api.types.is_float_dtype(data.attendance_percent):
        print("attendance_percent dtype is wrong:", data.attendance_percent.dtype)
    if not pd.api.types.is_integer_dtype(data.previous_scores):
        print("previous_scores dtype is wrong:", data.previous_scores.dtype)
    if not pd.api.types.is_float_dtype(data.exam_score):
        print("exam_score dtype is wrong:", data.exam_score.dtype)

    if not (pd.api.types.is_object_dtype(data.student_id) and
            pd.api.types.is_float_dtype(data.hours_studied) and
            pd.api.types.is_float_dtype(data.sleep_hours) and
            pd.api.types.is_float_dtype(data.attendance_percent) and
            pd.api.types.is_integer_dtype(data.previous_scores) and
            pd.api.types.is_float_dtype(data.exam_score)):
        print("Data types are wrong. Exiting...")
        exit(1)

check_type()

data.previous_scores = data.previous_scores.astype(float)

print("data types are good, starting script")