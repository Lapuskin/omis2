from abc import ABC, abstractmethod

from repo.model import Seller, Review


class SellerControllerInterface(ABC):
    @abstractmethod
    def get_seller(self, id: int) -> Seller:
        pass

    @abstractmethod
    def get_all_sellers(self) -> list[Seller]:
        pass

    @abstractmethod
    def register_review(self, review: Review)-> Review:
        pass

    @abstractmethod
    def create_seller(self, seller: Seller)-> Seller:
        pass

    @abstractmethod
    def edit_seller(self, seller: Seller)-> Seller:
        pass
