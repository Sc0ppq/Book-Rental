from domain.Carte import Carte

class ValidatorCarte:
    def validate(self, carte:Carte):
        """
        Valideaza datele unei carti
        :param carte: cartea de validat
        :return: -; arunca eroare in caz ca datele sunt invalide
        """
        errors = []
        if type(carte.id) != int:
            errors.append("ID-ul cartii trebuie sa fie un numar intreg!")
        if len(carte.titlu)<2:
            errors.append("Titlul trebuie sa aiba cel putin un caracter!")
        if len(carte.autor)<2:
            errors.append("Autorul trebuie sa aiba cel putin un caracter!")
        if len(carte.desc)<2:
            errors.append("Descrierea trebuie sa aiba cel putin un caracter!")

        if len(errors)>0:
            error_message = '\n'.join(errors)
            raise ValueError(error_message)