import pandas as pd

from src.database import connect_database
from src.employee import Employee


class EmployeeManager:

    def __init__(self):
        self.connection = connect_database()
        self.cursor = self.connection.cursor()

    def add_employee(self, employee: Employee):

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
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            employee.first_name,
            employee.last_name,
            employee.age,
            employee.department,
            employee.position,
            employee.salary,
            employee.email,
            employee.phone,
            employee.hire_date
        )

        self.cursor.execute(query, values)
        self.connection.commit()

    def get_all_employees(self):

        query = """
        SELECT *
        FROM employees
        ORDER BY employee_id;
        """

        return pd.read_sql(query, self.connection)

    def search_employee(self, search):

        query = """
        SELECT *
        FROM employees
        WHERE
            first_name ILIKE %s
            OR last_name ILIKE %s
            OR department ILIKE %s
            OR position ILIKE %s
        ORDER BY employee_id;
        """

        value = f"%{search}%"

        return pd.read_sql(
            query,
            self.connection,
            params=(value, value, value, value)
        )

    def update_employee(
        self,
        employee_id,
        department,
        position,
        salary
    ):

        query = """
        UPDATE employees
        SET
            department=%s,
            position=%s,
            salary=%s
        WHERE employee_id=%s;
        """

        self.cursor.execute(
            query,
            (
                department,
                position,
                salary,
                employee_id
            )
        )

        self.connection.commit()

    def delete_employee(self, employee_id):

        query = """
        DELETE FROM employees
        WHERE employee_id=%s;
        """

        self.cursor.execute(query, (employee_id,))
        self.connection.commit()

    def total_employees(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM employees"
        )

        return self.cursor.fetchone()[0]

    def average_salary(self):

        self.cursor.execute(
            "SELECT AVG(salary) FROM employees"
        )

        return self.cursor.fetchone()[0]

    def highest_salary(self):

        self.cursor.execute(
            "SELECT MAX(salary) FROM employees"
        )

        return self.cursor.fetchone()[0]

    def total_departments(self):

        self.cursor.execute(
            "SELECT COUNT(DISTINCT department) FROM employees"
        )

        return self.cursor.fetchone()[0]

    def close(self):

        self.cursor.close()
        self.connection.close()