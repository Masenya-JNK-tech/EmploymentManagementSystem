import streamlit as st
import pandas as pd
from datetime import datetime

from src.database import connect_database

st.set_page_config(
    page_title="Employee Management System",
    page_icon="👨‍💼",
    layout="wide"
)


# -------------------------
# DATABASE FUNCTIONS
# -------------------------

def load_data():

    connection = connect_database()

    query = """
    SELECT *
    FROM employees
    ORDER BY employee_id;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


def add_employee(first_name, last_name, age, department,
                 position, salary, email, phone, hire_date):

    connection = connect_database()
    cursor = connection.cursor()

    query = """
    INSERT INTO employees
    (
        first_name,
        last_name,
        age,
        department,
        position,
        salary,
        email,
        phone,
        hire_date
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            first_name,
            last_name,
            age,
            department,
            position,
            salary,
            email,
            phone,
            hire_date
        )
    )

    connection.commit()
    cursor.close()
    connection.close()


def update_employee(emp_id, department, position, salary):

    connection = connect_database()
    cursor = connection.cursor()

    query = """
    UPDATE employees
    SET
        department=%s,
        position=%s,
        salary=%s
    WHERE employee_id=%s
    """

    cursor.execute(
        query,
        (
            department,
            position,
            salary,
            emp_id
        )
    )

    connection.commit()

    cursor.close()
    connection.close()


def delete_employee(emp_id):

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE employee_id=%s",
        (emp_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()


# -------------------------
# LOAD DATA
# -------------------------

employees = load_data()


# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("Employee Management")

page = st.sidebar.radio(

    "Navigation",

    [

        "Dashboard",

        "Employees",

        "Add Employee",

        "Update Employee",

        "Delete Employee"

    ]

)


# -------------------------
# DASHBOARD
# -------------------------

if page == "Dashboard":

    st.title("👨‍💼 Employee Management Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Employees",
        len(employees)
    )

    col2.metric(
        "Departments",
        employees["department"].nunique()
    )

    col3.metric(
        "Average Salary",
        f"R{employees['salary'].mean():,.2f}"
    )

    col4.metric(
        "Highest Salary",
        f"R{employees['salary'].max():,.2f}"
    )

    st.divider()

    st.subheader("Employee Database")

    st.dataframe(
        employees,
        use_container_width=True
    )


# -------------------------
# VIEW EMPLOYEES
# -------------------------

elif page == "Employees":

    st.title("Employees")

    search = st.text_input("Search employee")

    if search:

        employees = employees[
            employees["first_name"].str.contains(search, case=False)
            |
            employees["last_name"].str.contains(search, case=False)
            |
            employees["department"].str.contains(search, case=False)
        ]

    st.dataframe(
        employees,
        use_container_width=True
    )


# -------------------------
# ADD EMPLOYEE
# -------------------------

elif page == "Add Employee":

    st.title("Add Employee")

    with st.form("employee_form"):

        first = st.text_input("First Name")

        last = st.text_input("Last Name")

        age = st.number_input(
            "Age",
            18,
            70
        )

        department = st.text_input("Department")

        position = st.text_input("Position")

        salary = st.number_input(
            "Salary",
            min_value=0.0
        )

        email = st.text_input("Email")

        phone = st.text_input("Phone")

        hire_date = st.date_input("Hire Date")

        submitted = st.form_submit_button(
            "Add Employee"
        )

        if submitted:

            add_employee(
                first,
                last,
                age,
                department,
                position,
                salary,
                email,
                phone,
                hire_date
            )

            st.success("Employee added successfully!")

            st.rerun()


# -------------------------
# UPDATE
# -------------------------

elif page == "Update Employee":

    st.title("Update Employee")

    emp_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1
    )

    department = st.text_input(
        "New Department"
    )

    position = st.text_input(
        "New Position"
    )

    salary = st.number_input(
        "New Salary",
        min_value=0.0
    )

    if st.button("Update"):

        update_employee(
            emp_id,
            department,
            position,
            salary
        )

        st.success("Employee updated!")

        st.rerun()


# -------------------------
# DELETE
# -------------------------

elif page == "Delete Employee":

    st.title("Delete Employee")

    emp_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1
    )

    if st.button("Delete"):

        delete_employee(emp_id)

        st.success("Employee deleted!")

        st.rerun()