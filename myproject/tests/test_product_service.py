import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

import unittest
from unittest.mock import MagicMock, patch
from product.services.product import ProductService

# Your test class and methods follow
class TestProductService(unittest.TestCase):
    @patch("product.services.product.ProductRepository", autospec=True)
    def setUp(self, mock_repo_class):
        self.mock_repo = MagicMock()
        mock_repo_class.return_value = self.mock_repo
        self.product_service = ProductService()

    def test_create_product_success(self):
        data = {'name': 'Test product', 'price': 12}
        mock_product = MagicMock()
        self.mock_repo.create_product.return_value = mock_product
        product = self.product_service.create_product(data)
        self.mock_repo.create_product.assert_called_once_with(data)
        self.assertEqual(product, mock_product)

if __name__ == '__main__':
    unittest.main(verbosity=2)
