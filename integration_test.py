import unittest  # HACK: Although this isn't a unit test, this works.
import urllib2

BASE_URL = 'http://jessan.pythonanywhere.com/'

class TicTacToeIntegrationTest(unittest.TestCase):
    """docstring for TicTacToeIntegrationTest."""

    def testBasic(self):
        self.assertResponse('board=', '         ')

    def testBoardNotset(self):
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
