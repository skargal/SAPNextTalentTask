import unittest
from app import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')
    def test_int(self):
        tester = app.test_client(self)
        response = tester.get('10', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'1 2 3 4 5 6 7 8 9 10' in response.data)
    def test_odd(self):
        tester = app.test_client(self)
        response = tester.get('10/odd', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'1 3 5 7 9' in response.data)
    def test_even(self):
        tester = app.test_client(self)
        response = tester.get('10/even', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'2 4 6 8' in response.data)
    def test_prime(self):
        tester = app.test_client(self)
        response = tester.get('10/prime', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'2 3 5 7' in response.data)
if __name__ == '__main__':
    unittest.main()