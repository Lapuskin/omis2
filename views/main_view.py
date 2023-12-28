from interfaces.interface_fabric import IntarfaceFabric
from views.standart_interface_fabric import StandartInterfaceFabric


class MainView:
    def __init__(self):
        self._fabric = StandartInterfaceFabric()
        self.__windows: {str: str} = {'/': 'main.html',
                                     '/lot_edit': 'lot_edit.html',
                                     '/buyer_edit': 'buyer_edit.html',
                                     '/buyer_create': 'buyer_create.html',
                                     '/seller_create': 'seller_create.html',
                                     '/lot_create': 'lot_create.html',
                                      }

    def create_interface(self) -> None:
        pass

    def get_windows(self) -> dict:
        return self.__windows

    def show_interface(self) -> None:
        pass

    def show_window(self) -> None:
        pass
