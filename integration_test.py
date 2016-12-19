import unittest  # HACK: Although this isn't a unit test, this works.
import urllib2

BASE_URL = 'http://127.0.0.1:5000/' or 'http://jessan.pythonanywhere.com/'

class TicTacToeIntegrationTest(unittest.TestCase):
    """Verifies the live server, comparing actual to expected response."""

    def testBasic(self):
        self.assertResponse('board=+xoxx+o+o', 'oxoxx o o')

    def testBoardNotSet(self):
        self.assertHttpError('')

    def assertResponse(self, request_data, expected_response):
        response = urllib2.urlopen(BASE_URL + '?' + request_data).read()
        self.assertEquals(expected_response, response)

    def assertHttpError(self, request_data, error_code=400):
        with self.assertRaises(urllib2.HTTPError) as http_error:
            urllib2.urlopen(BASE_URL + '?' + request_data).read()
        self.assertEquals(error_code, http_error.exception.code)

if __name__ == "__main__":
     unittest.main(exit=False)
