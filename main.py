from area_calculator.figures import Figure, Circle, Triangle


def main():
    print("Какаую фигуру будем считать? (1 - круг, 2- треугольник)")
    user_input = input()

    match(user_input):
        case '1':
            f = Circle(10)
        case '2':
            f = Triangle(3, 4, 5)
        case _:
            f = None

    if f:
        print(get_area(f))


def get_area(f: Figure):
    # do something
    area = f.get_area()
    # do smoething else
    return area


main()
