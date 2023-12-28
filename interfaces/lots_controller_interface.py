from abc import ABC, abstractmethod

from repo.model import Lot


class LotsControllerInterface(ABC):
    @abstractmethod
    def get_lot(self, id: int) -> Lot:
        pass

    @abstractmethod
    def get_lots(self) -> list[Lot]:
        pass

    @abstractmethod
    def define_winner(self, id: int) -> Lot:
        pass

    @abstractmethod
    def add_bid(self, bid: float) -> float:
        pass

    @abstractmethod
    def create_lot(self, lot: Lot) -> Lot:
        pass

    @abstractmethod
    def edit_lot(self, lot: Lot) -> Lot:
        pass
