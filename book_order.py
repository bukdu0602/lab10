# Ryan Lim , lab partner Larissa Chan

import sys
import book_order_utils


def main():
    """
    :return: calls functions from the imported book_order_utils script in order to accomplish the following:
    1. validate book order details
    2. calculate the unit cost for the ordered book
    3. write the book order details to the specified text file
    """
    try:
        order_num = sys.argv[1]
        title = sys.argv[2]
        author = sys.argv[3]
        isbn = sys.argv[4]
        year = sys.argv[5]
        quantity = sys.argv[6]
        cost = sys.argv[7]
        book_order_utils.validate_book_order_details(order_num, title, author, isbn, year, quantity, cost)
        book_order_utils.calculate_per_book_cost(float(cost), int(quantity))
        unit_cost = book_order_utils.calculate_per_book_cost(float(cost), int(quantity))
        filename = order_num + ".txt"
        book_order_utils.write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost)
    except ValueError as e:
        print("Value Error: ", end="")
        print(e)
    except TypeError as e:
        print("Type Error: ", end="")
        print(e)
    except ZeroDivisionError:
        print("No Books in Order")


if __name__ == '__main__':
    main()
