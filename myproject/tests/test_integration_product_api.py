import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

import unittest
from mongoengine import connect, disconnect
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from product.models.product import Product
from product.models.product_category import ProductCategory
from product.seed_data_test import seed


class ProductAPITest(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(ProductAPITest, cls).setUpClass()

        seed()
        cls.client = APIClient()

    
    @classmethod
    def tearDownClass(cls):
        Product.drop_collection()
        ProductCategory.drop_collection()
        disconnect()
        super(ProductAPITest, cls).tearDownClass()


    def test_list_products_success(self):
        url = reverse("product-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        products = data.get("results", data)
        self.assertIsInstance(products, list)
        self.assertGreaterEqual(len(products), 0)
        print("List Products (Success):", products)

if __name__=='__main__':
    unittest.main(verbosity=2)