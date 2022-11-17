from product import Product


class SmartWatch(Product):

    def __init__(self, category: str, name: str, price: float, quantity: int,
                 Brand: str, Body_size: float, Sim_support: str, GPS: bool,
                 Battery: int):
        super().__init__(
            'Смарт-годинники',
            name,
            price,
            quantity
        )
        self.Brand = Brand
        self.Body_size = Body_size
        self.Sim_support = Sim_support
        self.GPS = GPS
        self.Battery = Battery
