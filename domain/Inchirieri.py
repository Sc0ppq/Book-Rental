class Inchirieri:
    def __init__(self, carte_id, client_cnp):
        self.__carte_id = carte_id
        self.__client_cnp = client_cnp

    @property
    def carte_id(self):
        return self.__carte_id
    @property
    def client_cnp(self):
        return self.__client_cnp

    def __str__(self):
        return f"[{self.carte_id}, {self.client_cnp}]"

    def __eq__(self, other):
        return self.__carte_id == other.carte_id and self.__client_cnp == other.client_cnp