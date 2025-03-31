from domain.Client import Client
from repo.ClientiRepo import ClientRepository, ClientiFileRepo
import unittest

from utils.file_utils import clear_file_content, copy_file_content


class TestClientiRepository(unittest.TestCase):
    def setUp(self):
        self.repo = ClientRepository()

    def test_add_client(self):
        client = Client(1,"Ana Pop", 1111111111111)
        self.repo.add_client(client)
        assert self.repo.get_all_clienti() == [client]

        client2 = Client(2,"Ana Pop", 2222222222222)
        self.repo.add_client(client2)
        assert self.repo.get_all_clienti() == [client, client2]

    def test_cauta_client_id(self):
        client = Client(1,"Ana Pop", 1111111111111)
        self.repo.add_client(client)
        assert self.repo.cauta_client_id(1) == client
        assert self.repo.cauta_client_id(2) is None

    def test_cauta_client_CNP(self):
        client = Client(1,"Ana Pop", 1111111111111)
        self.repo.add_client(client)
        assert self.repo.cauta_client_CNP(1111111111111) == client
        assert self.repo.cauta_client_CNP(2222222222222) is None

    def test_update_client(self):
        client = Client(1,"Ana Pop", 1111111111111)
        self.repo.add_client(client)
        self.repo.update_client(client, 2, "Maria Pop", 2222222222222)
        updated_client = self.repo.cauta_client_id(2)
        assert updated_client.id == 2
        assert updated_client.nume == "Maria Pop"
        assert updated_client.CNP == 2222222222222


    def test_sterge_client_id(self):
        client = Client(1,"Ana Pop", 1111111111111)
        self.repo.add_client(client)
        self.repo.sterge_client_id(1)
        assert self.repo.get_all_clienti() == []
        assert self.repo.cauta_client_id(2) is None

    def test_get_all_clienti(self):
        client1 = Client(1,"Ana Pop", 1111111111111)
        client2 = Client(2,"Maria Pop", 2222222222222)
        self.repo.add_client(client1)
        self.repo.add_client(client2)
        assert self.repo.get_all_clienti() == [client1, client2]


class TestClientiFileRepo(unittest.TestCase):
    def setUp(self):
        clear_file_content("test_client.txt")
        self.repo = ClientiFileRepo("test_client.txt")

    def test_read_from_file(self):
        copy_file_content("default_clienti.txt", "test_client.txt")
        self.assertEqual(self.repo.size(), 7)

    def test_add_client(self):
        client = Client(1,"Ana Pop", 1111111111111)
        self.repo.add_client(client)
        assert(self.repo.size() == 1)
        client2 = Client(2,"Maria Pop", 2222222222222)
        self.repo.add_client(client2)
        assert(self.repo.size() == 2)
        assert self.repo.get_all_clienti() == [client, client2]

    def test_find_client_id(self):
        client1 = Client(1,"Ana Pop", 1111111111111)
        client2 = Client(2,"Maria Pop", 2222222222222)
        client3 = Client(3,"Alexia Pop", 3333333333333)

        self.repo.add_client(client1)
        self.repo.add_client(client2)
        self.repo.add_client(client3)

        assert (self.repo.size() == 3)
        assert (self.repo.cauta_client_id(1) == client1)
        assert (self.repo.cauta_client_id(2) == client2)
        assert (self.repo.cauta_client_id(3) == client3)
        assert (self.repo.cauta_client_id(10) is None)

    def test_find_client_CNP(self):
        client1 = Client(1, "Ana Pop", 1111111111111)
        client2 = Client(2, "Maria Pop", 2222222222222)
        client3 = Client(3, "Alexia Pop", 3333333333333)

        self.repo.add_client(client1)
        self.repo.add_client(client2)
        self.repo.add_client(client3)

        assert (self.repo.size() == 3)
        assert (self.repo.cauta_client_CNP(1111111111111) == client1)
        assert (self.repo.cauta_client_CNP(2222222222222) == client2)
        assert (self.repo.cauta_client_CNP(3333333333333) == client3)

    def test_delete_client(self):
        client1 = Client(1, "Ana Pop", 1111111111111)
        client2 = Client(2, "Maria Pop", 2222222222222)
        client3 = Client(3, "Alexia Pop", 3333333333333)

        self.repo.add_client(client1)
        self.repo.add_client(client2)
        self.repo.add_client(client3)

        assert (self.repo.size() == 3)

        deleted_client = self.repo.sterge_client_id(1)
        assert (self.repo.size() == 2)
        assert (self.repo.cauta_client_id(1) is None)
        assert (deleted_client.nume == "Ana Pop")

        deleted_client = self.repo.sterge_client_id(2)
        assert (self.repo.size() == 1)
        assert (self.repo.cauta_client_id(2) is None)
        assert (deleted_client.nume == "Maria Pop")

        non_exist_client = self.repo.sterge_client_id(111)
        assert (non_exist_client is None)

    def test_update_client(self):
        client = Client(1,"Ana Pop", 1111111111111)
        self.repo.add_client(client)
        self.repo.update_client(client, 2, "Maria Pop", 2222222222222)
        updated_client = self.repo.cauta_client_id(2)
        assert updated_client.id == 2
        assert updated_client.nume == "Maria Pop"
        assert updated_client.CNP == 2222222222222