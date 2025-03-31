class ClientInchirieri:
    def __init__(self,cnp:int):
        self.__cnp = cnp
        self.__nume = ""
        self.__nr_carti = 1

    @property
    def cnp(self):
        return self.__cnp
    @property
    def nume(self):
        return self.__nume
    @property
    def nr_carti(self):
        return self.__nr_carti

    @nume.setter
    def nume(self,nume:str):
        self.__nume = nume

    def increase_nr_carti(self):
        self.__nr_carti += 1

    def __str__(self):
        return f"[{self.nume}, {self.nr_carti}]"


class CartiInchirieri:
    def __init__(self,id:int):
        self.__id = id
        self.__titlu = ""
        self.__nr_inchirieri = 1

    @property
    def id(self):
        return self.__id
    @property
    def titlu(self):
        return self.__titlu
    @titlu.setter
    def titlu(self,titlu:str):
        self.__titlu = titlu
    @property
    def nr_inchirieri(self):
        return self.__nr_inchirieri
    def increase_nr_inchirieri(self):
        self.__nr_inchirieri += 1

    def __str__(self):
        return f"[{self.id}, {self.titlu}, {self.nr_inchirieri}]"


