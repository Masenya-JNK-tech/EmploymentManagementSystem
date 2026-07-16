
from src.database import connect_database


class EmployeeReports:

    def __init__(self):
        self.connection = connect_database()
        self.cursor = self.connection.cursor()

    def total_employees(self):

        query = "SELECT COUNT(*) FROM employees;"

        self.cursor.execute(query)

        total = self.cursor.fetchone()[0]

        print(f"\nTotal Employees : {total}")

    def average_salary(self):

        query = "SELECT AVG(salary) FROM employees;"

        self.cursor.execute(query)

        average = self.cursor.fetchone()[0]

        if average is None:
            average = 0

        print(f"\nAverage Salary : R{average:.2f}")

    def highest_salary(self):

        query = """
        SELECT first_name,
               last_name,
               salary
        FROM employees
        ORDER BY salary DESC
        LIMIT 1;
        """

        self.cursor.execute(query)

        employee = self.cursor.fetchone()

        if employee:

            print("\nHighest Paid Employee")
            print("----------------------")
            print(f"Name   : {employee[0]} {employee[1]}")
            print(f"Salary : R{employee[2]}")

    def lowest_salary(self):

        query = """
        SELECT first_name,
               last_name,
               salary
        FROM employees
        ORDER BY salary ASC
        LIMIT 1;
        """

        self.cursor.execute(query)

        employee = self.cursor.fetchone()

        if employee:

            print("\nLowest Paid Employee")
            print("---------------------")
            print(f"Name   : {employee[0]} {employee[1]}")
            print(f"Salary : R{employee[2]}")

    def employees_per_department(self):

        query = """
        SELECT department,
               COUNT(*)
        FROM employees
        GROUP BY department
        ORDER BY department;
        """

        self.cursor.execute(query)

        departments = self.cursor.fetchall()

        print("\nEmployees Per Department")
        print("-------------------------")

        for department, count in departments:
            print(f"{department} : {count}")