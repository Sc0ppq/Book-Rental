from domain.Inchirieri import Inchirieri
from domain.Client import Client
from domain.Carte import Carte
import unittest

class TestInchirieri(unittest.TestCase):
    def test_create_inchiriere(self):
        carte = Carte(2, "title", "author", "description")
        client = Client(1, "name", 1212121212121)

        inchiriere = Inchirieri(carte.id, client.CNP)

        assert (inchiriere.carte_id == carte.id)
        assert (inchiriere.client_cnp == client.CNP)

    def test_inchirieri_egale(self):
        carte1 = Carte(2, "title", "author", "description")
        client1 = Client(1, "name", 1212121212121)

        inchiriere1 = Inchirieri(carte1.id, client1.CNP)
        inchiriere2 = Inchirieri(carte1.id, client1.CNP)
        assert (inchiriere1 == inchiriere2)

        carte2 = Carte(3, "title", "author", "description")
        inchiriere3 = Inchirieri(carte2.id, client1.CNP)
        assert (inchiriere3 != inchiriere1)