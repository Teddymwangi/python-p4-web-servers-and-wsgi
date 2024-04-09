# tests/test_app.py

import sys
print(sys.path)

import unittest
from server.werkzeug_app import application

class TestApp(unittest.TestCase):
    def test_application_response(self):
        # Mock request
        class MockRequest:
            remote_addr = "127.0.0.1"

        request = MockRequest()
        response = application(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'A WSGI generated this response!')

if __name__ == '__main__':
    unittest.main()
