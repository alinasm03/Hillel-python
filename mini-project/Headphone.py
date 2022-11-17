from product import Product


class Headphone(Product):

    def __init__(self, category: str, name: str, price: float, quantity: int,
                 Brand: str, Bluetooth: bool, Type: str, Vacuum: bool,
                 Battery: int):
        super().__init__(
            'Навушники',
            name,
            price,
            quantity
        )
        self.Brand = Brand
        self.Bluetooth = Bluetooth
        self.Type = Type
        self.Vacuum = Vacuum
        self.Battery = Battery
