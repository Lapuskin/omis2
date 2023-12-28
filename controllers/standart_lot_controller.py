from interfaces.seller_controller_Interface import SellerControllerInterface
from repo.model import Lot


class StandartLotController(SellerControllerInterface):
    _lot_repo = '../lot_repo'
    _bid_repo = '../bid_repo'

    def get_lot(self, id: int) -> Lot:
        pass

    def get_lots(self) -> list[Lot]:
        pass

    def define_winner(self, id: int) -> Lot:
        pass

    def add_bid(self, bid: float) -> float:
        pass

    def create_lot(self, lot: Lot) -> Lot:
        pass

    def edit_lot(self, lot: Lot) -> Lot:
        pass