from domain.Client import Client

class ClientRepository:
    def __init__(self):
        self.__lista_clienti = []

    def add_client(self, client: Client):
        """
        Adauga un client la lista de clienti
        :param client: clientul de adaugat
        :return: -; lista de clienti este modificata
        """
        self.__lista_clienti.append(client)

    def cauta_client_id(self, id_cautat: int, index =0):
        """
        Cauta un client in lista dupa id
        :param id_cautat: id-ul dupa care se cauta clientul
        :return: clientul daca a fost gasit, altfel None
        """
        if index >= len(self.__lista_clienti):
            return None
        

        if self.__lista_clienti[index].id == id_cautat:
            return self.__lista_clienti[index]

        return self.cauta_client_id(id_cautat, index + 1)

    def cauta_client_CNP(self, CNP_cautat: int):
        """
        Cauta un client in lista dupa CNP
        :param CNP_cautat: CNP-ul dupa care se cauta clientul
        :return: clientul daca a fost gasit, altfel None
        """
        for client in self.__lista_clienti:
            if client.CNP == CNP_cautat:
                return client
        return None

    def update_client(self, client_de_modif: Client, id_nou:int, nume:str, CNP:int):
        """
        Modifica datele unui client
        :param client_de_modif: clientul de modificat
        :param id_nou: id-ul nou
        :param nume: numele nou
        :param CNP: CNP-ul nou
        :return: -; datele clientului sunt modificate
        """
        client_de_modif.id = id_nou
        client_de_modif.nume = nume
        client_de_modif.CNP = CNP

    def sterge_client_id(self, id:int):
        """
        Sterge un client din lista dupa id
        :param id: id-ul clientului de sters
        :return: clientul sters daca a fost gasit, altfel None
        """
        client_de_sters = self.cauta_client_id(id)
        if client_de_sters is not None:
            self.__lista_clienti.remove(client_de_sters)
            return client_de_sters
        return None

    def get_all_clienti(self):
        return self.__lista_clienti


class ClientiFileRepo:
    def __init__(self, filename):
        self.filename = filename

    def read_from_file(self):
        f = open(self.filename, mode = 'r')

        clienti = []
        lines = f.readlines()
        for line in lines:
            elements = line.split('|')
            elements = [element.strip() for element in elements]
            id = int(elements[0])
            nume = elements[1]
            CNP = int(elements[2])
            client = Client(id, nume, CNP)
            clienti.append(client)
        f.close()
        return clienti

    def write_to_file(self, clienti):
        with open(self.filename, mode = 'w') as file:
            for client in clienti:
                client_elements = [client.id, client.nume, client.CNP]
                clienti_elements = [str(element) for element in client_elements]
                line = '|'.join(clienti_elements) + '\n'
                file.write(line)

    def add_client(self, client):
        clienti = self.read_from_file()
        clienti.append(client)
        self.write_to_file(clienti)

    def cauta_client_id(self, id_cautat):
        clienti = self.read_from_file()
        for client in clienti:
            if client.id == id_cautat:
                return client
        return None

    def cauta_client_CNP(self, CNP_cautat):
        clienti = self.read_from_file()
        for client in clienti:
            if client.CNP == CNP_cautat:
                return client
        return None

    def update_client(self, client_de_modif: Client, id_nou, nume, CNP):
        clienti = self.read_from_file()

        for client in clienti:
            if client.id == client_de_modif.id:
                client.id = id_nou
                client.nume = nume
                client.CNP = CNP
                break

        self.write_to_file(clienti)

    def sterge_client_id(self, id):
        clienti = self.read_from_file()
        client_de_sters = self.cauta_client_id(id)
        if client_de_sters is not None:
            clienti.remove(client_de_sters)
            self.write_to_file(clienti)
            return client_de_sters
        return None

    def get_all_clienti(self):
        return self.read_from_file()

    def size(self):
        return len(self.read_from_file())