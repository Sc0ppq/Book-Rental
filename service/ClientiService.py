from domain.Client import Client
from repo.ClientiRepo import ClientRepository, ClientRepository, ClientiFileRepo
from domain.ValidatorClient import ValidatorClient

class ClientiService:
    def __init__(self, repository, validator: ValidatorClient):
        self.__repository = repository
        self.__validator = validator

    def add_client(self, id:int, nume:str, CNP:int):
        """
        Adauga un client in lista daca datele sale sunt valide
        :param id: id-ul clientului
        :param nume: numele clientului
        :param CNP: CNP-ul clientului
        :return: -; se modifica lista de clienti daca datele sunt valide
        :raise: ValueError daca nu se trece de validare
                ValueError daca exista deja un client cu id-ul dat
                ValueError daca exista deja un client cu CNP-ul dat
        """
        client=Client(id, nume, CNP)
        self.__validator.validate(client)
        existing_client = self.__repository.cauta_client_id(id)
        if existing_client is not None:
            raise ValueError(f"Clientul cu ID-ul {id} exista deja!")
        existing_client_CNP = self.__repository.cauta_client_CNP(CNP)
        if existing_client_CNP is not None:
            raise ValueError(f"Clientul cu CNP-ul {CNP} exista deja!")
        self.__repository.add_client(client)

    def modify_client(self, id_vechi:int, nume:str, CNP:int, id_nou:int):
        """
        Modifica un client din lista daca datele sale sunt valide
        :param id_vechi: id-ul clientului de modificat
        :param nume: numele nou
        :param CNP: CNP-ul nou
        :param id_nou: id-ul nou
        :return: -; se modifica datele clientului daca sunt valide
        :raise: ValueError daca nu exista clientul de modificar
                ValueError daca nu se trece de validare
                ValueError daca exista deja un client cu id-ul nou
                ValueError daca exista deja un client cu CNP-ul nou
        """
        client_de_modif = self.__repository.cauta_client_id(id_vechi)
        if client_de_modif is None:
            raise ValueError(f"Clientul cu ID-ul {id_vechi} nu exista!")
        client_modificat = Client(id_nou, nume, CNP)
        self.__validator.validate(client_modificat)
        if id_vechi!=id_nou:
            existing_client = self.__repository.cauta_client_id(id_nou)
            if existing_client is not None:
                raise ValueError(f"Clientul cu ID-ul {id_nou} exista deja!")
        if client_de_modif.CNP != client_modificat.CNP:
            existing_client_CNP = self.__repository.cauta_client_CNP(CNP)
            if existing_client_CNP is not None:
                raise ValueError(f"Clientul cu CNP-ul {CNP} exista deja!")
        self.__repository.update_client(client_de_modif, id_nou, nume, CNP)

    def cauta_client_id(self, id:int):
        """
        Cauta un client in lista dupa id
        :param id: id-ul dupa care se cauta
        :return: clientul daca a fost gasit, None altfel
        """
        return self.__repository.cauta_client_id(id)

    def cauta_client_CNP(self, CNP:int):
        """
        Cauta un client in lista dupa CNP
        :param CNP: cnp-ul dupa care se cauta
        :return: clientul daca a fost gasot, None, altfel
        """
        return self.__repository.cauta_client_CNP(CNP)

    def sterge_client_id(self, id:int):
        """
        Sterge un client din lista dupa id
        :param id: id-ul clientului de sters
        :return: clientul sters daca a fost gasit, None altfel
        """
        client_sters = self.__repository.sterge_client_id(id)
        return client_sters

    def filtreaza_dupa_nume(self, nume:str):
        """
        Filtreaza lista de clienti dupa nume
        :param nume: numele dupa care se face filtrarea
        :return: lista de clienti cu numele dat
        """
        lista_noua = []
        for client in self.__repository.get_all_clienti():
            if nume.lower() in client.nume.lower():
                lista_noua.append(client)
        return lista_noua

    def get_clienti(self):
        return self.__repository.get_all_clienti()

    def add_default_clienti(self):
        self.add_client(1, "Ana Pop", 1234567891234)
        self.add_client(2, "Ion Popescu", 2345678901234)
        self.add_client(3, "Maria Ionescu", 3456789012345)
        #self.add_client(4, "Andrei Marin", 4567890123456)
        #self.add_client(5, "Elena Georgescu", 5678901234567)
        #self.add_client(6, "Diana Florescu", 6789012345678)
        #self.add_client(7, "Mihai Tudor", 7890123456789)
