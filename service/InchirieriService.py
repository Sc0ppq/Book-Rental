from domain.Inchirieri import Inchirieri
from repo.CartiRepo import CartiFileRepo
from repo.ClientiRepo import ClientiFileRepo
from repo.InchirieriRepo import InchirieriRepo
from domain.ValidatorInchiriere import ValidatorInchiriere
from service.Sorters import *

class InchirieriService:
    def __init__(self, carte_repo:CartiFileRepo, clienti_repo:ClientiFileRepo, inchirieri_repo:InchirieriRepo, inchirieri_validator:ValidatorInchiriere):
        self.__carte_repo = carte_repo
        self.__clienti_repo = clienti_repo
        self.__inchirieri_repo = inchirieri_repo
        self.__inchirieri_validator = inchirieri_validator

    def add_inchiriere(self, id_carte, cnp):
        """
        Adauga o inchiriere in lista daca are date valide
        :param id_carte: id-ul cartii de inchiriat
        :param cnp: cnp-ul clientului care face inchirierea
        :return: -; se modifica lista de inchirieri daca datele sunt valide
        :raise: ValueError daca nu exista cartea cu id-ul dat
                ValueError daca nu exista clientul cu cnp-ul dat
                ValueError daca exista deja o astfel de inchiriere
        """
        inchiriere = Inchirieri(id_carte, cnp)
        self.__inchirieri_validator.validate(inchiriere)

        carte = self.__carte_repo.cauta_carte_id(id_carte)
        if carte is None:
            raise ValueError("Nu exista carte cu id-ul dat")

        client = self.__clienti_repo.cauta_client_CNP(cnp)
        if client is None:
            raise ValueError("Nu exista clientul cu cnp-ul dat")

        existing_inchiriere = self.__inchirieri_repo.find_inch(id_carte, cnp)
        if existing_inchiriere is not None:
            raise ValueError("Exista deja o astfel de inchiriere!")

        self.__inchirieri_repo.add_inchiriere(inchiriere)

    def remove_inchiriere(self, id_carte, cnp):
        """
        Returneaza o carte/ Sterge o inchiriere din lista daca datele sunt valide
        :param id_carte: id-ul cartii de returnat
        :param cnp: cnp-ul clientului care face retrunarea
        :return: -; se modifica lista de inchirieri daca datele sunt valide
        :raise: ValueError daca nu exista o astfel de inchiriere
        """
        returnare = self.__inchirieri_repo.find_inch(id_carte, cnp)
        if returnare is None:
            raise ValueError("Nu exista acest tip de inchiriere")
        self.__inchirieri_repo.delete_inchiriere(returnare)

    def get_all_inchirieri(self):
        return self.__inchirieri_repo.get_all_inchirieri()

    def cele_mai_inchiriate_carti(self):
        """
        :return: Lista cu cartile cu cele mai multe inchirieri, sortate dupa numarul de inchirieri
        """
        dto_list = self.__inchirieri_repo.get_nr_inchirieri()
        dto_list = sorted(dto_list, key=lambda item: item.nr_inchirieri, reverse=True)

        carti_inchiriate = dto_list
        for carte_dto in carti_inchiriate:
            id = carte_dto.id
            carte_obj = self.__carte_repo.cauta_carte_id(id)
            carte_dto.titlu = carte_obj.titlu

        return carti_inchiriate

    def cele_m_inchiriate_carti_mergesort(self):
        """
        Sorteaza dupa numarul de inchirieri lista de carti
        :return: lista de carti sortata
        """
        dto_list = list(self.__inchirieri_repo.get_nr_inchirieri())
        dto_list = mergeSort(dto_list, key=lambda item: item.nr_inchirieri, reverse=True)

        carti_inchiriate = dto_list
        for carte_dto in carti_inchiriate:
            id = carte_dto.id
            carte_obj = self.__carte_repo.cauta_carte_id(id)
            carte_dto.titlu = carte_obj.titlu

        return carti_inchiriate

    def get_cele_mmulte_inchirieri_bingosort(self):
        """
        Sorteaza dupa numarul de carti inchiriate si nume lista de clienti
        :return: lista de clienti sortata
        """
        dto_list = list(self.__inchirieri_repo.get_nr_carti())

        for client_dto in dto_list:
            cnp = client_dto.cnp
            client_obj = self.__clienti_repo.cauta_client_CNP(cnp)
            client_dto.nume = client_obj.nume

        dto_list = bingoSort(dto_list, key=lambda item: (-item.nr_carti, item.nume))

        return dto_list

    def get_cele_mmulte_inchirieri(self):
        """
        :return: Lista cu clientii cu cele mai multe carti inchiriate, sortati dupa nume si numarul de carti
        """
        dto_list = self.__inchirieri_repo.get_nr_carti()

        for client_dto in dto_list:
            cnp = client_dto.cnp
            client_obj = self.__clienti_repo.cauta_client_CNP(cnp)
            client_dto.nume = client_obj.nume
        dto_list = sorted(dto_list, key=lambda item: (-item.nr_carti, item.nume))

        return dto_list

    def top_20_percent(self):
        # O(n*logn)
        """
        :return: Lista cu top 20% clienti cu cele mai multe carti inchiriate, sortati dupa nume si nume
        """
        clienti_sortati = self.get_cele_mmulte_inchirieri() #O(n*logn)
        top_20_count = int(0.2 * len(clienti_sortati)) #Θ(1)
        top_20_percent = clienti_sortati[:top_20_count] #Θ(n*0.2) = Θ(n)

        return top_20_percent

    def top_20_percent_books(self):
        """
        :return: Lista cu top 20% carti care au fost inchiriate de cele mai multe ori
        """
        carti_sortate = self.cele_mai_inchiriate_carti()
        top_20_count = int(0.2 * len(carti_sortate))
        top_20_percent = carti_sortate[:top_20_count]

        return top_20_percent
