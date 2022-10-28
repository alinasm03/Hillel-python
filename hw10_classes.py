class Triangle:
    def __init__(self, a: float, b: float, c: float):
        """
        Ініціалізація змінних - сторони трикутника
        :param a: сторона трикутника a
        :param b: сторона трикутника b
        :param c: сторона трикутника c
        """
        self.a = a
        self.b = b
        self.c = c

    def exists(self) -> bool:
        """
        Метод перевіряє чи існує трикутник
        :return: повертає True/False
        """
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False

    def triangle_perimeter(self) -> float:
        """
        :return: периметр трикутника, якщо він існує, інакше - 0
        """
        if self.exists():
            return self.a + self.b + self.c
        else:
            return 0

    def triangle_square(self) -> float:
        """
        :return: площу трикутника, якщо він існує, інакше - 0
        """
        if self.exists():
            p = self.triangle_perimeter() / 2
            square = pow(p * (p - self.a) * (p - self.b) * (p - self.c), 0.5)
            return square
        else:
            return 0


if __name__ == '__main__':

    def get_length_sides(name: str) -> float:
        """
        :param name: назва сторони трикутника
        :return: довжину сторони трикутника
        """
        while True:
            side = input(f'{name}')
            try:
                side = float(side)
            except ValueError:
                print('Введіть, будь ласка, число!')
                continue
            if side > 0:
                return side
            else:
                print('Введіть, будь ласка, додатнє число!')

    a0 = get_length_sides('a: ')
    b0 = get_length_sides('b: ')
    c0 = get_length_sides('c: ')
    tr = Triangle(a0, b0, c0)
    print(f'Чи існує трикутник? {tr.exists()}')
    print(f'Периметр трикутника: {tr.triangle_perimeter()}')
    print(f'Площа трикутника: {tr.triangle_square()}')
