import pytest
def product_details(name, price, quantity,product_id):
    result = (
        f"Product Name: {name}\n"
        f"Product ID: {product_id}\n"
        f"Price: {price}\n"
        f"Quantity: {quantity}"
    )
    return result
if __name__ == "__main__":
    name = "Laptop"
    product_id = "P123"
    price = "1200"
    quantity = "5"
    print(product_details(name, price, quantity, product_id))