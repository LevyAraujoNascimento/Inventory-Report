from inventory_report.product import Product


# MOCK
mock = {
        'id': 'mock_id',
        'company_name': 'mock_company_name',
        'product_name': 'mock_product_name',
        'manufacturing_date': 'mock_manufacturing_date',
        'expiration_date': 'mock_expiration_date',
        'serial_number': 'mock_serial_number',
        'storage_instructions': 'mock_storage_instructions',
    }


def test_product_report() -> None:
    test_product = Product(
        mock['id'],
        mock['product_name'],
        mock['company_name'],
        mock['manufacturing_date'],
        mock['expiration_date'],
        mock['serial_number'],
        mock['storage_instructions'],
    )

    result = (
        f"The product {mock['id']} - {mock['product_name']} "
        f"with serial number {mock['serial_number']} "
        f"manufactured on {mock['manufacturing_date']} "
        f"by the company {mock['company_name']} "
        f"valid until {mock['expiration_date']} "
        "must be stored according to the following instructions: "
        f"{mock['storage_instructions']}."
    )

    assert test_product.__str__() == result
