# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: November 24th, 2023
# Description: This program defines an Employee class with private data members for the employee's name,
# ID number, salary, and email address, along with getter methods for each. It also includes a function
# make_employee_dict that takes lists of names, ID numbers, salaries, and email addresses to create a
# dictionary of Employee objects.

class Employee:
    """ 
    Represents an employee with private data members for name, ID number, salary, and email address.
    """

    def __init__(self, name, ID_number, salary, email_address):
        """
        Initializes a new Employee object with the provided name, ID number, salary, and email address.

        :param name: The name of the employee.
        :param ID_number: The ID number of the employee.
        :param salary: The salary of the employee.
        :param email_address: The email address of the employee.
        """
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """ Returns the name of the employee. """
        return self._name

    def get_ID_number(self):
        """ Returns the ID number of the employee. """
        return self._ID_number

    def get_salary(self):
        """ Returns the salary of the employee. """
        return self._salary

    def get_email_address(self):
        """ Returns the email address of the employee. """
        return self._email_address

def make_employee_dict(names, ids, salaries, emails):
    """
    Creates and returns a dictionary of Employee objects from provided lists.

    The function iterates over the lists, creating an Employee object for each set of corresponding
    values in the lists and adds them to the dictionary with the ID number as the key.

    :param names: List of names.
    :param ids: List of ID numbers.
    :param salaries: List of salaries.
    :param emails: List of email addresses.
    :return: A dictionary with ID numbers as keys and Employee objects as values.
    """
    employee_dict = {}
    for name, id, salary, email in zip(names, ids, salaries, emails):
        employee_dict[id] = Employee(name, id, salary, email)
    return employee_dict


