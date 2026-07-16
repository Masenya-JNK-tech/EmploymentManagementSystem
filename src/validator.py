import re
from datetime import datetime


def validate_name(name: str):

    if not name.strip():
        return False, "Name cannot be empty."

    if not name.replace(" ", "").isalpha():
        return False, "Name should contain letters only."

    return True, name.title()


def validate_age(age: str):

    try:
        age = int(age)

        if age < 18:
            return False, "Employee must be at least 18 years old."

        if age > 70:
            return False, "Age must be below 70."

        return True, age

    except ValueError:
        return False, "Age must be a whole number."


def validate_salary(salary: str):

    try:
        salary = float(salary)

        if salary < 0:
            return False, "Salary cannot be negative."

        return True, salary

    except ValueError:
        return False, "Salary must be numeric."


def validate_email(email: str):

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if re.match(pattern, email):
        return True, email

    return False, "Invalid email address."


def validate_phone(phone: str):

    phone = phone.replace(" ", "")

    pattern = r'^\d{10}$'

    if re.match(pattern, phone):
        return True, phone

    return False, "Phone number must contain exactly 10 digits."


def validate_date(date_text: str):

    try:
        hire_date = datetime.strptime(
            date_text,
            "%Y-%m-%d"
        ).date()

        return True, hire_date

    except ValueError:
        return False, "Date must be in YYYY-MM-DD format."


def validate_department(department: str):

    if not department.strip():
        return False, "Department cannot be empty."

    return True, department.title()


def validate_position(position: str):

    if not position.strip():
        return False, "Position cannot be empty."

    return True, position.title()