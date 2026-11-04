from Models import Employee
from Models import Book
class Order:
    def __init__(self, employee: Employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Order: {self.student}, Employee: {self.employee.first_name} {self.employee.last_name}, Date: {self.order_date}, Books: {', '.join(str(book) for book in self.books)}"