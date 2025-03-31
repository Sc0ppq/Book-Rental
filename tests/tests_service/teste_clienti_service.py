from repo.ClientiRepo import ClientRepository, ClientiFileRepo
from domain.ValidatorClient import ValidatorClient
from service.ClientiService import ClientiService
import unittest
from utils.file_utils import *

class TestClientiService(unittest.TestCase):
    def setUp(self):
        self.repo = ClientRepository()
        self.validator = ValidatorClient()
        self.service = ClientiService(self.repo, self.validator)

    def test_add_client(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        client = self.repo.cauta_client_id(1)
        assert client is not None
        assert client.id == 1
        assert client.nume == "Ana Pop"
        assert client.CNP == 1111111111111

        try:
            self.service.add_client(1, "Ana Pop", 2222222222222)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu ID-ul 1 exista deja!"

        try:
            self.service.add_client(2, "Ana Pop", 1111111111111)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu CNP-ul 1111111111111 exista deja!"


    def test_modif_client(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        self.service.add_client(2, "Maria Pop", 2222222222222)

        self.service.modify_client(1,"Alex Pop", 3333333333333, 3)
        client = self.repo.cauta_client_id(3)
        assert client is not None
        assert client.id == 3
        assert client.nume == "Alex Pop"
        assert client.CNP == 3333333333333

        try:
            self.service.modify_client(1,"Alex Pop", 3333333333334, 4)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu ID-ul 1 nu exista!"

        try:
            self.service.modify_client(2,"Alex Pop", 3333333333334, 3)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu ID-ul 3 exista deja!"

        try:
            self.service.modify_client(2,"Alex Pop", 3333333333333, 4)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu CNP-ul 3333333333333 exista deja!"


    def test_cauta_client_id(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)

        client = self.service.cauta_client_id(1)
        assert client is not None
        assert client.id == 1

        client = self.service.cauta_client_id(2)
        assert client is None

    def test_cauta_client_CNP(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)

        client = self.service.cauta_client_CNP(1111111111111)
        assert client is not None
        assert client.CNP == 1111111111111

        client = self.service.cauta_client_CNP(2222222222222)
        assert client is None

    def test_sterge_client_id(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        self.service.sterge_client_id(1)
        client = self.service.cauta_client_id(1)
        assert client is None

    def test_filtreaza_dupa_nume(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        self.service.add_client(2, "Maria Pop", 2222222222222)
        self.service.add_client(3, "David Pintea", 3333333333333)

        clienti_pop = self.service.filtreaza_dupa_nume("Pop")
        assert len(clienti_pop) == 2
        assert clienti_pop[0].nume == "Ana Pop"
        assert clienti_pop[1].nume == "Maria Pop"

    def test_get_clienti(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        self.service.add_client(2, "Maria Pop", 2222222222222)

        clienti = self.service.get_clienti()
        assert len(clienti) == 2
        assert clienti[0].id == 1
        assert clienti[1].id == 2

class TestClientiServiceFile(unittest.TestCase):
    def setUp(self):
        clear_file_content('test_client.txt')
        self.repo = ClientiFileRepo('test_client.txt')
        validator = ValidatorClient()
        self.service = ClientiService(self.repo, validator)

    def test_add_client_service_file(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        client = self.repo.cauta_client_id(1)
        assert client is not None
        assert client.id == 1
        assert client.nume == "Ana Pop"
        assert client.CNP == 1111111111111

        try:
            self.service.add_client(1, "Ana Pop", 2222222222222)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu ID-ul 1 exista deja!"

        try:
            self.service.add_client(2, "Ana Pop", 1111111111111)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu CNP-ul 1111111111111 exista deja!"


    def test_modif_client_service_file(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        self.service.add_client(2, "Maria Pop", 2222222222222)

        self.service.modify_client(1,"Alex Pop", 3333333333333, 3)
        client = self.repo.cauta_client_id(3)
        assert client is not None
        assert client.id == 3
        assert client.nume == "Alex Pop"
        assert client.CNP == 3333333333333

        try:
            self.service.modify_client(1,"Alex Pop", 3333333333334, 4)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu ID-ul 1 nu exista!"

        try:
            self.service.modify_client(2,"Alex Pop", 3333333333334, 3)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu ID-ul 3 exista deja!"

        try:
            self.service.modify_client(2,"Alex Pop", 3333333333333, 4)
            assert False
        except ValueError as e:
            assert str(e) == "Clientul cu CNP-ul 3333333333333 exista deja!"


    def test_cauta_client_id_service_file(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)

        client = self.service.cauta_client_id(1)
        assert client is not None
        assert client.id == 1

        client = self.service.cauta_client_id(2)
        assert client is None

    def test_cauta_client_CNP_service_file(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)

        client = self.service.cauta_client_CNP(1111111111111)
        assert client is not None
        assert client.CNP == 1111111111111

        client = self.service.cauta_client_CNP(2222222222222)
        assert client is None

    def test_sterge_client_id_service_file(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        self.service.sterge_client_id(1)
        client = self.service.cauta_client_id(1)
        assert client is None

    def test_filtreaza_dupa_nume_service_file(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        self.service.add_client(2, "Maria Pop", 2222222222222)
        self.service.add_client(3, "David Pintea", 3333333333333)

        clienti_pop = self.service.filtreaza_dupa_nume("Pop")
        assert len(clienti_pop) == 2
        assert clienti_pop[0].nume == "Ana Pop"
        assert clienti_pop[1].nume == "Maria Pop"

    def test_get_clienti_service_file(self):
        self.service.add_client(1, "Ana Pop", 1111111111111)
        self.service.add_client(2, "Maria Pop", 2222222222222)

        clienti = self.service.get_clienti()
        assert len(clienti) == 2
        assert clienti[0].id == 1
        assert clienti[1].id == 2