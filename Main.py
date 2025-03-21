import sys

# Определяем базовый класс для фигур
class Shape:
    _id_counter = 1

    def __init__(self, shape_type):
        self.id = Shape._id_counter
        Shape._id_counter += 1
        self.shape_type = shape_type

    def __str__(self):
        return f"{self.shape_type} (ID: {self.id})"

# Класс для точки
class Point(Shape):
    def __init__(self, x, y):
        super().__init__("Point")
        self.x = x
        self.y = y

    def __str__(self):
        return f"{super().__str__()} - Coordinates: ({self.x}, {self.y})"

# Класс для отрезка
class Line(Shape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__("Line")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return (f"{super().__str__()} - Start: ({self.x1}, {self.y1}), "
                f"End: ({self.x2}, {self.y2})")

# Класс для круга
class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__("Circle")
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"{super().__str__()} - Center: ({self.x}, {self.y}), Radius: {self.r}"

# Класс для квадрата
class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__("Square")
        self.x = x
        self.y = y
        self.side = side

    def __str__(self):
        return f"{super().__str__()} - Top-left: ({self.x}, {self.y}), Side: {self.side}"

# Список для хранения фигур
shapes = []

# Функция для обработки команды создания фигур
def create_shape(tokens):
    if len(tokens) < 2:
        print("Ошибка: недостаточно параметров.")
        return

    shape_type = tokens[1].lower()

    try:
        if shape_type == "point":
            if len(tokens) != 4:
                print("Использование: create point <x> <y>")
                return
            x, y = float(tokens[2]), float(tokens[3])
            shape = Point(x, y)
        elif shape_type == "line":
            if len(tokens) != 6:
                print("Использование: create line <x1> <y1> <x2> <y2>")
                return
            x1, y1, x2, y2 = map(float, tokens[2:6])
            shape = Line(x1, y1, x2, y2)
        elif shape_type == "circle":
            if len(tokens) != 5:
                print("Использование: create circle <x> <y> <radius>")
                return
            x, y, r = float(tokens[2]), float(tokens[3]), float(tokens[4])
            shape = Circle(x, y, r)
        elif shape_type == "square":
            if len(tokens) != 5:
                print("Использование: create square <x> <y> <side>")
                return
            x, y, side = float(tokens[2]), float(tokens[3]), float(tokens[4])
            shape = Square(x, y, side)
        else:
            print(f"Неизвестный тип фигуры: {shape_type}")
            return

        shapes.append(shape)
        print(f"Фигура создана: {shape}")

    except ValueError:
        print("Ошибка: параметры должны быть числами.")

# Функция для удаления фигуры по ID
def delete_shape(tokens):
    if len(tokens) != 2:
        print("Использование: delete <id>")
        return

    try:
        id_to_delete = int(tokens[1])
        for shape in shapes:
            if shape.id == id_to_delete:
                shapes.remove(shape)
                print(f"Фигура с ID {id_to_delete} удалена.")
                return
        print(f"Фигура с ID {id_to_delete} не найдена.")
    except ValueError:
        print("Ошибка: ID должен быть целым числом.")

# Функция для вывода списка фигур
def list_shapes():
    if not shapes:
        print("Нет созданных фигур.")
    else:
        print("Список фигур:")
        for shape in shapes:
            print(f"  {shape}")

# Основной цикл программы
def main():
    print("Простой векторный редактор (CLI)")
    print("Доступные команды:")
    print("  create <figure_type> [parameters] - создать фигуру")
    print("      Типы: point, line, circle, square")
    print("  delete <id> - удалить фигуру по ID")
    print("  list - показать список фигур")
    print("  exit - выход из программы")

    while True:
        command = input("Введите команду: ").strip()
        if not command:
            continue

        tokens = command.split()

        if tokens[0].lower() == "create":
            create_shape(tokens)
        elif tokens[0].lower() == "delete":
            delete_shape(tokens)
        elif tokens[0].lower() == "list":
            list_shapes()
        elif tokens[0].lower() == "exit":
            print("Выход из программы.")
            sys.exit(0)
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()
