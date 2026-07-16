from datetime import datetime
import os

from src.employee import Employee
from src.manager import EmployeeManager
from src.reports import EmployeeReports

def menu():

    print("\n\n\n===[EMPLOYEE MANAGEMENT SYSTEM]===")
    print("What would you like to do?")
    print("""
><1>< Add an employee
><2>< Get employee list
><3>< Update employee
><4>< Delete employee
><5>< Search employee
><6>< Reports
><X>< Exit
""")


def screen_clear():
    os.system("cls")


def logic(manager,reports):

    while True:

        menu()

        choice = input("Enter option: ").upper()

        match choice:

            case "1":

                screen_clear()

                print("<1> Enter Employee Details\n")

                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                age = int(input("Enter age: "))
                department = input("Enter department: ")
                position = input("Enter position: ")
                salary = float(input("Enter salary: "))
                email = input("Enter email: ")
                phone = input("Enter phone number: ")

                hire_date = input(
                    "Enter hire date (YYYY-MM-DD): "
                )

                hire_date = datetime.strptime(
                    hire_date,
                    "%Y-%m-%d"
                ).date()

                employee = Employee(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    department=department,
                    position=position,
                    salary=salary,
                    email=email,
                    phone=phone,
                    hire_date=hire_date
                )

                manager.add_employee(employee)

                input("\nPress Enter to continue...")

            case "2":

                screen_clear()

                manager.view_employee()

                input("\nPress Enter to continue...")

            case "3":

                screen_clear()

                print("<3> Update Employee\n")

                employee_id = int(
                    input("Enter Employee ID: ")
                )

                department = input(
                    "New Department: "
                )

                position = input(
                    "New Position: "
                )

                salary = float(
                    input("New Salary: ")
                )

                manager.update_employee(
                    employee_id,
                    department,
                    position,
                    salary
                )

                input("\nPress Enter to continue...")

            case "4":

                screen_clear()

                print("<4> Delete Employee\n")

                employee_id = int(
                    input("Enter Employee ID: ")
                )

                manager.delete_employee(employee_id)

                input("\nPress Enter to continue...")

            case "5":

                screen_clear()

                print("<5> Search Employee\n")

                employee_id = int(
                    input("Enter Employee ID: ")
                )

                manager.search_employee(employee_id)

                input("\nPress Enter to continue...")

            case "X":

                screen_clear()

                print("Goodbye!")

                break

            case "6":

                screen_clear()

                reports.total_employees()

                reports.average_salary()

                reports.highest_salary()

                reports.lowest_salary()

                reports.employees_per_department()

                input("\nPress Enter to continue...")

            case _:

                print("Invalid option.")
                input("\nPress Enter to continue...")


def main():

    manager = EmployeeManager()
    reports = EmployeeReports()

    logic(manager,reports)


if __name__ == "__main__":
    main()