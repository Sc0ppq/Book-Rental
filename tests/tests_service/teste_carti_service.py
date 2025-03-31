from domain.Carte import Carte
from repo.CartiRepo import CartiRepository, CartiFileRepo
from domain.ValidatorCarte import ValidatorCarte
from service.CartiService import CartiService
import unittest
from utils.file_utils import *


class TestCartiService(unittest.TestCase):
    def setUp(self):
        self.repo = CartiRepository()
        self.validator = ValidatorCarte()
        self.service = CartiService(self.repo, self.validator)

    def test_add_carte(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        carte = self.repo.cauta_carte_id(1)
        assert carte is not None
        assert carte.id == 1
        assert carte.titlu == '1984'
        assert carte.autor == 'George Orwell'
        assert carte.desc == 'A dystopian novel.'

        try:
            self.service.add_carte(1, 'Animal Farm', 'George Orwell', 'A political allegory.')
            assert False, "Expected ValueError"
        except ValueError as e:
            assert str(e) == "Carte cu ID-ul 1 exista deja!"

    def test_modif_carte(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        self.service.add_carte(3, 'Brave New World', 'Aldous Huxley', 'A dystopian society.')

        self.service.modif_carte(1, 2, 'Animal Farm', 'George Orwell', 'A political allegory.')
        carte = self.repo.cauta_carte_id(2)
        assert carte is not None
        assert carte.id == 2
        assert carte.titlu == 'Animal Farm'
        assert carte.autor == 'George Orwell'
        assert carte.desc == 'A political allegory.'

        try:
            self.service.modif_carte(1, 3, 'Brave New World', 'Aldous Huxley', 'A dystopian society.')
            assert False
        except ValueError as e:
            assert str(e) == "Carte cu ID-ul 1 nu exista!"

        try:
            self.service.modif_carte(2, 3, '1984', 'George Orwell', 'A dystopian novel.')
            assert False
        except ValueError as e:
            assert str(e) == "Carte cu ID-ul 3 exista deja!"

    def test_cauta_carte_id(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')

        carte = self.service.cauta_carte_id(1)
        assert carte is not None
        assert carte.id == 1

        carte = self.service.cauta_carte_id(2)
        assert carte is None

    def test_sterge_carte_id(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        self.service.sterge_carte_id(1)
        carte = self.repo.cauta_carte_id(1)
        assert carte is None

    def test_filtreaza_dupa_autor(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        self.service.add_carte(2, 'Animal Farm', 'George Orwell', 'A political allegory.')
        self.service.add_carte(3, 'Brave New World', 'Aldous Huxley', 'A dystopian society.')

        carti_george = self.service.filtreaza_dupa_autor('George Orwell')
        assert len(carti_george) == 2
        assert carti_george[0].autor == 'George Orwell'
        assert carti_george[1].autor == 'George Orwell'

        carti_huxley = self.service.filtreaza_dupa_autor('Aldous Huxley')
        assert len(carti_huxley) == 1
        assert carti_huxley[0].autor == 'Aldous Huxley'

    def test_get_carti(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        self.service.add_carte(2, 'Animal Farm', 'George Orwell', 'A political allegory.')

        carti = self.service.get_carti()
        assert len(carti) == 2
        assert carti[0].id == 1
        assert carti[1].id == 2

class TestCartiServiceFile(unittest.TestCase):
    def setUp(self):
        clear_file_content('test_carte.txt')
        self.repo = CartiFileRepo('test_carte.txt')
        validator = ValidatorCarte()
        self.service = CartiService(self.repo, validator)

    def test_add_carte_service_file(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        carte = self.repo.cauta_carte_id(1)
        assert carte is not None
        assert carte.id == 1
        assert carte.titlu == '1984'
        assert carte.autor == 'George Orwell'
        assert carte.desc == 'A dystopian novel.'

        try:
            self.service.add_carte(1, 'Animal Farm', 'George Orwell', 'A political allegory.')
            assert False, "Expected ValueError"
        except ValueError as e:
            assert str(e) == "Carte cu ID-ul 1 exista deja!"

    def test_modif_carte_service_file(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        self.service.add_carte(3, 'Brave New World', 'Aldous Huxley', 'A dystopian society.')

        self.service.modif_carte(1, 2, 'Animal Farm', 'George Orwell', 'A political allegory.')
        carte = self.repo.cauta_carte_id(2)
        assert carte is not None
        assert carte.id == 2
        assert carte.titlu == 'Animal Farm'
        assert carte.autor == 'George Orwell'
        assert carte.desc == 'A political allegory.'

        try:
            self.service.modif_carte(1, 3, 'Brave New World', 'Aldous Huxley', 'A dystopian society.')
            assert False
        except ValueError as e:
            assert str(e) == "Carte cu ID-ul 1 nu exista!"

        try:
            self.service.modif_carte(2, 3, '1984', 'George Orwell', 'A dystopian novel.')
            assert False
        except ValueError as e:
            assert str(e) == "Carte cu ID-ul 3 exista deja!"

    def test_cauta_carte_id_service_file(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')

        carte = self.service.cauta_carte_id(1)
        assert carte is not None
        assert carte.id == 1

        carte = self.service.cauta_carte_id(2)
        assert carte is None

    def test_sterge_carte_id_service_file(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        self.service.sterge_carte_id(1)
        carte = self.repo.cauta_carte_id(1)
        assert carte is None

    def test_filtreaza_dupa_autor_service_file(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        self.service.add_carte(2, 'Animal Farm', 'George Orwell', 'A political allegory.')
        self.service.add_carte(3, 'Brave New World', 'Aldous Huxley', 'A dystopian society.')

        carti_george = self.service.filtreaza_dupa_autor('George Orwell')
        assert len(carti_george) == 2
        assert carti_george[0].autor == 'George Orwell'
        assert carti_george[1].autor == 'George Orwell'

        carti_huxley = self.service.filtreaza_dupa_autor('Aldous Huxley')
        assert len(carti_huxley) == 1
        assert carti_huxley[0].autor == 'Aldous Huxley'

    def test_get_carti_service_file(self):
        self.service.add_carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        self.service.add_carte(2, 'Animal Farm', 'George Orwell', 'A political allegory.')

        carti = self.service.get_carti()
        assert len(carti) == 2
        assert carti[0].id == 1
        assert carti[1].id == 2
