# list of all relevants tests for the project

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from app.utils import *


def test_utils_scrap_html_content():
    """
    This method will just tests the html scrapping feature of example.com

    """

    selector = b64_encode("//div//h1")
    url = b64_encode("http://example.com/")
    SECRET_KEY = b64_encode("darker_san")

    response = scrap_html_content(SECRET_KEY, selector, url)

    assert (response["status"] == "success" and response["result"] == "<h1>Example Domain</h1>")


def test_utils_base64_encode():
    """
    A simple test methode for base64 encoding

    """
    assert b64_encode("test") == "dGVzdA=="


def test_utils_base64_decode():
    """
    A simple test methode for base64 decoding

    """
    assert b64_decode("dGVzdA==") == "test"
