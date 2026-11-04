from Models.Book import Book
from Models.Employee import Employee
from Models.Library import Library
from Models.Order import Order

library1 = Library("Kraków", "Floriańska 10", "31-019", "08:00-18:00", "123456789")

library2 = Library("Warszawa", "Marszałkowska 25", "00-576", "09:00-17:00", "987654321")


book1 = Book(library1, "1997-06-26", "J.K.", "Rowling", 320)
book2 = Book(library1, "1949-06-08", "George", "Orwell", 328)
book3 = Book(library1, "1954-07-29", "J.R.R.", "Tolkien", 423)
book4 = Book(library2, "1813-01-28", "Jane", "Austen", 432)
book5 = Book(library2, "1869-01-01", "Lew", "Tołstoj", 1225)


employee1 = Employee(
    "Anna",
    "Kowalska",
    "2020-03-15",
    "1990-05-12",
    "Kraków",
    "Długa 5",
    "31-146",
    "111222333",
)

employee2 = Employee(
    "Piotr",
    "Nowak",
    "2018-09-01",
    "1985-11-20",
    "Kraków",
    "Karmelicka 8",
    "31-128",
    "222333444",
)

employee3 = Employee(
    "Maria",
    "Wiśniewska",
    "2022-01-10",
    "1995-02-03",
    "Warszawa",
    "Puławska 12",
    "02-566",
    "333444555",
)


student1 = "Jan Malinowski"
student2 = "Katarzyna Zielińska"
student3 = "Adam Wójcik"


order1 = Order(employee1, student1, [book1, book2], "2026-10-20")

order2 = Order(employee3, student2, [book3, book4, book5], "2026-10-21")

print(order1)
print(order2)
