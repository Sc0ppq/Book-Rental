from ui.console import Console
from domain.ValidatorCarte import ValidatorCarte
from domain.ValidatorClient import ValidatorClient
from domain.ValidatorInchiriere import ValidatorInchiriere
from repo.CartiRepo import CartiRepository, CartiFileRepo
from repo.ClientiRepo import ClientRepository,ClientiFileRepo
from repo.InchirieriRepo import InchirieriRepo
from service.CartiService import CartiService
from service.ClientiService import ClientiService
from service.InchirieriService import InchirieriService

def main():
    validator_c = ValidatorCarte()
    #carte_repo = CartiRepository()
    carte_repo = CartiFileRepo('data/carti.txt')
    carte_service = CartiService(carte_repo, validator_c)

    validator_cl = ValidatorClient()
    #client_repo = ClientRepository()
    client_repo = ClientiFileRepo('data/clienti.txt')
    client_service = ClientiService(client_repo, validator_cl)

    validator_i = ValidatorInchiriere()
    inchirier_repo = InchirieriRepo('data/inchirieri.txt')
    inchirier_service = InchirieriService(carte_repo, client_repo, inchirier_repo,validator_i)

    console = Console(carte_service, client_service, inchirier_service)
    console.run()


main()