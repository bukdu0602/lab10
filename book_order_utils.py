# Ryan Lim , lab partner Larissa Chan

import re
import os


def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    """
    :param order_num: the order number for a specific book order (a unique order number is assigned to each order).
    :param title: the title of the ordered book.
    :param author: the author of the ordered book.
    :param isbn: the isbn of the ordered book.
    :param year: the year the book was published.
    :param quantity: the quantity in the book order.
    :param cost: the total cost for the order.
    :return: the function raises errors if any of the book order details passed through the function are invalid.
    """
    if not re.search('^[0-9]+$', order_num):   # One or more integer values. Note that both 1 and 0001 would be valid.
        raise ValueError("Order Number is invalid")
    if not re.search('^[a-zA-Z ]+$', title):  # One or more lower or upper case letters or spaces.
        raise ValueError("Title is invalid")
    if not re.search('^[a-zA-Z \']*$', author):  # Zero or more lower or upper case letters, spaces or apostrophes.
        raise ValueError("Author is invalid")
    if not re.search('^[0-9]+$', isbn):  # Must be integers.
        raise TypeError("ISBN must be an integer")
    if not re.search(r'^\d{4,20}$', isbn):  # Must be between 4 and 20 digits, inclusive
        raise ValueError("ISBN is invalid")
    if not re.search('^[0-9]+$', year):  # Must be integers.
        raise TypeError("Year must be an integer")
    if not re.search(r'^\d{4}$', year):  # Must be 4 digits exactly.
        raise ValueError("Year is invalid")
    if not re.search(r'^\d+$', quantity):  # Must be integers.
        raise TypeError("Quantity must be an integer")
    if not re.search('^[0]?[0-9]?[0-9]?[0-9]$|^[1][0][0][0]$', quantity):  # Must be between 0 and 1000, inclusive.
        raise ValueError("Quantity is invalid")
    if not re.search(r'^\d+[.]\d{2}$', cost):  # Mus tbe a floating point value with exactly 2 decimal places.
        raise ValueError("Cost is invalid")


def calculate_per_book_cost(cost, quantity):
    """
    :param cost: the cost of the entire book order (string format with digits and 2 digits after the period).
    :param quantity: quantity of books ordered (string variable which can be converted to an integer).
    :return: returns the per unit book cost by dividing the total cost by the quantity of books ordered.
    """
    per_book = cost / quantity
    return float(per_book)


def write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost):
    """
    :param filename: the filename of the book order.
    :param title: the book title in the book order.
    :param author: the author of the ordered book.
    :param isbn: the isbn of the ordered book.
    :param year: the publishing year of the ordered book.
    :param quantity: the quantity ordered.
    :param cost: the total cost of the books ordered.
    :param unit_cost: the unit cost of the books ordered.
    :return: creates a text file and writes the book order details to the file. Error if the file already exists.
    """
    if os.path.exists(filename):  # check if the file name already exist.
        raise ValueError("Order file name already exists!")
    f = open(filename, "w")
    f.write(f"title={title}\nauthor={author}\nisbn={isbn}\nyear={year}\nquantity={quantity}\ncost={cost}\n"
            f"unit_cost={unit_cost}")
    f.close()


if __name__ == '__main__':
    write_book_order_details("file", "Intro to Python", "Bill Smith", "123456", "2010", "10", "$500", "50.05")
