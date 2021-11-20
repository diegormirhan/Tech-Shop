from utils.helper import formata_float_str_moeda as formata


class Produto:
    counter: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__code: int = Produto.counter
        self.__name: str = name
        self.__price: float = price
        Produto.counter += 1

    @property
    def code(self) -> int:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f'Código: {self.code} \n' \
               f'Nome: {self.name} \n' \
               f'Preço: {formata(self.price)} \n'

