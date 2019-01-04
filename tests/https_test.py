import pytest
from billy.utils.https import convert_to_https


class TestConvertToHttps(object):
    def test_http_url(self):
        assert convert_to_https(
            "http://www.google.com") == "https://www.google.com"

    def test_https_url(self):
        assert convert_to_https(
            "https://www.amazon.com") == "https://www.amazon.com"

    def test_faulty_url(self):
        assert convert_to_https(
            "http://www.broken.http://") == "https://www.broken.http://"

    def test_no_http(self):
        assert convert_to_https("www.cnet.com") == "www.cnet.com"
