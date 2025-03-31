import random

from service.CartiService import CartiService
from service.ClientiService import ClientiService
from service.InchirieriService import InchirieriService

class Console:
    def __init__(self, carti_service: CartiService, client_service: ClientiService, inchirieri_service: InchirieriService):
        self.__carti_service = carti_service
        self.__client_service = client_service
        self.__inchirier_service = inchirieri_service

    @staticmethod
    def print_menu():
        print("1. Adauga/Modifica")
        print("2. Stergeri")
        print("3. Cautari")
        print("4. Filtrari")
        print("5. Genereaza clienti")
        print("6. Rapoarte")
        print("P. Afiseaza lista de carti")
        print("PC. Afiseaza lista de clienti")
        print("PI. Afiseaza lista de inchirieri")
        print("E. Iesire din aplicatie")

    def print_carti(self, lista_carti):
        for carte in lista_carti:
            print(carte)

    def print_clienti(self, lista_client):
        for client in lista_client:
            print(client)

    def print_inchirieri(self, lista_inchirieri):
        for inchiriere in lista_inchirieri:
            print(inchiriere)

    def citeste_info_carti(self) -> tuple:
        ID = input("Introduceti id-ul cartii: ")
        titlu = input("Introduceti titlul cartii: ")
        autor = input("Introduceti autorul cartii: ")
        desc = input("Introduceti descrierea cartii: ")

        try:
            ID = int(ID)
        except ValueError as e:
            print("ID-ul trebuie sa fie un numar intreg!")
            return None
        return ID, titlu, autor, desc

    def citeste_info_clienti(self) -> tuple:
        ID = input("Introduceti id-ul clientului: ")
        nume = input("Introduceti numele clientului: ")
        CNP = input("Introduceti CNP-ul clientului: ")

        try:
            ID = int(ID)
        except ValueError as e:
            print("ID-ul trebuie sa fie un numar intreg!")
            return None

        try:
            CNP = int(CNP)
        except ValueError as e:
            print("CNP-ul trebuie sa fie format din cifre!")
            return None

        return ID, nume, CNP


    def adauga_carte_ui(self):
        info = self.citeste_info_carti()
        if info:
            ID, titlu, autor, desc = info
            try:
                self.__carti_service.add_carte(ID, titlu, autor, desc)
                print("Carte adaugata!")
            except ValueError as e:
                print(e)

    def adauga_client_ui(self):
        info = self.citeste_info_clienti()
        if info:
            ID, nume, CNP = info
            try:
                self.__client_service.add_client(ID, nume, CNP)
                print("Client adaugat!")
            except ValueError as e:
                print(e)

    def modif_carte_ui(self):
        ID_vechi = input("Introduceti id-ul cartii de modificat: ")
        try:
            ID_vechi = int(ID_vechi)
        except ValueError:
            print("ID-ul trebuie sa fie un numar intreg!")
            return

        info = self.citeste_info_carti()
        if info:
            ID, titlu, autor, desc = info
            try:
                self.__carti_service.modif_carte(ID_vechi, ID, titlu, autor, desc)
                print("Carte modificata!")
            except ValueError as e:
                print(e)

    def modif_client_ui(self):
        ID_vechi = input("Introduceti id-ul clientului de modificat: ")
        try:
            ID_vechi = int(ID_vechi)
        except ValueError:
            print("ID-ul trebuie sa fie un numar intreg!")
            return
        info = self.citeste_info_clienti()
        if info:
            ID, nume, CNP = info
            try:
                self.__client_service.modify_client(ID_vechi, nume, CNP, ID)
                print("Client modificat!")
            except ValueError as e:
                print(e)

    def cauta_carte_id_ui(self):
        ID_cauta = input("Introduceti id-ul cartii de cautat: ")
        try:
            ID_cauta = int(ID_cauta)
            carte_gasita = self.__carti_service.cauta_carte_id(ID_cauta)
            if carte_gasita:
                print(f"Cartea cu Id-ul {ID_cauta} este: ")
                print(carte_gasita)
            else:
                print(f"Cartea cu Id-ul {ID_cauta} nu exista")
        except ValueError:
            print("ID-ul trebuie sa fie un numar intreg!")

    def cauta_client_id_ui(self):
        ID_cauta = input("Introduceti id-ul clientului de cautat: ")
        try:
            ID_cauta = int(ID_cauta)
            client_gasit = self.__client_service.cauta_client_id(ID_cauta)
            if client_gasit:
                print(f"Clientul cu Id-ul {ID_cauta} este: ")
                print(client_gasit)
            else:
                print(f"Clientul cu Id-ul {ID_cauta} nu exista")
        except ValueError:
            print("ID-ul trebuie sa fie un numar intreg!")

    def sterge_carte_id_ui(self):
        ID_sters = input("Introduceti id-ul cartii de sters: ")
        try:
            ID_sters = int(ID_sters)
            carte_stearsa = self.__carti_service.sterge_carte_id(ID_sters)
            if carte_stearsa is not None:
                print(f"Cartea cu Id-ul {ID_sters} a fost stearsa")
            else:
                print(f"Cartea cu Id-ul {ID_sters} nu exista")
        except ValueError as e:
            print(e)

    def sterge_client_id_ui(self):
        ID_sters = input("Introduceti id-ul clientului de sters: ")
        try:
            ID_sters = int(ID_sters)
            client_sters = self.__client_service.sterge_client_id(ID_sters)
            if client_sters is not None:
                print(f"Clientul cu Id-ul {ID_sters} a fost sters")
            else:
                print(f"Clientul cu Id-ul {ID_sters} nu exista")
        except ValueError as e:
            print(e)

    def filtrare_autor_ui(self):
        autor_filtr = input("Introduceti autorul dupa care se se faca filtrarea: ")
        carti_gasite = self.__carti_service.filtreaza_dupa_autor(autor_filtr)
        if carti_gasite:
            print(f"Lista de carti scrise de {autor_filtr}:")
            self.print_carti(carti_gasite)
        else:
            print(f"Nu exista carti scrise de {autor_filtr}")

    def filtrare_nume_ui(self):
        nume_filtr = input("Introduceti numele dupa care sa se faca filtrarea: ")
        clienti_gasiti = self.__client_service.filtreaza_dupa_nume(nume_filtr)
        if clienti_gasiti:
            print(f"Lista de clienti cu numele {nume_filtr}:")
            self.print_clienti(clienti_gasiti)
        else:
            print(f"Nu exista clienti cu numele {nume_filtr}")

    import random

    def generate_unique_CNP(self, existing_CNPs):
        while True:
            CNP = random.randint(10 ** 12, 10 ** 13 - 1)
            if CNP not in existing_CNPs:
                return CNP

    def randomClient(self, numar):
        first_names = ('Mihaela', 'Adrian', 'Florin', 'Andrei', 'Ana', 'Gabriela', 'Darius', 'Tudor', 'Bianca')
        last_names = ('Popescu', 'Florescu', 'Dumitrescu', 'Dragomir', 'Birle', 'Pop', 'Bercu')
        existing_CNPs = []

        for _ in range(numar):
            id = random.randint(0, 200)
            name = random.choice(first_names) + ' ' + random.choice(last_names)
            CNP = self.generate_unique_CNP(existing_CNPs)
            existing_CNPs.append(CNP)
            self.__client_service.add_client(id, name, CNP)

    def adauga_inchiriere_ui(self):
        id_carte = input("Introduceti id-ul cartii: ")
        cnp = input("Introduceti cnp: ")
        try:
            id_carte = int(id_carte)
            cnp = int(cnp)
            self.__inchirier_service.add_inchiriere(id_carte, cnp)
            print("Inchirierea a fost adaugata cu succes")
        except ValueError as e:
            print(e)

    def sterge_inchiriere_ui(self):
        id_carte = input("Introduceti id-ul cartii de returnat: ")
        cnp = input("Introduceti cnp-ul clientului care returneaza: ")
        try:
            id_carte = int(id_carte)
            cnp = int(cnp)
            self.__inchirier_service.remove_inchiriere(id_carte, cnp)
            print("Returnarea a fost facuta cu succes")
        except ValueError as e:
            print(e)

    def cele_mmulte_carti_ui(self):
        clienti_cu_inchirieri = self.__inchirier_service.get_cele_mmulte_inchirieri()
        for client in clienti_cu_inchirieri:
            print(f"Numele clientului:", client.nume, ",numar de carti inchiriate:", client.nr_carti)

    def cele_mmulte_inchirieri_ui(self):
        carti_inchiriate = self.__inchirier_service.cele_mai_inchiriate_carti()
        for carte in carti_inchiriate:
            if int(carte.nr_inchirieri)>1:
                print(f"Cartea", carte.titlu, "a fost inchiriata de", carte.nr_inchirieri, "ori.")
            else:
                print(f"Cartea", carte.titlu, "a fost inchiriata odata.")


    def cele_mmulte_carti_ui_bingo(self):
        clienti_cu_inchirieri = self.__inchirier_service.get_cele_mmulte_inchirieri_bingosort()
        for client in clienti_cu_inchirieri:
            print(f"Numele clientului:", client.nume, ",numar de carti inchiriate:", client.nr_carti)

    def cele_mmulte_inchirieri_ui_merge(self):
        carti_inchiriate = self.__inchirier_service.cele_m_inchiriate_carti_mergesort()
        for carte in carti_inchiriate:
            if int(carte.nr_inchirieri)>1:
                print(f"Cartea", carte.titlu, "a fost inchiriata de", carte.nr_inchirieri, "ori.")
            else:
                print(f"Cartea", carte.titlu, "a fost inchiriata odata.")

    def top_20_percent_ui(self):
        top_20_list = self.__inchirier_service.top_20_percent()
        for client in top_20_list:
            print(f"Numele clientului:", client.nume, ",numar de carti inchiriate:", client.nr_carti)

    def top_20_p_books_ui(self):
        top_20_p_books = self.__inchirier_service.top_20_percent_books()
        for carte in top_20_p_books:
            print(f"Titlul cartii:", carte.titlu, ",numarul de inchirieri:", carte.nr_inchirieri)


    def run(self):
        while True:
            self.print_menu()
            option = input("Introduceti optiunea: ")
            match option:
                case "1":
                    while True:
                        print("1.1 Adauga carte")
                        print("1.2 Modifica o carte existenta")
                        print("1.3 Adauga un client")
                        print("1.4 Modifica un client existent")
                        print("1.5 Inchiriere")
                        print("E. Inapoi")
                        option2 = input("Introduceti optiunea: ")
                        match option2:
                            case "1.1":
                                self.adauga_carte_ui()
                            case "1.2":
                                self.modif_carte_ui()
                            case "1.3":
                                self.adauga_client_ui()
                            case "1.4":
                                self.modif_client_ui()
                            case "1.5":
                                self.adauga_inchiriere_ui()
                            case "E":
                                break
                            case _:
                                print("Optiune invalida!")
                case "2":
                    while True:
                        print("2.1 Sterge o carte dupa id")
                        print("2.2 Sterge un client dupa id")
                        print("2.3 Returnare")
                        print("E. Inapoi")
                        option3 = input("Introduceti optiunea: ")
                        match option3:
                            case "2.1":
                                self.sterge_carte_id_ui()
                            case "2.2":
                                self.sterge_client_id_ui()
                            case "2.3":
                                self.sterge_inchiriere_ui()
                            case "E":
                                break
                            case _:
                                print("Optiune invalida!")
                case "3":
                    while True:
                        print("3.1 Cauta o carte dupa id")
                        print("3.2 Cauta un client dupa id")
                        print("E. Inapoi")
                        option4 = input("Introduceti optiunea: ")
                        match option4:
                            case "3.1":
                                self.cauta_carte_id_ui()
                            case "3.2":
                                self.cauta_client_id_ui()
                            case "E":
                                break
                            case _:
                                print("Optiune invalida!")
                case "4":
                    while True:
                        print("4.1 Filtreaza cartile dupa autor")
                        print("4.2 Filtreaza clientii dupa nume")
                        print("E. Inapoi")
                        option5 = input("Introduceti optiunea: ")
                        match option5:
                            case "4.1":
                                self.filtrare_autor_ui()
                            case "4.2":
                                self.filtrare_nume_ui()
                            case "E":
                                break
                            case _:
                                print("Optiune invalida!")
                case "5":
                    numar = input("Introduceti numarul de clienti care sa se genereze: ")
                    numar = int(numar)
                    self.randomClient(numar)
                    self.print_clienti(self.__client_service.get_clienti())
                case "6":
                    while True:
                        print("6.1 Clientii care au carti inchiriate ordonati dupa numarul de carti")
                        print("6.2 Cele mai inchiriate carti")
                        print("6.3 Top 20% clienti")
                        print("6.4 Top 20% carti")
                        print("6.5 Cele mai inchiriate carti cu merge sort")
                        print("6.6 Cele mai multe inchirieri ordonati si dupa nume gnomesort")
                        print("E. Inapoi")
                        option6 = input("Introduceti optiunea: ")
                        match option6:
                            case "6.1":
                                self.cele_mmulte_carti_ui()
                            case "6.2":
                                self.cele_mmulte_inchirieri_ui()
                            case "6.3":
                                self.top_20_percent_ui()
                            case "6.4":
                                self.top_20_p_books_ui()
                            case "6.5":
                                self.cele_mmulte_inchirieri_ui_merge()
                            case "6.6":
                                self.cele_mmulte_carti_ui_bingo()
                            case "E":
                                break
                            case _:
                                print("Optiune invalida!")
                case "D":
                    self.__carti_service.add_default_carti()
                case "DC":
                    self.__client_service.add_default_clienti()
                case "P":
                    self.print_carti(self.__carti_service.get_carti())
                case "PC":
                    self.print_clienti(self.__client_service.get_clienti())
                case "PI":
                    self.print_inchirieri(self.__inchirier_service.get_all_inchirieri())
                case "E":
                    break
                case _:
                    print("Optiune invalida!")
