from domain.Carte import Carte
from repo.CartiRepo import CartiRepository, CartiFileRepo
import unittest

from utils.file_utils import clear_file_content, copy_file_content


class TestCartiRepository(unittest.TestCase):

    def test_add_carte(self):
        repo = CartiRepository()
        carte = Carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        repo.add_carte(carte)
        assert repo.get_all_carti() == [carte]

    def test_cauta_carte_id(self):
        repo = CartiRepository()
        carte = Carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        repo.add_carte(carte)
        assert repo.cauta_carte_id(1) == carte
        assert repo.cauta_carte_id(2) is None

    def test_update_carte(self):
        repo = CartiRepository()
        carte = Carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        repo.add_carte(carte)
        repo.update_carte(carte, 2, 'Animal Farm', 'George Orwell', 'A political allegory.')
        updated_carte = repo.cauta_carte_id(2)
        assert updated_carte.id == 2
        assert updated_carte.titlu == 'Animal Farm'
        assert updated_carte.autor == 'George Orwell'
        assert updated_carte.desc == 'A political allegory.'

    def test_sterge_carte_id(self):
        repo = CartiRepository()
        carte = Carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        repo.add_carte(carte)
        repo.sterge_carte_id(1)
        assert repo.get_all_carti() == []
        assert repo.cauta_carte_id(1) is None

    def test_get_all(self):
        repo = CartiRepository()
        carte1 = Carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        carte2 = Carte(2, 'Animal Farm', 'George Orwell', 'A political allegory.')
        repo.add_carte(carte1)
        repo.add_carte(carte2)
        assert repo.get_all_carti() == [carte1, carte2]


class TestCartiFileRepo(unittest.TestCase):
    def setUp(self):
        clear_file_content("test_carte.txt")
        self.repo = CartiFileRepo("test_carte.txt")

    def test_read_from_file(self):
        copy_file_content("default_carti.txt", "test_carte.txt")
        self.assertEqual(self.repo.size(), 7)

    def test_add_carte(self):
        carte = Carte(1, "titlu", "autor", "desc")
        self.repo.add_carte(carte)
        assert(self.repo.size() == 1)
        carte2 = Carte(2, "titlu", "autor", "desc")
        self.repo.add_carte(carte2)
        assert (self.repo.size() == 2)
        assert(self.repo.get_all_carti() == [carte, carte2])

    def test_find_carte(self):
        assert (self.repo.size() == 0)

        carte1=Carte(1, "titlu", "autor", "desc")
        carte2=Carte(2, "titlu2", "autor2", "desc2")
        carte3=Carte(3, "titlu3", "autor3", "desc3")

        self.repo.add_carte(carte1)
        self.repo.add_carte(carte2)
        self.repo.add_carte(carte3)

        assert (self.repo.size() == 3)

        assert (self.repo.cauta_carte_id(1) is not None)
        assert (self.repo.cauta_carte_id(1) == carte1)
        assert (self.repo.cauta_carte_id(2) is not None)
        assert (self.repo.cauta_carte_id(2) == carte2)
        assert (self.repo.cauta_carte_id(3) is not None)
        assert (self.repo.cauta_carte_id(3) == carte3)
        assert (self.repo.cauta_carte_id(10) is None)

    def test_delete_carte(self):
        carte1 = Carte(1, "titlu", "autor", "desc")
        carte2 = Carte(2, "titlu2", "autor2", "desc2")
        carte3 = Carte(3, "titlu3", "autor3", "desc3")

        self.repo.add_carte(carte1)
        self.repo.add_carte(carte2)
        self.repo.add_carte(carte3)

        assert (self.repo.size() == 3)

        deleted_book = self.repo.sterge_carte_id(1)
        assert (self.repo.size() == 2)
        assert (self.repo.cauta_carte_id(1) is None)
        assert (deleted_book.titlu == "titlu")

        deleted_book = self.repo.sterge_carte_id(2)
        assert (self.repo.size() == 1)
        assert (self.repo.cauta_carte_id(2) is None)
        assert (deleted_book.titlu == "titlu2")

        non_exist_book = self.repo.sterge_carte_id(111)
        assert (non_exist_book is None)

    def test_update_carte(self):
        carte = Carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        self.repo.add_carte(carte)
        self.repo.update_carte(carte, 2, 'Animal Farm', 'George Orwell', 'A political allegory.')
        updated_carte = self.repo.cauta_carte_id(2)
        assert updated_carte.id == 2
        assert updated_carte.titlu == 'Animal Farm'
        assert updated_carte.autor == 'George Orwell'
        assert updated_carte.desc == 'A political allegory.'