import pickle

class Shape:
    def __init__(self, coordinate:list) -> None:
        self.coordinate = coordinate

    def show(self) -> None:
        raise NotImplementedError

    def save(self, filename):
        with open(filename, 'ab') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        shapes = []
        try:
            with open(filename, 'rb') as f:
                while True:
                    try:
                        shape = pickle.load(f)
                        shapes.append(shape)
                    except EOFError:
                        break
        except FileNotFoundError:
            print(f"Файл {filename} не найден")
        return shapes


class Square(Shape):
    def __init__(self, Shape, length:int) -> None:
        super().__init__(Shape.coordinate)
        self.length = length

    def show(self) -> None:
        print(f"Origin: {self.coordinate}, Side length: {self.length}. Shape: Square")


class Rectangle(Shape):
    def __init__(self, Shape, width:int, height:int) -> None:
        super().__init__(Shape.coordinate)
        self.width = width
        self.height = height

    def show(self) -> None:
        print(f"Origin: {self.coordinate}, Width: {self.width}, Height: {self.height}. Shape: Rectangle")


class Circle(Shape):
    def __init__(self, Shape, radius:int) -> None:
        super().__init__(Shape.coordinate)
        self.radius = radius

    def show(self) -> None:
        print(f"Origin: {self.coordinate}, Radius: {self.radius}. Shape: Circle")


class Ellipse(Shape):
    def __init__(self, Shape, width:int, height:int) -> None:
        super().__init__(Shape.coordinate)
        self.width = width
        self.height = height

    def show(self) -> None:
        print(f"Origin: {self.coordinate}, Width: {self.width}, Height: {self.height}. Shape: Ellipse")

