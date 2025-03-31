from domain.Client import Client
from domain.ValidatorCarte import ValidatorCarte
from domain.ValidatorClient import ValidatorClient
import unittest

class TestClient(unittest.TestCase):
    def test_create_client(self):
        client = Client(1, "Ana Pop", 1111111111111)
        assert client.id == 1
        assert client.nume == "Ana Pop"
        assert client.CNP == 1111111111111

    def test_equals_client(self):
        client1 = Client(1, "Ana Pop", 1111111111111)
        client2 = Client(1, "Maria Pop", 1111111111111)
        assert client1 == client2

        client3 = Client(2, "Ana Pop", 1111111111111)
        assert client1 != client3

    def test_validare_client(self):
        validator = ValidatorClient()

        client_valid = Client(1, "Ana Pop", 1111111111111)
        try:
            validator.validate(client_valid)
            assert True
        except ValueError:
            assert False

        client_invalid = Client(1, "Ana Pop", 123456789)
        try:
            validator.validate(client_invalid)
            assert False
        except ValueError:
            assert True

        client_invalid = Client('a', "Ana Pop", 1111111111111)
        try:
            validator.validate(client_invalid)
            assert False
        except ValueError:
            assert True

        client_invalid = Client(1, "", 1111111111111)
        try:
            validator.validate(client_invalid)
            assert False
        except ValueError:
            assert True