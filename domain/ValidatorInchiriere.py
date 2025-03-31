from domain.Inchirieri import Inchirieri

class ValidatorInchiriere:
    def validate(self, inchiriere:Inchirieri):
        """
        Valideaza datele unei inchirieri
        :param inchiriere: inchirierea validata
        :return: -; se arunca eroare in caz ca datele sunt invalide
        """
        errors = []
        if type(inchiriere.carte_id) != int:
            errors.append("ID-ul cartii trebuie sa fie un numar intreg!")
        if type(inchiriere.client_cnp) != int:
            errors.append("CNP-ul trebuie sa contina doar numere!")
        if len(str(inchiriere.client_cnp)) != 13:
            errors.append("CNP-ul trebuie sa aiba 13 cifre!")

        if len(errors)>0:
            error_message = '\n'.join(errors)
            raise ValueError(error_message)