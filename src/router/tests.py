from django.test import TestCase
from django.test.client import Client

class Routing(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_correct_redirects(self):
        "test valid parameters issue a 302 - temporary redirect response"
        passes = [
            ('a', '1'),
            
            ('ab', '1'),
            ('abc', '1'),
            ('zyx', '1'),
            
            ('a', '12'),
            ('a', '123'),
            ('a', '1234'),
            ('a', '12345'),
        ]
        for args in passes:
            try:
                url = '/v1/%s/%s/' % args
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302) # if you prefer
            except Exception:
                print('failed on',url)
                raise
            
    def test_incorrect_redirects(self):
        "test invalid params issue a 404 - not found response"
        fails = [
            # too many chars
            ('abcd', '1'),
            ('zyxw', '1'),

            # too many digits
            ('a', '123456'),
            ('a', '999999'),

            # too many chars and digits
            ('abcd', '123456'),

            # digits instead of chars
            ('1', '1'),

            # chars instead of digits
            ('a', 'a'),

            # digits instead of chars, chars instead of digits
            ('1', 'a')
        ]
        for args in fails:
            try:
                url = '/v1/%s/%s/' % args
                response = self.client.get(url)
                self.assertEqual(response.status_code, 404)
            except Exception:
                print('failed on',url)
                raise
