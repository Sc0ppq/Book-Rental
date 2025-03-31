from domain.Carte import Carte
from domain.ValidatorInchiriere import ValidatorInchiriere
from domain.ValidatorCarte import ValidatorCarte
from domain.ValidatorClient import ValidatorClient
from repo.ClientiRepo import ClientiFileRepo
from repo.CartiRepo import CartiFileRepo
from repo.InchirieriRepo import InchirieriRepo
from service.InchirieriService import InchirieriService
from utils.file_utils import *
import unittest


class TestInchirieriService(unittest.TestCase):
    def setUp(self):
        clear_file_content('test_carte.txt')
        copy_file_content('default_carti.txt', 'test_carte.txt')
        carti_repo = CartiFileRepo('test_carte.txt')

        clear_file_content('test_client.txt')
        copy_file_content('default_clienti.txt', 'test_client.txt')
        client_repo = ClientiFileRepo('test_client.txt')

        clear_file_content('test_inchirieri.txt')
        inchirieri_repo = InchirieriRepo('test_inchirieri.txt')
        inchirieri_validator = ValidatorInchiriere()
        self.__inchirieri_service = InchirieriService(carti_repo, client_repo, inchirieri_repo, inchirieri_validator)

    def test_add_inchiriere(self):
        self.__inchirieri_service.add_inchiriere(1, 2345678901234)
        assert (len(self.__inchirieri_service.get_all_inchirieri()) == 1)

        self.__inchirieri_service.add_inchiriere(2, 2345678901234)
        assert (len(self.__inchirieri_service.get_all_inchirieri()) == 2)

        try:
            self.__inchirieri_service.add_inchiriere(2, 2)
            assert False
        except ValueError:
            assert True

        try:
            self.__inchirieri_service.add_inchiriere(999, 1111111111111)  # Client inexistent
            assert False
        except ValueError:
            assert True

        try:
            self.__inchirieri_service.add_inchiriere(1, 9999999999999)  # Carte inexistentă
            assert False
        except ValueError:
            assert True

    def test_returnare_inchiriere(self):
        self.__inchirieri_service.add_inchiriere(1, 2345678901234)
        assert (len(self.__inchirieri_service.get_all_inchirieri()) == 1)

        self.__inchirieri_service.remove_inchiriere(1, 2345678901234)
        assert (len(self.__inchirieri_service.get_all_inchirieri()) == 0)

        try:
            self.__inchirieri_service.remove_inchiriere(1, 2345678901234)
            assert False
        except ValueError:
            assert True

        try:
            self.__inchirieri_service.remove_inchiriere(999, 1111111111111)
            assert False
        except ValueError:
            assert True

    def test_cele_mai_inchiriate_carti(self):
        copy_file_content("default_inchirieri.txt", "test_inchirieri.txt")

        carti_inchiriate = self.__inchirieri_service.cele_mai_inchiriate_carti()
        first_dto = carti_inchiriate[0]
        assert first_dto.titlu == "Crime and Punishment"
        assert first_dto.nr_inchirieri == 4

        second_dto = carti_inchiriate[1]
        assert second_dto.titlu == "The Great Gatsby"
        assert second_dto.nr_inchirieri == 3

    def test_clienti_cu_cele_mai_multe_inchirieri(self):
        copy_file_content("default_inchirieri.txt", "test_inchirieri.txt")

        clienti_inchiriere = self.__inchirieri_service.get_cele_mmulte_inchirieri()
        first_dto = clienti_inchiriere[0]
        assert first_dto.nume == "Ana-Maria Popescu"
        assert first_dto.nr_carti == 4

        second_dto = clienti_inchiriere[1]
        assert second_dto.nume== "Ion Popescu"
        assert second_dto.nr_carti == 3

    def test_top_20_percent(self):
        copy_file_content("default_inchirieri.txt", "test_inchirieri.txt")
        top20p = self.__inchirieri_service.top_20_percent()
        assert len(top20p) == 1
        top = top20p[0]
        assert top.nume == "Ana-Maria Popescu"
        assert top.nr_carti == 4

    def test_top_20_p_books(self):
        copy_file_content("default_inchirieri.txt", "test_inchirieri.txt")
        top20pBooks = self.__inchirieri_service.top_20_percent_books()
        assert len(top20pBooks) == 1
        top = top20pBooks[0]
        assert top.titlu == "Crime and Punishment"
        assert top.nr_inchirieri == 4

    def test_cele_mai_inchiriate_carti_merge(self):
        copy_file_content("default_inchirieri.txt", "test_inchirieri.txt")

        carti_inchiriate = self.__inchirieri_service.cele_m_inchiriate_carti_mergesort()
        for ob in carti_inchiriate:
            print(ob)
        first_dto = carti_inchiriate[0]
        assert first_dto.titlu == "Crime and Punishment"
        assert first_dto.nr_inchirieri == 4

        second_dto = carti_inchiriate[1]
        print(second_dto.titlu)
        assert second_dto.titlu == "The Catcher in the Rye"
        assert second_dto.nr_inchirieri == 3

    def test_clienti_cu_cele_mai_multe_inchirieri_bingo(self):
        copy_file_content("default_inchirieri.txt", "test_inchirieri.txt")

        clienti_inchiriere = self.__inchirieri_service.get_cele_mmulte_inchirieri_bingosort()
        first_dto = clienti_inchiriere[0]
        assert first_dto.nume == "Ana-Maria Popescu"
        assert first_dto.nr_carti == 4

        second_dto = clienti_inchiriere[1]
        assert second_dto.nume== "Ion Popescu"
        assert second_dto.nr_carti == 3