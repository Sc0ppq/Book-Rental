class Carte:

    def  __init__(self, id: int, titlu:str, autor:str,desc:str):
        self.__id = id
        self.__titlu = titlu
        self.__autor = autor
        self.__desc = desc


    
    @property
    def id(self):
        return self.__id
    @property
    def titlu(self):
        return self.__titlu
    @property
    def autor(self):
        return self.__autor
    @property
    def desc(self):
        return self.__desc

    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise ValueError("ID-ul trebuie sa fie un numar intreg!")
        self.__id = id

    @titlu.setter
    def titlu(self, titlu):
        if not isinstance(titlu, str):
            raise ValueError("Titlu must be a string")
        self.__titlu = titlu

    @autor.setter
    def autor(self, autor):
        if not isinstance(autor, str):
            raise ValueError("Autor must be a string")
        self.__autor = autor

    @desc.setter
    def desc(self, desc):
        if not isinstance(desc, str):
            raise ValueError("Desc must be a string")
        self.__desc = desc

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id == other.id

    def __str__(self):
        return "Carte: ID = " + str(self.__id) + "; Titlu = " + self.__titlu + "; Autor = " + self.__autor + "; Descriere = " + self.__desc