class Client:
    def __init__(self, id:int, nume:str, CNP:int):
        self.__id = id
        self.__nume = nume
        self.__CNP = CNP

    @property
    def id(self):
        return self.__id
    @property
    def nume(self):
        return self.__nume
    @property
    def CNP(self):
        return self.__CNP
    @id.setter
    def id(self, id:int):
        if not isinstance(id, int):
            raise TypeError("ID-ul trebuie sa fie un numar intreg!")
        self.__id = id
    @nume.setter
    def nume(self, nume:str):
        self.__nume = nume
    @CNP.setter
    def CNP(self, CNP:int):
        if not isinstance(CNP, int):
            raise TypeError("CNPul trebuie sa fie format din numere!")
        self.__CNP = CNP

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.__id == other.__id and self.__CNP == other.__CNP

    def __str__(self):
        return "Client: ID = " + str(self.__id) + "; Nume = " + self.__nume + "; CNP = " + str(self.__CNP)
