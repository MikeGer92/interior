import self as self
from django.test import TestCase
from django.test.client import Client
from mainapp.models import ProductCategory, Product
# Create your tests here.



class TestMainappSmokeTest(TestCase):
    status_code_success = 200
    def setUp(self):
        cat_1 = ProductCategory.objects.create(name='cat 1')
        Product.objects.create(category=cat_1, name='prod 1')

        self.client = Client()

    def test_mainapp_urls(self):

        # response = self.client.get('/')
        # self.assertEqual(response.status_code, self.status_code_success)

        # response = self.client.get('/contact/')
        # self.assertEqual(response.status_code, self.status_code_success)

        # response = self.client.get('/products/')
        # self.assertEqual(response.status_code, self.status_code_success)
        #
        # response = self.client.get('/products/category/0/')
        # self.assertEqual(response.status_code, self.status_code_success)

        # for category in ProductCategory.objects.all():
        #     response = self.client.get(f'/products/category/{category.pk}/')
        #     self.assertEqual(response.status_code, self.status_code_success)

        for product in Product.objects.all():
            response = self.client.get(f'/products/product/{product.pk}/')
            self.assertEqual(response.status_code, self.status_code_success)

    def tearDown(self):
        pass

