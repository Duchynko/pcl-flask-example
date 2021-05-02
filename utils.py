from decimal import Decimal
from beverages import Beverage, Price
from functools import reduce


def __get_price(beverage: Beverage, size: str):
    return {
        'S': beverage.prices.small,
        'M': beverage.prices.medium,
        'L': beverage.prices.large
    }.get(size, Decimal(0.0))


def get_items_from_request(form_data: dict, menu: list) -> list:
    """Returns list of tuples containing a beverage, its price and amount
    as specified in the order passed from the form in the request.

    Args: 
        form_data: data from the form passed in the POST request.
        menu: list of offered beverages.

    Returns:
        list of tuples containing the beverage, its price for specified size
        and ordered amount. The structure and types of items in the tuple are
        (Beverage, Decimal, int). For example:

        [ 
          (Beverage(...), Decimal(15.0), 2),
          (Beverage(...), Decimal(10.0), 3),
          (Beverage(...), Decimal(6.5), 1)
        ]

        Returned items will never contain an item with the amount 
        (last item in the tuple) of 0.
    """

    items = []

    for beverage in menu:
        # Don't include items with amount 0 in the final order
        if int(form_data[beverage.name]) == 0:
            continue

        size_key = f"{beverage.name}-size"
        item_size = form_data[size_key]
        item_price = __get_price(beverage, item_size)
        item_amount = form_data[beverage.name]

        items.append((beverage, item_price, item_amount))

    return items


def calculate_price(items: list) -> Decimal:
    def __add(accumulator: Decimal, item: tuple):
        price = item[1]
        amount = item[2]
        total = Decimal(price) * Decimal(amount)

        return accumulator + total

    return reduce(__add, items, Decimal(0.0))
