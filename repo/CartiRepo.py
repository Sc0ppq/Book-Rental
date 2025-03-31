from domain.Carte import Carte

class CartiRepository:
    def __init__(self):
        self.__lista_carti = []

    def add_carte(self, carte: Carte):
        """
        Adauga o carte la lista de carti
        :param carte: cartea de adaugat
        :return: -; lista de carti e modificata
        """
        self.__lista_carti.append(carte)

    """
    def cauta_carte_id(self, id_cautat: int):
        for carte in self.__lista_carti:
            if carte.id == id_cautat:
                return carte
        return None
    """

    def cauta_carte_id(self, id_cautat: int, index=0):
        """
        Cauta o carte in lista dupa id folosind recursivitatea
        :param id_cautat: id-ul dupa care se cauta cartea
        :param index: indexul curent (default 0)
        :return: cartea daca a fost gasita, altfel None
        """
        if index >= len(self.__lista_carti):
            return None

        if self.__lista_carti[index].id == id_cautat:
            return self.__lista_carti[index]

        return self.cauta_carte_id(id_cautat, index + 1)


    def update_carte(self, carte_de_modif: Carte, id_nou: int, titlu: str, autor: str, descriere: str):
        """
        Modifica datele unei carti
        :param carte_de_modif: cartea de modificat
        :param id_nou: id-ul nou
        :param titlu: titlul nou
        :param autor: autorul nou
        :param descriere: descrierea noua
        :return: -; se modifica datele cartii
        """
        carte_de_modif.id = id_nou
        carte_de_modif.titlu = titlu
        carte_de_modif.autor = autor
        carte_de_modif.desc = descriere

    def sterge_carte_id(self, id: int):
        """
        Sterge o carte din lista dupa id
        :param id: id-ul cartii de sters
        :return: cartea stearsa daca a fost gasita, altfel None
        """
        carte_de_sters = self.cauta_carte_id(id)
        if carte_de_sters is not None:
            self.__lista_carti.remove(carte_de_sters)
            return carte_de_sters
        return None

    def get_all_carti(self):
        return self.__lista_carti


class CartiFileRepo:
    def __init__(self, filename):
        self.filename = filename

    def read_from_file(self):
        f = open(self.filename, mode = 'r')
        carti = []
        lines = f.readlines()
        for line in lines:
            elements = line.split('|')
            elements = [element.strip() for element in elements]
            id = int(elements[0])
            titlu = elements[1]
            autor = elements[2]
            desc = elements[3]
            carte = Carte(id, titlu, autor,desc)
            carti.append(carte)
        f.close()
        return carti

    def write_to_file(self, carti):
        with open(self.filename, mode = 'w') as file:
            for carte in carti:
                carte_elements = [carte.id, carte.titlu, carte.autor, carte.desc]
                carti_elements = [str(element) for element in carte_elements]
                line = '|'.join(carti_elements) + '\n'
                file.write(line)

    def add_carte(self, carte: Carte):
        carti = self.read_from_file()
        carti.append(carte)
        self.write_to_file(carti)

    def cauta_carte_id(self, id_cautat: int):
        carti = self.read_from_file()
        for carte in carti:
            if carte.id == id_cautat:
                return carte
        return None

    def update_carte(self,carte_de_modif: Carte, id_nou: int, titlu: str, autor: str, descriere: str):
        carti = self.read_from_file()

        for carte in carti:
            if carte.id == carte_de_modif.id:
                carte.id = id_nou
                carte.titlu = titlu
                carte.autor = autor
                carte.desc = descriere
                break

        self.write_to_file(carti)

    def sterge_carte_id(self, id: int):
        carti = self.read_from_file()
        carte_de_sters = self.cauta_carte_id(id)
        if carte_de_sters is not None:
            carti.remove(carte_de_sters)
            self.write_to_file(carti)
            return carte_de_sters
        return None

    def get_all_carti(self):
        return self.read_from_file()

    def size(self):
        return len(self.read_from_file())