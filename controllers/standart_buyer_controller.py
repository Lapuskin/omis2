from interfaces.buyer_controller_interface import BuyerControllerInterface
from repo.model import Buyer


class StandartBuyerController(BuyerControllerInterface):
    _buyer_repo = '../buyer_repo'

    def get_all_buyers(self)-> list[Buyer]:
        pass

    def get_buyer(self, id: int)-> Buyer:
        pass

    def create_buyer(self, buyer: Buyer)-> Buyer:
        pass

    def edit_buyer(self, buyer: Buyer)-> Buyer:
        pass