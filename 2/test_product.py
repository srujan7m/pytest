from product import product_details
def test_product_details():
    expected_output = (
        "Product Name: Laptop\n"
        "Product ID: P123\n"
        "Price: 1200\n"
        "Quantity: 5"
    )
    assert product_details("Laptop", "1200", "5", "P123") == expected_output