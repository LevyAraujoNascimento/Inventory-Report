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


def test_create_product() -> None:
    test_product = Product(
        mock['id'],
        mock['product_name'],
        mock['company_name'],
        mock['manufacturing_date'],
        mock['expiration_date'],
        mock['serial_number'],
        mock['storage_instructions'],
    )

    result = {
        'id': test_product.id,
        'company_name': test_product.company_name,
        'product_name': test_product.product_name,
        'manufacturing_date': test_product.manufacturing_date,
        'expiration_date': test_product.expiration_date,
        'serial_number': test_product.serial_number,
        'storage_instructions': test_product.storage_instructions,
    }

    assert result == mock
