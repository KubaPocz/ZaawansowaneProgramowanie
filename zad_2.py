class Library:
    def __init__(self, city, street, zip_code,open_hours:str,phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self):
        return f"Library located in {self.city}, {self.street}, {self.zip_code}. Open hours: {self.open_hours}. Contact: {self.phone}"
class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, Hired on: {self.hire_date}, Born on: {self.birth_date}, Address: {self.city}, {self.street}, {self.zip_code}, Phone: {self.phone}"
class Book:
    def __init__(self,library:Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}, Published on: {self.publication_date}, Pages: {self.number_of_pages}, Library: {self.library.city}, {self.library.street}, {self.library.zip_code}"
class Order:
    def __init__(self, employee:Employee,student, books:list[Book], order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self):
        return f"Order: {self.student}, Employee: {self.employee.first_name} {self.employee.last_name}, Date: {self.order_date}, Books: {', '.join(str(book) for book in self.books)}"

library1 = Library(
    "Kraków", "Floriańska 10", "31-019",
    "08:00-18:00", "123456789"
)

library2 = Library(
    "Warszawa", "Marszałkowska 25", "00-576",
    "09:00-17:00", "987654321"
)


book1 = Book(library1, "1997-06-26", "J.K.", "Rowling", 320)
book2 = Book(library1, "1949-06-08", "George", "Orwell", 328)
book3 = Book(library1, "1954-07-29", "J.R.R.", "Tolkien", 423)
book4 = Book(library2, "1813-01-28", "Jane", "Austen", 432)
book5 = Book(library2, "1869-01-01", "Lew", "Tołstoj", 1225)


employee1 = Employee(
    "Anna", "Kowalska", "2020-03-15", "1990-05-12",
    "Kraków", "Długa 5", "31-146", "111222333"
)

employee2 = Employee(
    "Piotr", "Nowak", "2018-09-01", "1985-11-20",
    "Kraków", "Karmelicka 8", "31-128", "222333444"
)

employee3 = Employee(
    "Maria", "Wiśniewska", "2022-01-10", "1995-02-03",
    "Warszawa", "Puławska 12", "02-566", "333444555"
)


student1 = "Jan Malinowski"
student2 = "Katarzyna Zielińska"
student3 = "Adam Wójcik"


order1 = Order(
    employee1,
    student1,
    [book1, book2],
    "2026-10-20"
)

order2 = Order(
    employee3,
    student2,
    [book3, book4, book5],
    "2026-10-21"
)

print(order1)
print(order2)