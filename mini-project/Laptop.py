from product import Product


class Laptop(Product):

    def __init__(self, category: str, name: str, price: float, quantity: int,
                 Brand: str, Diagonal: float, Weight: float, Processor_cores: int,
                 Operative_memory: int):
        super().__init__(
            'Ноутбуки',
            name,
            price,
            quantity
        )
        self.Brand = Brand
        self.Diagonal = Diagonal
        self.Weight = Weight
        self.Processor_cores = Processor_cores
        self.Operative_memory = Operative_memory
