import functools

def log_activity(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

student_records = []

@log_activity
def add_student(name, age, *grades, **additional_info):
    student = {
        "name": name,
        "age": age,
        "grades": list(grades),
    }
    student.update(additional_info)
    student_records.append(student)

@log_activity
def calculate_results():
    for student in student_records:
        grades = student.get("grades", [])
        if grades:
            average = sum(grades) / len(grades)
            student["average"] = average
            student["status"] = "Pass" if average >= 50 else "Fail"
        else:
            student["average"] = None
            student["status"] = "No grades available"

@log_activity
def display_records():
    for student in student_records:
        print("-" * 30)
        for key, value in student.items():
            print(f"{key.capitalize()}: {value}")

add_student("Akshaya", 21, 75, 90, 75, major="Computer Science")
add_student("Abhigna", 21, 45, 50, 55, major="Mathematics")
add_student("Abhinaya", 22, 70, 65, major="Physics")
add_student("Sindhu", 24, major="History")

calculate_results()
display_records()
