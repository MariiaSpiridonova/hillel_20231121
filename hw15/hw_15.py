class Triangle():
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3


class TriangleChecker():
    def is_triangle(self):
        if (type(self.side_1) == int and type(self.side_2) == int
                and type(self.side_3) == int):
            if self.side_1 > 0 and self.side_2 > 0 and self.side_3 > 0:
                if ((self.side_1 + self.side_2) <= self.side_3 or
                        (self.side_1 + self.side_3) <= self.side_2 or \
                        (self.side_2 + self.side_3) <= self.side_1):
                    return "Жаль, але з цього трикутник не зробити"
                else:
                    return "Ура, можна побудувати трикутник!"
            else:
                return "З негативними числами нічого не вийде!"
        else:
            return "Потрібно вводити тільки числа!"


class ExtTriangle(Triangle, TriangleChecker):
    pass


triangle_1 = ExtTriangle(3, 3, 4)
print(triangle_1.is_triangle())

triangle_2 = ExtTriangle(3, 3, -4)
print(triangle_2.is_triangle())

triangle_3 = ExtTriangle(3, 3, "d")
print(triangle_3.is_triangle())

triangle_4 = ExtTriangle(3, 3, 7)
print(triangle_4.is_triangle())
