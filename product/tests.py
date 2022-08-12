from django.test import TestCase

class TestProduct(TestCase):
    def test_product_list(self):
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
            
    def sub_product(self):
        response = self.client.post('/product/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

