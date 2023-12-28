from interfaces.seller_controller_Interface import SellerControllerInterface
from repo.model import Seller, Review


class StandartSellerController(SellerControllerInterface):
    _seller_repo = '../seller_repo'
    _review_repo = '../review_repo'

    def get_seller(self, id: int) -> Seller:
        pass

    def get_all_sellers(self) -> list[Seller]:
        pass

    def register_review(self, review: Review) -> Review:
        pass

    def create_seller(self, seller: Seller) -> Seller:
        pass

    def edit_seller(self, seller: Seller) -> Seller:
        pass