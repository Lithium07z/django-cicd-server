from django.test import TestCase
from rest_framework.test import APIClient


class Test(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_funtion(self):
        x = self.client.get('/')
        self.assertEqual(x.status_code, 200)
        print("완료")

    def test_abort(self):
        a = 1
        b = 2
        assert (a == b)

    # def test_success(self):
    #     a = 1
    #     b = 1
    #     assert (a == b)
