from domain.dtos import CartiInchirieri,ClientInchirieri
from domain.Inchirieri import Inchirieri

class InchirieriRepo:
    def __init__(self, filename):
        self.filename = filename

    def read_from_file(self):
        f = open(self.filename, mode = 'r')

        inchirieri = []
        lines = f.readlines()
        for line in lines:
            elements = line.split('|')
            elements = [element.strip() for element in elements]
            id_carte = int(elements[0])
            CNP = int(elements[1])
            inchiriere = Inchirieri(id_carte, CNP)
            inchirieri.append(inchiriere)
        f.close()
        return inchirieri

    def write_to_file(self, inchirieri):
        with open(self.filename, mode = 'w') as file:
            for inchiriere in inchirieri:
                inchiriere_elements = [inchiriere.carte_id, inchiriere.client_cnp]
                inchirieri_elements = [str(element) for element in inchiriere_elements]
                line = '|'.join(inchirieri_elements) + '\n'
                file.write(line)

    def find_inch(self,id:int,cnp:int):
        """
        Gaseste o inchiriere in lista dupa id-ul cartii si cnp-ul clientului
        :param id: id-ul cartii
        :param cnp: cnp-ul clientului
        :return: inchirierea daca a fost gasita
                None, altfel
        """
        inchirieri = self.read_from_file()
        for inchiriere in inchirieri:
            if inchiriere.carte_id== id and inchiriere.client_cnp == cnp:
                return inchiriere
        return None

    def add_inchiriere(self,inchiriere):
        """
        Adauga o inchiriere in lista
        :param inchiriere: inchirierea de adaugat
        :return: -; se modifica lista de inchirieri
        """
        inchirieri = self.read_from_file()
        inchirieri.append(inchiriere)
        self.write_to_file(inchirieri)

    def delete_inchiriere(self,inchiriere):
        """
        Sterge o inchiriere daca exista
        :param inchiriere: inchirierea de sters
        :return: inchirierea stearsa daca a fist gasita
                None, altfel
        """
        inch_de_sters = self.find_inch(inchiriere.carte_id,inchiriere.client_cnp)
        if inch_de_sters:
            inchirieri = self.read_from_file()
            inchirieri.remove(inchiriere)
            self.write_to_file(inchirieri)
            return inchiriere
        return None

    def get_nr_carti(self):
        """
        :return: Numarul de carti inchiriate de un client
        """
        inchirieri = self.read_from_file()
        clienti_cu_inchirieri = {}
        for inchiriere in inchirieri:
            client_cnp = inchiriere.client_cnp
            if client_cnp in clienti_cu_inchirieri:
                clienti_cu_inchirieri[client_cnp].increase_nr_carti()
            else:
                clienti_cu_inchirieri[client_cnp] = ClientInchirieri(client_cnp)
        return clienti_cu_inchirieri.values()

    def get_nr_inchirieri(self):
        """
        :return: De cate ori este inchiriata o carte
        """
        inchirieri = self.read_from_file()
        carti_inchiriate = {}
        for inchiriere in inchirieri:
            carte_id = inchiriere.carte_id
            if carte_id in carti_inchiriate:
                carti_inchiriate[carte_id].increase_nr_inchirieri()
            else:
                carti_inchiriate[carte_id] = CartiInchirieri(inchiriere.carte_id)
        return carti_inchiriate.values()

    def get_all_inchirieri(self) -> list:
        """
        :return: lista de inchirieri
        """
        return self.read_from_file()

    def size(self):
        return len(self.read_from_file())