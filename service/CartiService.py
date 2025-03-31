from domain.Carte import Carte
from repo.CartiRepo import CartiRepository, CartiFileRepo
from domain.ValidatorCarte import ValidatorCarte

class CartiService:
    def __init__(self, repository, validator: ValidatorCarte):
        self.__repository = repository
        self.__validator = validator

    def add_carte(self, id: int, titlu: str, autor: str, descriere: str):
        """
        Valideaza si adauga o carte in lista
        :param id: id-ul cartii
        :param titlu: titlul cartii
        :param autor: autorul cartii
        :param descriere: descrierea cartii
        :return: -; daca se trece de validare se modifica lista de carti
        :raise: ValueError daca nu se trece de validare
                ValueError daca exista deja o carte cu id-ul dat
        """
        carte = Carte(id, titlu, autor, descriere)
        self.__validator.validate(carte)
        existing_carte = self.__repository.cauta_carte_id(id)
        if existing_carte is not None:
            raise ValueError(f"Carte cu ID-ul {id} exista deja!")
        self.__repository.add_carte(carte)

    def modif_carte(self, id_vechi: int, id_nou: int, titlu: str, autor: str, descriere: str):
        """
        Se modifica datele unei carti daca sunt valide
        :param id_vechi: id-ul cartii de modificat
        :param id_nou: id-ul nou
        :param titlu: titlul nou
        :param autor: autorul nou
        :param descriere: descrierea noua
        :return: -; datele cartii se modifica daca sunt corecte
        :raise: ValueError daca nu se gaseste cartea de modificat
                ValueError daca nu se trece de validare
                ValueError daca exista deja o carte cu id-ul nou dat
        """
        carte_de_modificat = self.__repository.cauta_carte_id(id_vechi)
        if carte_de_modificat is None:
            raise ValueError(f"Carte cu ID-ul {id_vechi} nu exista!")
        carte_modificata = Carte(id_nou, titlu, autor, descriere)
        self.__validator.validate(carte_modificata)
        if id_vechi != id_nou:
            existing_carte = self.__repository.cauta_carte_id(id_nou)
            if existing_carte is not None:
                raise ValueError(f"Carte cu ID-ul {id_nou} exista deja!")
        self.__repository.update_carte(carte_de_modificat, id_nou, titlu, autor, descriere)

    def cauta_carte_id(self, id_cautat: int):
        """
        Cauta o carte in lista dupa id
        :param id_cautat: id-ul dupa care se cauta
        :return: cartea daca a fost gasita, None altfel
        """
        return self.__repository.cauta_carte_id(id_cautat)

    def sterge_carte_id(self, id: int):
        """
        Sterge o carte din lista dupa id
        :param id: id-ul dupa care se face stergerea
        :return: cartea stearsa daca a fost gasita, None altfel
        """
        carte_stearsa = self.__repository.sterge_carte_id(id)
        return carte_stearsa

    """
    def filtreaza_dupa_autor(self, autor: str):
        lista_noua = []
        for carte in self.__repository.get_all_carti():
            if carte.autor.lower() == autor.lower():
                lista_noua.append(carte)
        return lista_noua
    """

    def filtreaza_dupa_autor(self, autor: str, index=0, lista_noua=None):
        """
        Filtreaza lista de carti dupa autor folosind recursivitatea
        :param autor: autorul dupa care se face filtrarea
        :param index: indexul curent (default 0)
        :param lista_noua: lista care acumuleaza cartile care se potrivesc (default empty)
        :return: lista de carti scrise de autorul dat
        """
        if lista_noua is None:
            lista_noua = []

        if index >= len(self.__repository.get_all_carti()):  # Base case: reached the end of the list
            return lista_noua

        carte = self.__repository.get_all_carti()[index]
        if carte.autor.lower() == autor.lower():
            lista_noua.append(carte)

        return self.filtreaza_dupa_autor(autor, index + 1, lista_noua)

    def get_carti(self):
        return self.__repository.get_all_carti()

    def add_default_carti(self):
        self.add_carte(1, "Pride and Prejudice", "Jane Austen", "A classic love story set in 19th-century England.")
        self.add_carte(2, "Crime and Punishment", "Fyodor Dostoevsky", "A novel about guilt and redemption.")
        self.add_carte(3, "1984", "George Orwell", "A tale of a totalitarian regime led by the Big Brother.")
        #self.add_carte(4, "To Kill a Mockingbird", "Harper Lee", "A story about racial injustice and moral growth.")
        #self.add_carte(5, "The Great Gatsby", "F. Scott Fitzgerald","A tragic romance exploring wealth, and the American Dream.")
        #self.add_carte(6, "The Catcher in the Rye", "J.D. Salinger", "A tale of teenage rebellion.")
        #self.add_carte(7, "The Lord of the Rings", "J.R.R. Tolkien","An epic adventure of friendship, courage, and good versus evil.")


