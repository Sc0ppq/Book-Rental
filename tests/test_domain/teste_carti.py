from domain.Carte import Carte
from domain.ValidatorCarte import ValidatorCarte
import unittest

class TestCarte(unittest.TestCase):

    def test_create_carte(self):
        carte = Carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        assert carte.id == 1
        assert carte.titlu == '1984'
        assert carte.autor == 'George Orwell'
        assert carte.desc == 'A dystopian novel.'

    def test_equals_carte(self):
        carte1 = Carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        carte2 = Carte(1, 'Animal Farm', 'George Orwell', 'A political allegory.')
        assert carte1 == carte2

        carte3 = Carte(2, 'Brave New World', 'Aldous Huxley', 'A dystopian novel.')
        assert carte1 != carte3

    def test_validate_carte(self): #BLACKBOX
        validator = ValidatorCarte()

        id_invalid = Carte('a', 'titlu', 'autor', 'desc')
        try:
            validator.validate(id_invalid)
            assert False
        except ValueError as e:
            assert True
            assert str(e) == "ID-ul cartii trebuie sa fie un numar intreg!"

        titlu_invalid = Carte(1, '', 'autor', 'desc')
        try:
            validator.validate(titlu_invalid)
            assert False
        except ValueError as e:
            assert True
            assert str(e) == "Titlul trebuie sa aiba cel putin un caracter!"

        autor_invalid = Carte(1, 'titlu', '', 'desc')
        try:
            validator.validate(autor_invalid)
            assert False
        except ValueError as e:
            assert True
            assert str(e) == "Autorul trebuie sa aiba cel putin un caracter!"

        desc_invalida = Carte(1, 'titlu', 'autor', '')
        try:
            validator.validate(desc_invalida)
            assert False
        except ValueError as e:
            assert True
            assert str(e) == "Descrierea trebuie sa aiba cel putin un caracter!"

        carte_valid = Carte(1, '1984', 'George Orwell', 'A dystopian novel.')
        try:
            validator.validate(carte_valid)
            assert True
        except ValueError:
            assert False

