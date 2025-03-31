import unittest

from domain.Carte import Carte
from domain.Inchirieri import Inchirieri
from repo.InchirieriRepo import InchirieriRepo
from utils.file_utils import *

class TestInchirieriRepo(unittest.TestCase):
    def setUp(self):
        clear_file_content('test_inchirieri.txt')
        self.test_repo = InchirieriRepo("test_inchirieri.txt")

    def test_read_from_file(self):
        copy_file_content("default_inchirieri.txt", "test_inchirieri.txt")
        self.assertEqual(self.test_repo.size(), 5)

    def test_store(self):
        inchiriere = Inchirieri(2,1548975642398)
        self.test_repo.add_inchiriere(inchiriere)
        assert (self.test_repo.size() == 1)

    def test_find(self):
        assert (self.test_repo.size() == 0)

        inchiriere1 = Inchirieri(2,1548975642398)
        inchiriere2 = Inchirieri(3,1548975642398)
        inchiriere3 = Inchirieri(2,2548975642398)

        self.test_repo.add_inchiriere(inchiriere1)
        self.test_repo.add_inchiriere(inchiriere2)
        self.test_repo.add_inchiriere(inchiriere3)

        assert (self.test_repo.size() == 3)

        assert (self.test_repo.find_inch(2, 1548975642398) is not None)
        assert (self.test_repo.find_inch(3, 1548975642398) is not None)
        assert (self.test_repo.find_inch(2, 2548975642398) is not None)
        assert (self.test_repo.find_inch(1, 1548975642398) is None)
        assert (self.test_repo.find_inch(2, 3548975642398) is None)

    def test_delete(self):
        inchiriere1 = Inchirieri(2, 1548975642398)
        inchiriere2 = Inchirieri(3, 1548975642398)
        inchiriere3 = Inchirieri(2, 2548975642398)

        self.test_repo.add_inchiriere(inchiriere1)
        self.test_repo.add_inchiriere(inchiriere2)

        assert (self.test_repo.size() == 2)
        deleted_inchiriere = self.test_repo.delete_inchiriere(inchiriere1)
        assert (self.test_repo.size() == 1)
        assert (self.test_repo.find_inch(2, 1548975642398) is None)
        assert (deleted_inchiriere.carte_id == 2)


        deleted_inchiriere2 = self.test_repo.delete_inchiriere(inchiriere3)
        assert (deleted_inchiriere2 is None)

