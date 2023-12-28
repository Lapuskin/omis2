from abc import ABC, abstractmethod
from typing import Callable, Any


class InterfaceObject(ABC):
    @abstractmethod
    def set_size(self, length: int, width: int) -> None:
        pass

    @abstractmethod
    def show(self) -> None:
        pass


class Field(InterfaceObject):
    def set_type(self, type: str) -> None:
        pass


class Button(InterfaceObject, ABC):
    def set_action(self, action: Callable[..., Any]) -> None:
        pass


class Layer(InterfaceObject):
    def set_type(self, type: str) -> None:
        pass

    def add(self, object: InterfaceObject, x: int, y: int):
        pass


class Window(InterfaceObject):
    def add_layer(self, layer: Layer) -> None:
        pass


class Table(InterfaceObject):
    def set_base(self, rows: int, columns: int) -> None:
        pass
