from abc import ABC, abstractmethod


class IntarfaceFabric(ABC):
    @abstractmethod
    def create_window(self):
        pass

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_field(self):
        pass

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_layer(self):
        pass
