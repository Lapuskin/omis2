from abc import ABC, abstractmethod

from repo.model import Buyer


class BuyerControllerInterface(ABC):
    @abstractmethod
    def get_all_buyers(self) -> list[Buyer]:
        pass

    @abstractmethod
    def get_buyer(self, id: int) -> Buyer:
        pass

    @abstractmethod
    def create_buyer(self, buyer: Buyer) -> Buyer:
        pass

    @abstractmethod
    def edit_buyer(self, buyer: Buyer) -> Buyer:
        pass
