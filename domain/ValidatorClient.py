
from domain.Client import Client

class ValidatorClient:
    def validate(self, client:Client):
        """
        Valideaza datele unui client
        :param client: clientul de validat
        :return: -; se arunca eroare in caz ca datele sunt invalide
        """
        errors = []
        if type(client.id) != int:
            errors.append("ID-ul clientului trebuie sa fie un numar intreg!")
        if type(client.CNP) != int:
            errors.append("CNP-ul trebuie sa contina doar numere!")
        if len(str(client.CNP)) != 13:
            errors.append("CNP-ul trebuie sa aiba 13 cifre!")
        if len(client.nume) < 2:
            errors.append("Numele trebuie sa aiba cel putin un caracter!")

        if len(errors)>0:
            error_message = '\n'.join(errors)
            raise ValueError(error_message)